import json
import re
from typing import Any, Dict, List, Optional, Union

DEPENDENCE_KEYS = {
    "control": "ControlDependence",
    "data": "DataDependence",
    "infoflow": "InformationFlow",
}

# Accept both spellings for the info‑flow sources key
SOURCES_KEYS = {
    "control": ["ControlDependenceSources"],
    "data": ["DataDependenceSources"],
    "infoflow": ["InformationFlowSources", "InfomationFlowSources"],
}


def extract_code_blocks(text: str) -> List[str]:
    code_block_pattern = re.compile(r"```(?:\w+)?\n?(.*?)```", re.DOTALL)
    # inst_block_pattern = re.compile(r"\[INST\]\n?(.*?)\n?\[/INST\]", re.DOTALL)

    blocks = code_block_pattern.findall(text)
    # blocks += inst_block_pattern.findall(text)
    return blocks


def parse_json_code_block(block: str) -> Union[Dict[str, Any], None]:
    try:
        return json.loads(block)
    except json.JSONDecodeError:
        return None


def is_continuous_trace(trace: List[Dict[str, Any]]) -> bool:
    for i in range(len(trace) - 1):
        if trace[i]["to"][0] != trace[i + 1]["from"][0]:
            return False
    return True


def _extract_sources(parsed: Dict[str, Any], task_type: str) -> Optional[List[Any]]:
    """
    Look for a *sources‑only* key (e.g., "DataDependenceSources") in the
    parsed JSON block.  If found and structurally valid, return its value;
    otherwise return None so that the caller can keep searching/try legacy
    formats.
    """
    # Possible keys for this task type (e.g., ["DataDependenceSources"])
    for key in SOURCES_KEYS[task_type]:
        if key not in parsed:
            continue

        sources_list = parsed[key]

        # --- Structural validation ---------------------------------------
        if task_type == "control":
            # Must be a list of ints
            if not (
                isinstance(sources_list, list)
                and all(isinstance(n, int) for n in sources_list)
            ):
                return None
        else:  # "data" or "infoflow"
            # Must be a list of ["var", line] pairs
            if not (
                isinstance(sources_list, list)
                and all(
                    isinstance(pair, list)
                    and len(pair) == 2
                    and isinstance(pair[0], str)
                    and isinstance(pair[1], int)
                    for pair in sources_list
                )
            ):
                return None

        # Everything looks good
        return sources_list

    # No recognised sources key found in this block
    return None


def parse_dependence_output(
    text: str, task_type: str = "control", trace: bool = True
) -> Optional[Dict[str, Any]]:
    key = DEPENDENCE_KEYS.get(task_type)
    if not key:
        return None

    code_blocks = extract_code_blocks(text)
    attempted_blocks = (
        code_blocks if code_blocks else [text]
    )  # Include raw text if no code blocks found

    for block in attempted_blocks:
        parsed = parse_json_code_block(block)
        # ---------- 1) New “Sources”‑only format ----------
        if parsed:
            sources = _extract_sources(parsed, task_type)
            if sources is not None:
                # Already validated in _extract_sources
                return {"sources": sources}

        if parsed and key in parsed:

            # ---------- 2) Legacy answer / trace format ----------
            answer = bool(parsed[key])
            trace_data = parsed.get("Trace", []) if trace and answer else []

            if task_type == "control":
                trace_data = [int(x) for x in trace_data] if trace_data else []

            elif task_type == "data":
                if not all(
                    isinstance(t, dict)
                    and isinstance(t.get("from"), list)
                    and len(t["from"]) == 2
                    and isinstance(t.get("to"), list)
                    and len(t["to"]) == 2
                    and isinstance(t["from"][0], str)
                    and isinstance(t["from"][1], int)
                    and isinstance(t["to"][0], str)
                    and isinstance(t["to"][1], int)
                    for t in trace_data
                ):
                    return None
                trace_data = [
                    {
                        "from": [t["from"][0], t["from"][1]],
                        "to": [t["to"][0], t["to"][1]],
                    }
                    for t in trace_data
                ]

            elif task_type == "infoflow":
                if not all(
                    isinstance(t, dict)
                    and "from" in t
                    and "to" in t
                    and "type" in t
                    and isinstance(t["from"], list)
                    and len(t["from"]) >= 2
                    and isinstance(t["to"], list)
                    and len(t["to"]) >= 2
                    and isinstance(t["from"][0], str)
                    and isinstance(t["from"][1], int)
                    and isinstance(t["to"][0], str)
                    and isinstance(t["to"][1], int)
                    and t["type"] in {"data", "control"}
                    for t in trace_data
                ):
                    return None
                trace_data = [
                    {
                        "from": [
                            t["from"][0],
                            t["from"][1],
                            len(t["from"]) == 3 and t["from"][2] == "use",
                        ],
                        "to": [
                            t["to"][0],
                            t["to"][1],
                            len(t["to"]) == 3 and t["to"][2] == "use",
                        ],
                        "type": t["type"],
                    }
                    for t in trace_data
                ]

            if task_type in {"data", "infoflow"} and not is_continuous_trace(
                trace_data
            ):
                return None

            return {"answer": answer, "trace": trace_data}

    return None


# ---------------------------
# Test Cases
# ---------------------------


def run_tests():
    test_cases = [
        {
            "name": "control valid",
            "text": """```json\n{\n  \"ControlDependence\": true,\n  \"Trace\": [1, 3, 5]\n}\n```""",
            "type": "control",
            "expected": {"answer": True, "trace": [1, 3, 5]},
        },
        {
            "name": "control false",
            "text": """```json\n{\n  \"ControlDependence\": false\n}\n```""",
            "type": "control",
            "expected": {"answer": False, "trace": []},
        },
        {
            "name": "data valid",
            "text": """```json\n{\n  \"DataDependence\": true,\n  \"Trace\": [\n    { \"from\": [\"value\", 2], \"to\": [\"step\", 3] },\n    { \"from\": [\"step\", 3], \"to\": [\"step\", 9] }\n  ]\n}\n```""",
            "type": "data",
            "expected": {
                "answer": True,
                "trace": [
                    {"from": ["value", 2], "to": ["step", 3]},
                    {"from": ["step", 3], "to": ["step", 9]},
                ],
            },
        },
        {
            "name": "data invalid trace",
            "text": """```json\n{\n  \"DataDependence\": true,\n  \"Trace\": [\n    { \"from\": [\"value\"], \"to\": [\"step\", 3] }\n  ]\n}\n```""",
            "type": "data",
            "expected": None,
        },
        {
            "name": "no language specified",
            "text": """```\n{\n  "ControlDependence": true,\n  "Trace": [2, 4, 6]\n}\n```""",
            "type": "control",
            "expected": {"answer": True, "trace": [2, 4, 6]},
        },
        {
            "name": "raw json input only",
            "text": """{
        "InformationFlow": true,
        "Trace": [
            {
            "from": ["foo", 1],
            "to": ["bar", 2],
            "type": "control"
            }
        ]
        }""",
            "type": "infoflow",
            "expected": {
                "answer": True,
                "trace": [
                    {
                        "from": ["foo", 1, False],
                        "to": ["bar", 2, False],
                        "type": "control",
                    }
                ],
            },
        },
        {
            "name": "raw json input only 2",
            "text": """{\n  \"ControlDependence\": true\n}""",
            "type": "control",
            "expected": {"answer": True, "trace": []},
        },
        {
            "name": "infoflow valid",
            "text": """```json\n{\n  \"InformationFlow\": true,\n  \"Trace\": [\n    {\n      \"from\": [\"balance\", 4],\n      \"to\": [\"balance\", 5],\n      \"type\": \"data\"\n    },\n    {\n      \"from\": [\"balance\", 5],\n      \"to\": [\"balance\", 6, \"use\"],\n      \"type\": \"data\"\n    }\n  ]\n}\n```""",
            "type": "infoflow",
            "expected": {
                "answer": True,
                "trace": [
                    {
                        "from": ["balance", 4, False],
                        "to": ["balance", 5, False],
                        "type": "data",
                    },
                    {
                        "from": ["balance", 5, False],
                        "to": ["balance", 6, True],
                        "type": "data",
                    },
                ],
            },
        },
        {
            "name": "infoflow invalid type",
            "text": """```json\n{\n  \"InformationFlow\": true,\n  \"Trace\": [\n    {\n      \"from\": [\"x\", 1],\n      \"to\": [\"y\", 2],\n      \"type\": \"badtype\"\n    }\n  ]\n}\n```""",
            "type": "infoflow",
            "expected": None,
        },
        {
            "name": "mixed code blocks",
            "text": """
Here is some explanation.

```python
print("Hello")
```

```json
{"ControlDependence": false}
```
some other text
```json
{
  "InformationFlow": true,
  "Trace": [
    {"from": ["x", 1], "to": ["y", 2], "type": "data"}
  ]
}
```

```text
Some text block
```
""",
            "type": "infoflow",
            "expected": {
                "answer": True,
                "trace": [
                    {"from": ["x", 1, False], "to": ["y", 2, False], "type": "data"}
                ],
            },
        },
        {
            "name": "data non-continuous trace",
            "text": """```json
        {
        "DataDependence": true,
        "Trace": [
            { "from": ["a", 1], "to": ["b", 2] },
            { "from": ["c", 2], "to": ["d", 3] }
        ]
        }
        ```""",
            "type": "data",
            "expected": None,
        },
        {
            "name": "infoflow non-continuous trace",
            "text": """{
        "InformationFlow": true,
        "Trace": [
            { "from": ["foo", 1], "to": ["bar", 2], "type": "control" },
            { "from": ["baz", 2], "to": ["qux", 3], "type": "control" }
        ]
        }""",
            "type": "infoflow",
            "expected": None,
        },
        {
            "name": "test",
            "text": """To determine if `(t,20)` has data dependence over `(k,33)` in the `main` function, we need to analyze the data flow and dependencies between these two variable instances.\n\n**Analysis**:\n- Line 33: `k = j - b[i]`, meaning `(k,33)` directly depends on `(j,31)` and `(b,27)`.\n- Line 31: `j` is the loop induction variable, initialized and updated within the loop.\n- Line 27: `b[i]` is an array element that depends on `(i,30)` and `(b,27)` itself.\n- Line 30: `i` is the outer loop induction variable, initialized and updated within the loop.\n- Line 20: `t = getint()`, meaning `(t,20)` is initialized here.\n\nThere is no direct or transitive chain of data dependence from `(t,20)` to `(k,33)`. The value of `t` is not used in the computation of `k` or any of its dependencies.\n\n**Output**:\n```json\n{\n  \"DataDependence\": false\n}\n```""",
            "type": "data",
            "expected": {"answer": False, "trace": []},
        },
        {
            "name": "test2",
            "text": """```json
{
  "DataDependence": true,
  "Trace": [
    { "from": ["i", 23], "to": ["b", 27] },
    { "from": ["b", 27], "to": ["k", 33] }
  ]
}
```""",
            "type": "data",
            "expected": {
                "answer": True,
                "trace": [
                    {"from": ["i", 23], "to": ["b", 27]},
                    {"from": ["b", 27], "to": ["k", 33]},
                ],
            },
        },
        {
            "name": "infoflow sources list with typo key",
            "text": """```json
{
  "InfomationFlowSources": [
    ["limit", 9],
    ["status", 2],
    ["status", 7],
    ["balance", 4],
    ["balance", 5]
  ]
}
```""",
            "type": "infoflow",
            "expected": {
                "sources": [
                    ["limit", 9],
                    ["status", 2],
                    ["status", 7],
                    ["balance", 4],
                    ["balance", 5],
                ]
            },
        },
        {
            "name": "data sources list",
            "text": """```json
{
  "DataDependenceSources": [
    ["value", 2],
    ["value", 5],
    ["total", 1]
  ]
}
```""",
            "type": "data",
            "expected": {"sources": [["value", 2], ["value", 5], ["total", 1]]},
        },
        {
            "name": "control sources list",
            "text": """```json
{
  "ControlDependenceSources": [5, 6, 8]
}
```""",
            "type": "control",
            "expected": {"sources": [5, 6, 8]},
        },
    ]

    for case in test_cases:
        result = parse_dependence_output(case["text"], case["type"])
        assert (
            result == case["expected"]
        ), f"Failed: {case['name']}\nExpected: {case['expected']}\nGot: {result}"

    print("All tests passed.")


if __name__ == "__main__":
    # Uncomment to run tests
    run_tests()

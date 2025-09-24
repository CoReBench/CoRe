# CoRe: Benchmarking LLMs’ Code Reasoning Capabilities through Static Analysis Tasks

📢 **News**: CoRe has been accepted as a **Spotlight Paper** at **NeurIPS 2025 Datasets & Benchmarks Track**! 🎉

This repository contains the source code, prompts, and annotation data for **CoRe**, a benchmark designed to evaluate LLMs’ **code reasoning capabilities** through **static analysis tasks** across C/C++, Java, and Python.

---

### 🔗 Links
- 📂 Dataset: [Hugging Face](https://huggingface.co/datasets/danningx/CoRe)
- 🌐 Website: [https://corebench.github.io](https://corebench.github.io)
- 📄 Paper (arXiv): [https://arxiv.org/abs/2507.05269](https://arxiv.org/abs/2507.05269)

---

### 📘 Overview

Large Language Models (LLMs) are increasingly applied to **program analysis and reasoning**. However, evaluating their ability to perform **static reasoning tasks** (beyond text generation) has been underexplored.

**CoRe** fills this gap by introducing:
- **Human-verified annotations** across C/C++, Java, Python programs.
- **Three task families** for static reasoning:
  - `data`: data dependency reasoning
  - `control`: control dependency reasoning
  - `infoflowdep`: information flow reasoning
- **Two modes**:
  - `source`: enumerate dependency sources
  - `trace`: pairwise classification + reasoning trace

---
###  📂 Repository Structure
```
.
├── raw_annotation/       # Human-verified annotations across C/C++, Java, Python
│   ├── C/
│   │   ├── code/         # Program source files
│   │   ├── label/        # Ground truth labels
│   │   └── meta_scan_result.json  # Static info scan results
│   ├── Java/
│   └── Python/
│
├── prompts/              # All prompts used for evaluation
│   ├── control_{Lang}_{source|trace}.jsonl
│   ├── data_{Lang}_{source|trace}.jsonl
│   └── infoflowdep_{Lang}_{source|trace}.jsonl
│   # Lang = C, Java, Python
│   # *_source.jsonl — prompts for source enumeration
│   # *_trace.jsonl — prompts for pairwise queries (classification + trace)
│
├── scripts/              # Scripts for running and evaluating LLMs
│   ├── run.py            # Run LLM experiments
│   ├── eval.py           # Evaluate model outputs
│   ├── parse_label.py    # Parse and structure label files
│   ├── parse_response.py # Parse model outputs
│   ├── utils.py
│   ├── ScanResults.py    # Process scan results
│   ├── run.sh            # Example run script
│   └── eval.sh           # Example eval script
│
├── lite.json             # Metadata for CoRe Lite subset

```



- `raw_annotation/`: Contains annotated programs in three languages (C/C++, Java, Python). Each contains:
    - `code/`: Source files
    - `label/`: Ground truth annotations
    - `meta_scan_result.json`: Static analysis results with structural info for target sampling and filtering
- `prompts/`: Contains prompt templates for each task type and language.
    - Files are named as: `{task}_{language}_{mode}.jsonl`
        - `{task}`: data, control, or infoflowdep
        - `{language}`: C, Java, Python
        - `{mode}`: source for source enumeration, trace for pairwise classification and trace
- `scripts/`:
    - `run.py`: Main runner for LLM experiments
    - `eval.py`: Evaluation script
    - `parse_label.py`, parse_response.py: Utilities for parsing labels and LLM responses
    - `run.sh`, `eval.sh`: Example scripts demonstrating usage
- `lite.json`: Defines the list of task IDs included in CoRe Lite, a smaller representative subset of the full benchmark.

---

### 📦 CoRe Lite
A smaller representative subset is available via `lite.json` for lightweight experimentation.

For usage, please see the "Example Usage" section below.
---


### 🚀 Quickstart

To run or evaluate models, checkout our scripts:
```
python scripts/run.py --help
python scripts/eval.py --help
```

Or use our shell scripts:

```
bash scripts/run.sh
bash scripts/eval.sh <response_folder>
```

By running `run.py`/`run.sh`, responses will be generated in jsonl files at `response_folder/model_name/response/xx.jsonl`. After generation, you can call:

```
bash eval.sh response_folder/model_name
```

This will evaluate all the files in the folder and generate a CSV file summarizing all the results.

#### Example Usage

Our data has two modes: `trace` and `source` (see section `overview` or paper for more details).


- To run experiments that ask to predict trace (data points with `category="trace"`):

  ```bash
  python run.py \
    --prompt CoRe/prompts \
    --result_folder CoRe/response \
    --model ds-v3 \
    --max_tokens 2048 \
    --temperature 0 \
    --trace
  ```
  
  This runs all the experiments that ask the model to predict trace and generates responses in the `CoRe/response` folder.

- To run experiments with source enumeration task (with CoRe Lite, data points with `category="source"`):

  ```bash
  python run.py \
    --prompt CoRe/prompts \
    --result_folder CoRe/response \
    --model ds-v3 \
    --max_tokens 2048 \
    --temperature 0 \
    --source \
    --lite CoRe/lite.json
  ```
  
  This runs all experiments with source mode, and `--lite` (required for `source` mode) specifies data points in CoRe Lite.

- After running either command, you can call `eval.sh` to evaluate the results.
  ```bash
  bash eval.sh CoRe/response/ds-v3
  ```

Before using the bash scripts, please double-check the bash scripts and update the paths and arguments.

**To run experiment or evaluate only on CoRe Lite, use the `--lite lite.json` argument when running `run.py` or `eval.py`.**


---
### 📜 Citation
```
@article{xie2025core,
  title={CORE: Benchmarking LLMs Code Reasoning Capabilities through Static Analysis Tasks},
  author={Xie, Danning and Zheng, Mingwei and Liu, Xuwei and Wang, Jiannan and Wang, Chengpeng and Tan, Lin and Zhang, Xiangyu},
  journal={arXiv preprint arXiv:2507.05269},
  year={2025}
}
```

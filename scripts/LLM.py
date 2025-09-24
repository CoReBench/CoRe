import json
import os
from typing import Union

import boto3
import google.generativeai as genai
from botocore.config import Config
from openai import OpenAI

aws_access_key = os.getenv("AWS_ACC_KEY")
aws_secret_key = os.getenv("AWS_SEC_KEY")
DS_KEY = os.getenv("DEEPSEEK_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# long timeout – only for Llama‑3 405 B & 70 B
BEDROCK_LLAMA_CFG = Config(
    read_timeout=900,  # 15 min
    connect_timeout=20,
    retries={"max_attempts": 10, "mode": "adaptive"},
)


class Claude:
    V3: str = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    V3_7: str = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
    V3_7_THINKING: str = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"


class DEEPSEEK:
    R1: str = "us.deepseek.r1-v1:0"  # For Bedrock
    V3: str = "deepseek-chat"  # For OpenAI-compatible endpoint


class OAI:
    GPT_4O: str = "gpt-4o"
    O3: str = "o3"
    O4_MINI: str = "o4-mini"


class QWEN:
    V3_235B: str = "qwen/qwen3-235b-a22b"


class LLAMA:
    V3_405: str = "meta.llama3-1-405b-instruct-v1:0"
    V3_70: str = "meta.llama3-1-70b-instruct-v1:0"


class GEMINI:
    PRO_2_5: str = "gemini-2.5-pro-preview-05-06"


THINKING_MODE_TOKENS = 1024


class LLM:
    ACCEPT = "application/json"
    CONTENT_TYPE = "application/json"
    BEDROCK = "bedrock-runtime"
    BODY = "body"
    COMPLETION = "completion"

    def __init__(
        self,
        model_id: str = Claude.V3,
        max_token_to_sample: int = 200,
        max_token: int = 204_800,
        temperature: float = 0.1,
        top_p: float = 0.9,
        region: str = "us-west-2",
    ) -> None:
        config = Config(
            read_timeout=1000, retries={"max_attempts": 10, "mode": "adaptive"}
        )
        self.model_id = model_id
        self.max_token_to_sample = max_token_to_sample
        self.max_token = max_token
        self.temperature = temperature
        self.top_p = top_p
        self.pred_fun = None
        if self.model_id in (Claude.V3, Claude.V3_7, Claude.V3_7_THINKING, DEEPSEEK.R1):
            self.bedrock = boto3.client(
                "bedrock-runtime",
                region_name=region,
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
            )
        if self.model_id == Claude.V3:
            self.max_token = 204_800
            self.pred_fun = self.predict_v3
        elif self.model_id == Claude.V3_7:
            self.max_token = 204_800
            self.pred_fun = self.predict_claude_3_7
        elif self.model_id == Claude.V3_7_THINKING:
            self.max_token = 204_800
            assert THINKING_MODE_TOKENS > self.max_token_to_sample
            self.pred_fun = self.predict_claude_3_7_thinking
        elif self.model_id == DEEPSEEK.R1:
            self.max_token = 163_840
            self.pred_fun = self.predict_deepseek_r1
        elif model_id == DEEPSEEK.V3:
            self.client = OpenAI(api_key=DS_KEY, base_url="https://api.deepseek.com")
            self.model_id = model_id
            self.pred_fun = self.predict_deepseek_v3_openai
        elif model_id in [OAI.GPT_4O, OAI.O3, OAI.O4_MINI]:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
            self.model_id = model_id
            self.pred_fun = self.predict_openai
        elif self.model_id == LLAMA.V3_405:  # or  self.model_id == LLAMA.V3_70:
            self.bedrock = boto3.client(
                "bedrock-runtime",
                region_name=region,
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                config=BEDROCK_LLAMA_CFG,
            )
            self.max_token = 128_000
            self.pred_fun = self.predict_llama
        elif model_id == QWEN.V3_235B:
            self.client = OpenAI(
                api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1"
            )
            self.model_id = model_id
            self.pred_fun = self.predict_openrouter
        elif model_id == GEMINI.PRO_2_5:
            genai.configure(api_key=GEMINI_API_KEY)
            self.client = genai
            self.model_id = model_id
            self.pred_fun = self.predict_gemini
        else:
            raise ValueError(f"The selected model id {self.model_id} is not supported")

    def predict(self, prompt: str) -> str:
        return self.pred_fun(prompt)

    def predict_deepseek_v3_openai(
        self, messages: Union[str, list[dict]]
    ) -> (str, int, int):
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]

        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_token_to_sample,
            stream=False,
        )

        output = response.choices[0].message.content
        usage = getattr(response, "usage", {})
        input_tokens = getattr(usage, "prompt_tokens", 0)
        output_tokens = getattr(usage, "completion_tokens", 0)

        return output, input_tokens, output_tokens

    def predict_openai(self, messages: Union[str, list[dict]]) -> (str, int, int):
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]

        generate_args = {
            "model": self.model_id,
            "messages": messages,
            "response_format": {"type": "text"},
            "temperature": self.temperature,
            "max_tokens": self.max_token_to_sample,
        }

        if self.temperature > 0:
            generate_args["top_p"] = self.top_p

        if self.model_id in (OAI.O4_MINI, OAI.O3):
            generate_args["temperature"] = 1
            del generate_args["max_tokens"]

        response = self.client.chat.completions.create(**generate_args)

        output = response.choices[0].message.content
        usage = getattr(response, "usage", {})
        input_tokens = getattr(usage, "prompt_tokens", 0)
        output_tokens = getattr(usage, "completion_tokens", 0)

        return output, input_tokens, output_tokens

    def predict_gemini(self, messages: Union[str, list[dict]]) -> (str, int, int):
        if isinstance(messages, str):
            prompt = messages
        elif isinstance(messages, list):
            prompt = "\n".join(
                msg["content"] for msg in messages if msg["role"] == "user"
            )
        else:
            raise ValueError("Invalid format for Gemini input.")

        model = self.client.GenerativeModel(self.model_id)
        response = model.generate_content(prompt)

        # Note: Gemini responses don't expose token usage currently
        output = getattr(response, "text", "")
        return output.strip(), 0, 0

    def predict_openrouter(self, messages: Union[str, list[dict]]) -> (str, int, int):
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]

        generate_args = {
            "model": self.model_id,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_token_to_sample,
            "extra_body": {},
        }

        if self.temperature > 0:
            generate_args["top_p"] = self.top_p

        response = self.client.chat.completions.create(**generate_args)
        choice = response.choices[0]

        # Prefer content if available, otherwise use reasoning (OpenRouter/Qwen specific)
        output = choice.message.content or choice.message.reasoning or ""

        usage = getattr(response, "usage", {})
        input_tokens = getattr(usage, "prompt_tokens", 0)
        output_tokens = getattr(usage, "completion_tokens", 0)

        return output.strip(), input_tokens, output_tokens

    def _predict_claude(
        self, messages: Union[str, list[dict]], thinking: bool = False
    ) -> (str, int, int):
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]

        generate_args = {
            "anthropic_version": "bedrock-2023-05-31",
            "messages": messages,
            "max_tokens": self.max_token_to_sample,
            "temperature": self.temperature,
        }

        if self.temperature > 0:
            generate_args["top_p"] = self.top_p

        if thinking:
            generate_args["thinking"] = {
                "type": "enabled",
                "budget_tokens": THINKING_MODE_TOKENS,
            }

        body = json.dumps(generate_args)
        response = self.bedrock.invoke_model(body=body, modelId=self.model_id)
        response_body = json.loads(response.get("body").read())

        input_tokens = response_body["usage"]["input_tokens"]
        output_tokens = response_body["usage"]["output_tokens"]

        return response_body["content"][0]["text"], input_tokens, output_tokens

    def predict_deepseek_r1(self, messages: Union[str, list[dict]]) -> (str, int, int):
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]

        # Format messages for DeepSeek prompt structure
        prompt = ""
        for msg in messages:
            role = msg.get("role")
            content = msg.get("content")
            if role == "user":
                prompt += f"<｜User｜>{content}"
            elif role == "assistant":
                prompt += f"<｜Assistant｜>{content}"

        formatted_prompt = f"<｜begin▁of▁sentence｜>{prompt}<｜Assistant｜><think>\n"

        generate_args = {
            "prompt": formatted_prompt,
            "max_tokens": self.max_token_to_sample,
            "temperature": self.temperature,
        }

        if self.temperature > 0:
            generate_args["top_p"] = self.top_p

        body = json.dumps(generate_args)

        response = self.bedrock.invoke_model(body=body, modelId=self.model_id)

        response_body = json.loads(response["body"].read())
        choice = response_body["choices"][0]
        output = choice["text"]
        input_tokens = response_body.get("usage", {}).get("input_tokens", 0)
        output_tokens = response_body.get("usage", {}).get("output_tokens", 0)

        return output, input_tokens, output_tokens

    def predict_v3(self, messages: Union[str, list[dict]]) -> (str, int, int):
        return self._predict_claude(messages, thinking=False)

    def predict_claude_3_7(self, messages: Union[str, list[dict]]) -> (str, int, int):
        return self._predict_claude(messages, thinking=False)

    def predict_claude_3_7_thinking(
        self, messages: Union[str, list[dict]]
    ) -> (str, int, int):
        return self._predict_claude(messages, thinking=True)

    def predict_llama(self, messages: Union[str, list[dict]]) -> (str, int, int):
        if isinstance(messages, str):
            prompt = messages
        elif len(messages) == 1:
            prompt = messages[0]["content"]
        elif isinstance(messages, list):
            prompt = ""
            for msg in messages:
                role = msg.get("role")
                content = msg.get("content")
                if role == "user":
                    prompt += f"[INST] {content} [/INST]\n"
                elif role == "assistant":
                    prompt += f"{content}\n"
            # prompt += "[INST]"  # Optional: to cue response
        else:
            raise ValueError("Invalid input format for messages.")
        generate_args = {
            "prompt": prompt,
            "max_gen_len": self.max_token_to_sample,
            "temperature": self.temperature,
        }

        if self.temperature > 0:
            generate_args["top_p"] = self.top_p

        body = json.dumps(generate_args)

        response = self.bedrock.invoke_model(
            body=body,
            modelId=self.model_id,
            accept=self.ACCEPT,
            contentType=self.CONTENT_TYPE,
        )
        response_body = json.loads(response["body"].read())

        output = response_body.get("generation", "")
        input_tokens = response_body.get("usage", {}).get("input_tokens", 0)
        output_tokens = response_body.get("usage", {}).get("output_tokens", 0)

        return output, input_tokens, output_tokens


if __name__ == "__main__":
    # model = LLM(model_id = LLAMA.V3_405, max_token_to_sample = 200, temperature=0)
    model = LLM(model_id=OAI.GPT_4O, max_token_to_sample=200, temperature=0)
    # Maintain conversation history
    messages = []

    # First user input
    prompt1 = "Introduce a city in the world."
    print("> " + prompt1)
    messages.append({"role": "user", "content": prompt1})
    response1, _, _ = model.predict(messages)
    print("Response: " + response1)

    # Add model's response to history
    messages.append({"role": "assistant", "content": response1})

    # Follow-up question
    prompt2 = "Which continent the city is located?"
    print("\n\n> " + prompt2)
    messages.append({"role": "user", "content": prompt2})
    response2, _, _ = model.predict(messages)
    print("Response: " + response2)

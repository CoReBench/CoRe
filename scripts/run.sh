#!/bin/bash

python run.py \
  --prompt_folder ../prompts \
  --result_folder ../response \
  --model claude3.5 \
  --max_tokens 2048 \
  --temperature 0 \
  --source \
  --lite ../lite.json

#!/bin/bash

python run.py \
  --prompt ../prompts \
  --result_folder ../response \
  --model ds-v3 \
  --max_tokens 2048 \
  --temperature 0 \
  --num_workers 10 \
  --source \
  --lite ../lite.json

#!/bin/bash

python run.py \
  --prompt_folder CoRe/prompts \          # <- update path
  --result_folder xxx \     # <- update path, your input
  --model claude3.5 \       # <- your input
  --max_tokens 2048 \
  --temperature 0 \
  --source \
  --lite CoRe/lite.json   # <- update path
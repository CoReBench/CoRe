#!/usr/bin/env bash

set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <response_root>"
  exit 1
fi

response_root="$1"

python eval.py \
  -f "${response_root}/response" \
  -l CoRe/raw_annotation \      # <-update 
  -o "${response_root}/eval" \
  -c "${response_root}/eval/results.csv"



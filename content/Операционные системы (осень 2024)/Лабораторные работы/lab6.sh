#!/bin/bash

for i in {1..3}; do
  echo "Имя пользователя: $USER"
done

i=0
while [ $i -le 100 ]; do
  if [ $((i % 2)) -eq 0 ]; then
    printf '%s ' "$i"
  fi
  i=$((i + 1))
done
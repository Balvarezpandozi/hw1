#!/bin/bash

for i in {01..10}
do
  python3 "input=tc$i.txt;output=output$i.txt"
  cat -t "./output$i.txt"
  cat -t "./tc$i.out"
  
  if cmp "./output$i.txt" "./tc$i.out"; then
    echo "Test case $i passed"
  else
    echo "Test case $i failed"
  fi
  echo "_____________________________"
done
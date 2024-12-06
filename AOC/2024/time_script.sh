#!/bin/bash

# Loop through the directories day01 to day05
for i in {1..5}
do
  # Format directory name (e.g., day01, day02, ...)
  dir="day$(printf "%02d" $i)"
  # Enter the directory
  cd $dir
  echo "Running scripts in $dir..."
  # Measure time for part1.py
  echo "Executing part1.py:"
  time python3 part1.py

  # Measure time for part2.py
  echo "Executing part2.py:"
  time python3 part2.py

  # Go back to the parent directory
  cd ..

  echo "-------------------------"
done

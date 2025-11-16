#!/bin/bash
echo "Running Week 8 Data Poisoning Experiments..."

# Define the data path
DATA_PATH="data/iris.csv"

# Check if data file exists
if [ ! -f "$DATA_PATH" ]; then
    echo "Error: $DATA_PATH not found."
    echo "Please download the Iris dataset and save it as data/iris.csv"
    exit 1
fi

# Define the poison rates to test
RATES=(0.0 0.05 0.10 0.50)

# Loop and run training for each rate
for rate in "${RATES[@]}"
do
  echo ""
  echo "============================================="
  echo "Running training with poison rate: $rate"
  echo "============================================="
  python train.py --data $DATA_PATH --poison_rate $rate
done

echo ""
echo "All experiments complete."
echo "To view the results, run: mlflow ui"
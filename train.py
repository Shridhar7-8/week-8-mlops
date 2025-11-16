import argparse
import os
import pandas as pd
import numpy as np
import joblib
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

def poison_data(df, poison_rate):
    """
    Poisons the dataset by flipping labels at the specified rate.
    """
    if poison_rate == 0.0:
        print("No poisoning applied.")
        return df

    # Get the unique labels (0, 1, 2)
    labels = df['species'].unique()
    n_poison = int(len(df) * poison_rate)
    
    # Get random indices to poison
    poison_indices = df.sample(n=n_poison, random_state=42).index
    
    poisoned_count = 0
    for idx in poison_indices:
        current_label = df.loc[idx, 'species']
        
        # Choose a new label that is different from the current one
        new_label = np.random.choice([l for l in labels if l != current_label])
        df.loc[idx, 'species'] = new_label
        poisoned_count += 1
        
    print(f"✅ Poisoned {poisoned_count} rows ({poison_rate*100}%) with label flipping.")
    return df

def run_training(data_path, max_depth, poison_rate):
    """Loads data, poisons it, trains a model, and logs to MLflow."""
    
    print(f"--- Starting run: poison_rate={poison_rate}, max_depth={max_depth} ---")
    
    # Start an MLflow run
    with mlflow.start_run():
        
        # Log parameters
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("poison_rate", poison_rate)
        
        # --- 1. Load Data ---
        try:
            df = pd.read_csv(data_path)
        except FileNotFoundError:
            print(f"Error: Data file not found at {data_path}")
            return
            
        # --- 2. Poison Data ---
        df = poison_data(df, poison_rate)

        # --- 3. Split Data ---
        X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
        y = df['species']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.4, stratify=y, random_state=42
        )

        # --- 4. Train Model ---
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)

        # --- 5. Evaluate and Log ---
        prediction = model.predict(X_test)
        accuracy = metrics.accuracy_score(prediction, y_test)
        
        print(f"Model training complete. Accuracy: {accuracy:.4f}")
        mlflow.log_metric("accuracy", accuracy)

        # --- 6. Log Model ---
        mlflow.sklearn.log_model(model, "model")
        print(f"Model logged to MLflow.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data", 
        required=True, 
        help="Path to the training data CSV file."
    )
    parser.add_argument(
        "--depth", 
        type=int, 
        default=3, 
        help="Max depth for the Decision Tree."
    )
    parser.add_argument(
        "--poison_rate", 
        type=float, 
        default=0.0, 
        help="Fraction of data to poison (e.g., 0.05 for 5%)."
    )
    args = parser.parse_args()
    
    # Set experiment name
    mlflow.set_experiment("Week 8 - Iris Poisoning")
    
    run_training(args.data, args.depth, args.poison_rate)
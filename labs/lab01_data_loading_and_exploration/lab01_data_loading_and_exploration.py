"""Lab 01 – Data Loading and Exploration

Load and explore an engineering time-series dataset.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TODO: update this path once your dataset is downloaded
csv_path = "path/to/your/data.csv"

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print("Please download the dataset and update 'csv_path'.")
    df = None

if df is not None:
    print("Head:")
    print(df.head())
    print("\nInfo:")
    print(df.info())
    print("\nDescribe:")
    print(df.describe())

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        df[col].plot(title=f"Time series of {col}")
        plt.xlabel("Index")
        plt.ylabel(col)
        plt.show()
    else:
        print("No numeric columns found to plot.")


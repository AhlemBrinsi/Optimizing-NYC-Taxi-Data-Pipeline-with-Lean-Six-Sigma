import os
import pandas as pd

def load_data(df, filename):
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")
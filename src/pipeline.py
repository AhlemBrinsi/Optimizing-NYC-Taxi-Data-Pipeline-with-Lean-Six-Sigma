import time
from transform_before import transform_before
from load import load_data

def run_pipeline_before():
    start = time.time()

    df = transform_before()
    load_data(df, "data/processed/before.csv")

    end = time.time()

    print("⏱️ Execution time BEFORE:", end - start)

if __name__ == "__main__":
    run_pipeline_before()


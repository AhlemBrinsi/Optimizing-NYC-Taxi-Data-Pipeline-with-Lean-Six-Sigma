import time
from transform_after import transform_after
from load import load_data

def run_pipeline_after():
    start = time.time()

    df = transform_after()
    load_data(df, "data/processed/after.csv")

    end = time.time()
    print("⏱️ Execution time AFTER:", end - start)

if __name__ == "__main__":
    run_pipeline_after()
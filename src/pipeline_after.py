import time
from transform_after import transform_after
from load import load_data

RAW_PATH = "data/raw/yellow_tripdata_2016-01.csv"

def run_pipeline_after():
    start = time.time()

    df = transform_after(RAW_PATH)

    load_data(df, "data/processed/yellow_tripdata_2016_after.csv")

    end = time.time()
    print("⏱️ Execution time AFTER:", end - start)

if __name__ == "__main__":
    run_pipeline_after()
import time
from transform_before import transform_before
from load import load_data

RAW_PATH = "data/raw/yellow_tripdata_2016-01.csv"

def run_pipeline_before():
    start = time.time()

    df = transform_before(RAW_PATH) 
    load_data(df, "data/processed/yellow_tripdata_2016_before.csv")

    end = time.time()

    print("⏱️ Execution time BEFORE:", end - start)

if __name__ == "__main__":
    run_pipeline_before()
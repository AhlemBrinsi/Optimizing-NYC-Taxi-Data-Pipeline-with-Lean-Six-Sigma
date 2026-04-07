import pandas as pd

def transform_before(path):
    df = pd.read_csv(path)

    # Convert pickup datetime
    df['pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])

    # Compute trip_duration if missing
    if 'trip_duration' not in df.columns:
        df['trip_duration'] = (pd.to_datetime(df['lpep_dropoff_datetime']) - df['pickup_datetime']).dt.total_seconds()
    
    df['trip_minutes'] = df['trip_duration'] / 60
    df['hour'] = df['pickup_datetime'].dt.hour

    return df
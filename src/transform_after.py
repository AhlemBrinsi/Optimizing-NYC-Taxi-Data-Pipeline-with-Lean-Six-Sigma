import pandas as pd

def transform_after(path):

    df = pd.read_csv(
        path,
        dtype={'store_and_fwd_flag': 'category'},  # 👈 memory optimization
        low_memory=False
    )

    # Parse datetime once
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # Vectorized filtering (faster)
    df = df.query("trip_distance > 0 and fare_amount > 0")

    # Trip duration
    df['trip_duration'] = (
        df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
    ).dt.total_seconds() / 60

    df = df[df['trip_duration'] > 0]

    # Feature engineering (vectorized)
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_day'] = df['tpep_pickup_datetime'].dt.day
    df['pickup_month'] = df['tpep_pickup_datetime'].dt.month
    df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.dayofweek

    df['trip_speed'] = df['trip_distance'] / df['trip_duration']

    cols_to_keep = [
        'VendorID','tpep_pickup_datetime','tpep_dropoff_datetime',
        'Passenger_count','trip_distance','RateCodeID',
        'store_and_fwd_flag','Payment_type','fare_amount',
        'extra','mta_tax','improvement_surcharge','tip_amount',
        'tolls_amount','total_amount','trip_duration',
        'pickup_hour','pickup_day','pickup_month',
        'pickup_weekday','trip_speed'
    ]

    return df[[c for c in cols_to_keep if c in df.columns]]
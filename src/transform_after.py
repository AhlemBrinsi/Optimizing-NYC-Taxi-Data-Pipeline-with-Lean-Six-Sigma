import pandas as pd

def transform_after(path):
    df = pd.read_csv(
        path,
        dtype={'store_and_fwd_flag': str},
        parse_dates=['lpep_pickup_datetime','lpep_dropoff_datetime'],
        low_memory=False
    )

    # Clean data
    df = df[(df['trip_distance'] > 0) & (df['fare_amount'] > 0)]
    df['trip_duration'] = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']).dt.total_seconds() / 60
    df = df[df['trip_duration'] > 0]

    # Features
    df['pickup_hour'] = df['lpep_pickup_datetime'].dt.hour
    df['pickup_day'] = df['lpep_pickup_datetime'].dt.day
    df['pickup_month'] = df['lpep_pickup_datetime'].dt.month
    df['pickup_weekday'] = df['lpep_pickup_datetime'].dt.dayofweek
    df['trip_speed'] = df['trip_distance'] / df['trip_duration']

    # Keep useful columns
    df = df[['lpep_pickup_datetime','lpep_dropoff_datetime','trip_duration','trip_distance','fare_amount','tip_amount','total_amount',
             'pickup_hour','pickup_day','pickup_month','pickup_weekday','PULocationID','DOLocationID','passenger_count']]

    return df
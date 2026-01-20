#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import click

@click.command()
@click.option('--user', default='root', help='PostgreSQL user')
@click.option('--password', default='root', help='PostgreSQL password')
@click.option('--host', default='localhost', help='PostgreSQL host')
@click.option('--port', default=5432, type=int, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='green_taxi_data', help='Target table name')
def ingest_data(user, password, host, port, db, table):
    click.echo(type(port))

    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]

    file2 = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"


    from sqlalchemy import create_engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    # print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


    # In[ ]:


    from tqdm.auto import tqdm

    df_zones = pd.read_csv(file2)

    df_iter = pd.read_parquet(
        'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet',
        # iterator=True,
        # chunksize=100000
    )
    print("read")
    df_iter.to_sql(
        name=table,
        con=engine,
        if_exists="replace"
    )

    # first = True

    # for df_chunk in tqdm(df_iter):

    #     if first:
    #         # Create table schema (no data)
    #         df_chunk.head(0).to_sql(
    #             name=table,
    #             con=engine,
    #             if_exists="replace"
    #         )
    #         first = False
    #         print("Table created")

    #     # Insert chunk
    #     df_chunk.to_sql(
    #         name=table,
    #         con=engine,
    #         if_exists="append"
    #     )

    #     print("Inserted:", len(df_chunk))

    df_zones.to_sql(name="zones", con=engine, if_exists="replace")


# In[ ]:

if __name__ == "__main__":
    ingest_data()



```
CREATE EXTERNAL TABLE `future-snowfall-484415-m5.demo_dataset.external_1h_2024_yellow`
  OPTIONS (
    format ="parquet",
    uris = [
        'gs://2024-taxi-data/yellow_tripdata_2024-01.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-02.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-03.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-04.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-05.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-06.parquet']
    );
```

```
LOAD DATA INTO `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow`
FROM FILES(
    format = 'PARQUET',
    uris = [
        'gs://2024-taxi-data/yellow_tripdata_2024-01.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-02.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-03.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-04.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-05.parquet', 
        'gs://2024-taxi-data/yellow_tripdata_2024-06.parquet']
);
```

# Question 1
```
SELECT COUNT(*) FROM `future-snowfall-484415-m5.demo_dataset.external_1h_2024_yellow`;
```

20332093

# Question 2

```
SELECT COUNT(DISTINCT PULocationID) FROM `future-snowfall-484415-m5.demo_dataset.external_1h_2024_yellow`;
```
Estimated bytes processed: 0MB

```
SELECT COUNT(DISTINCT PULocationID) FROM `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow`;
```
Estimated bytes processed: 155.12 MB

# Question 3

```
SELECT PULocationID FROM `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow`;
```

```
SELECT PULocationID, DOLocationID FROM `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow`;
```

BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

# Question 4

```
SELECT COUNT(PULocationID) FROM `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow` WHERE fare_amount = 0;
```

8333

# Question 5

Partition by tpep_dropoff_datetime and Cluster on VendorID

```
CREATE OR REPLACE TABLE
  `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow_partitioned_clustered` (
    VendorID INTEGER,
    tpep_pickup_datetime TIMESTAMP,
    tpep_dropoff_datetime TIMESTAMP,
    passenger_count INTEGER,
    trip_distance FLOAT64,
    RatecodeID INTEGER,
    store_and_fwd_flag STRING,
    PULocationID INTEGER,
    DOLocationID INTEGER,
    payment_type INTEGER,
    fare_amount FLOAT64,
    extra FLOAT64,
    mta_tax FLOAT64,
    tip_amount FLOAT64,
    tolls_amount FLOAT64,
    improvement_surcharge FLOAT64,
    total_amount FLOAT64,
    congestion_surcharge FLOAT64,
    Airport_fee FLOAT64
  )
PARTITION BY
  TIMESTAMP_TRUNC(tpep_dropoff_datetime, DAY)
CLUSTER BY
  VendorID
AS
SELECT
  *
FROM
  `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow`;
```

# Question 6
```
SELECT DISTINCT VendorID FROM `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow` WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```

310.24 MB

```
SELECT DISTINCT VendorID FROM `future-snowfall-484415-m5.demo_dataset.internal_1h_2024_yellow_partitioned_clustered` WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```
26.84 MB

# Question 7
GCP Bucket

# Question 8
False

# Question 9
0B because the number of rows is already stored a BigQuery metadata so no scan is required.
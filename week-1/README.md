# Question 1
```
docker run -it --entrypoint "bash" python:3.13
```

Then in the container:
```
pip --version
```

The output is 

# Question 2
postgres:5433

# Question 3

```
docker build -t taxi_ingest .
docker-compose up
docker run --rm --network homework_default taxi_ingest --host pgdatabase
```

```
SELECT COUNT(*) FROM green_taxi_data WHERE lpep_pickup_datetime >= '2025-11-01' AND lpep_pickup_datetime < '2025-12-01' AND trip_distance <= 1;
```

8007

# Question 4

```
SELECT lpep_pickup_datetime FROM green_taxi_data WHERE trip_distance = (SELECT MAX(trip_distance) FROM green_taxi_data WHERE trip_distance < 100);
```

2025-11-14 15:36:27

# Question 5
```
SELECT z."Zone", SUM(total_amount) AS t FROM zones as z INNER JOIN green_taxi_data as g ON z."LocationID" = g."PULocationID" WHERE to_char(lpep_pickup_datetime, 'YYYY-MM') = '2025-11' GROUP BY z."Zone" ORDER BY t DESC;
```

East Harlem North

# Question 6
```
SELECT z."Zone" FROM green_taxi_data as g INNER JOIN zones as z ON g."DOLocationID" = z."LocationID" WHERE tip_amount = 
(SELECT MAX(tip_amount) FROM green_taxi_data as g INNER JOIN zones as z ON g."PULocationID" = z."LocationID" WHERE z."Zone" = 'East Harlem North');
```

Yorkville West

# Question 7
terraform init, terraform apply -auto-approve, terraform destroy
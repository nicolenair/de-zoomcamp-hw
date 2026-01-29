# Question 1
134.5 MB

# Question 2
green_tripdata_2020-04.csv

# Question 3
```
SELECT COUNT(*) FROM (SELECT * FROM `demo_dataset.yellow_tripdata_2020_01` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_02`
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_03`
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_04` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_05` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_06` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_07` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_08` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_09` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_10` 
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_11`
UNION ALL SELECT * FROM `demo_dataset.yellow_tripdata_2020_12`);
```

24648499

# Question 4
```
SELECT COUNT(*) FROM (SELECT * FROM `demo_dataset.green_tripdata_2020_01` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_02`
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_03`
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_04` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_05` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_06` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_07` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_08` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_09` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_10` 
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_11`
UNION ALL SELECT * FROM `demo_dataset.green_tripdata_2020_12`);
```

1734051

# Question 5
```
SELECT COUNT(*) FROM yellow_tripdata_2021-03 
```

1925152

# Question 6
Add a timezone property set to America/New_York in the Schedule trigger configuration
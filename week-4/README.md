# Question 1

int_trips_unioned only

# Question 2

dbt will fail the test, returning a non-zero exit code

# Question 3

```
select count(*) from taxi_rides_ny.prod.fct_monthly_zone_revenue;
```

12184

# Question 4


```
with max_revenue as 
(select max(revenue_monthly_total_amount) from taxi_rides_ny.prod.fct_monthly_zone_revenue 
where service_type = 'Green' and extract('year' FROM revenue_month
)='2020')

select pickup_zone from taxi_rides_ny.prod.fct_monthly_zone_revenue 
where revenue_monthly_total_amount = (select * from max_revenue limit 1)
and service_type = 'Green'
and extract('year' FROM revenue_month)='2020';
```

East Harlem North

# Question 5

```
select sum(total_monthly_trips) from taxi_rides_ny.prod.fct_monthly_zone_revenue where service_type='Green' and revenue_month = '2019-10-01';
```

384624

# Question 6

1. modified the original ingestion script to create fhv ingestion script in `ingest_fhv.py`
2. added stg_fhv_tripdata model.

```
select count(*) from taxi_rides_ny.prod.stg_fhv_tripdata;
```

43244693
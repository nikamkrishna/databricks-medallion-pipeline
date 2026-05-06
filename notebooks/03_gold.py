

from pyspark.sql.functions import sum, avg, hour ,when ,col
df_silver = spark.read.format("delta") \
    .load("/Volumes/workspace/default/project_vol/silver/taxi_data")
     

# Daily revenue
daily_revenue = df_silver.groupBy("pickup_date") \
    .agg(sum("total_amount").alias("total_revenue"))

# Trips per hour
df = df_silver.withColumn(
    "pickup_hour",
    hour("tpep_pickup_datetime")
)

trips_per_hour = df.groupBy("pickup_hour").count()
     

# Efficiency
efficiency = df_silver.withColumn(
    "fare_per_km",
    when(col("trip_distance") > 0,
         col("fare_amount") / col("trip_distance"))
).groupBy("pickup_date").agg(
    avg("fare_per_km").alias("avg_fare_per_km")
)

     

# Writes
base_path = "/Volumes/workspace/default/project_vol/gold"

# daily_revenue.write.format("delta").mode("overwrite") \
#     .save(f"{base_path}/daily_revenue")

# trips_per_hour.write.format("delta").mode("overwrite") \
#     .save(f"{base_path}/trips_per_hour")

efficiency.write.format("delta") \
    .mode("overwrite") \
    .save(f"{base_path}/fare_efficiency")
     


     

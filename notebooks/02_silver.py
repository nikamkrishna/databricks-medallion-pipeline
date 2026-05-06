

from pyspark.sql.functions import col,to_date
     

df_bronze = spark.read.format("delta") \
    .load("/Volumes/workspace/default/project_vol/bronze/taxi_data")
     

# display(df.filter(
#     (col("trip_distance") <= 0)))
     

# display(df)
     

clean_df = df_bronze.filter(

    ~(
        (col("trip_distance") == 0) &
        (col("fare_amount") == 0) &
        (col("passenger_count") == 0)
    )
)
     

df1 = clean_df.sample(0.01)
     

clean_df1 = df1.withColumn(
    "pickup_date",
    to_date(col("tpep_pickup_datetime"))
)
     

clean_df1.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("pickup_date") \
    .save("/Volumes/workspace/default/project_vol/silver/taxi_data")
     


     

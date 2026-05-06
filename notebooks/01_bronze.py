

df = spark.table("workspace.default.yellow_tripdata_2026_01")
     

df.write.format("delta") \
  .mode("overwrite") \
  .save("/Volumes/workspace/default/project_vol/bronze/taxi_data")
     


     

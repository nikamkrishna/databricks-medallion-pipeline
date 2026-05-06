

from pyspark.sql.functions import col, to_date
from delta.tables import DeltaTable
df_new = spark.table("workspace.default.yellow_tripdata_2026_02")
     

df_new_clean = df_new.withColumn(
    "pickup_date",
    to_date(col("tpep_pickup_datetime"))
)

     


delta_table = DeltaTable.forPath(
    spark,
    "/Volumes/workspace/default/project_vol/silver/taxi_data"
)
     

delta_table.alias("target").merge(
    df_new_clean.alias("source"),
    """
    target.tpep_pickup_datetime = source.tpep_pickup_datetime
    AND target.VendorID = source.VendorID
    """
).whenNotMatchedInsertAll().execute()
     
DataFrame[num_affected_rows: bigint, num_updated_rows: bigint, num_deleted_rows: bigint, num_inserted_rows: bigint]


     

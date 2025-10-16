import dlt
from pyspark.sql.functions import from_json, col, struct
from pyspark.sql.types import MapType, StringType


@dlt.table(
    name="telematics",
    comment="Parsed Kinesis data as map with metadata struct",
    table_properties={"quality": "bronze"}
)
def bronze_table():
    raw_stream = spark.readStream.table("smart_claims_dev.external_data_telematics.telematics")

    return raw_stream.select(
            col("chassis_no"),
            col("latitude"),
            col("longitude"),
            col("event_timestamp"),
            col("speed")
        )
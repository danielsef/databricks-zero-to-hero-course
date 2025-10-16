import dlt
from pyspark.sql.functions import from_json, col, struct
from pyspark.sql.types import MapType, StringType


@dlt.table(
    name="customer",
    comment="Ingest customers object",
    table_properties={"quality": "bronze"}
)
def bronze_table_customer():
    raw_stream = spark.readStream.table("smart_claims_dev.external_data_db.customers")
    return raw_stream

@dlt.table(
    name="claim",
    comment="Ingest claims object",
    table_properties={"quality": "bronze"}
)
def bronze_table_claim():
    raw_stream = spark.readStream.table("smart_claims_dev.external_data_db.claims")
    return raw_stream

@dlt.table(
    name="policy",
    comment="Ingest policies object",
    table_properties={"quality": "bronze"}
)
def bronze_table_policy():
    raw_stream = spark.readStream.table("smart_claims_dev.external_data_db.policies")
    return raw_stream
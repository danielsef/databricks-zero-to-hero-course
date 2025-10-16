import dlt

@dlt.table(
    name="smart_claims_dev.01_bronze.training_images",
    comment="Raw accident training image ingested from ADFS", 
    table_properties={"quality": "bronze"}
)
def raw_images():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "BINARYFILE")
        .load(f"/Volumes/smart_claims_dev/00_landing/training_imgs"))

@dlt.table(
    name="smart_claims_dev.01_bronze.claim_images_meta",
    comment="Raw accident claim images metadata ingested from ADFS", 
    table_properties={"quality": "bronze"}
)
def raw_images_meta():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .load(f"/Volumes/smart_claims_dev/00_landing/claims/metadata"))
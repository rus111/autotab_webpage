
from google.cloud import storage


def get_gcloud_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()
    print(storage_client)

    bucket = storage_client.bucket(bucket_name)
    print(bucket)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    print(blob)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )

# @st.cache(suppress_st_warning=True)
def upload_gcloud_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"
    
    storage_client = storage.Client()
    print(storage_client)

    bucket = storage_client.bucket(bucket_name)
    # sys.stdout.write(bucket)
    print("bucket", bucket)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    print("blob"+ str(blob)+"\n")
    file_exists = storage.Blob(bucket=bucket, name=destination_file_name).exists(storage_client)
    if not file_exists:
        blob.upload_from_filename(destination_file_name)
        print(
            "Uploaded storage object {} from local file {} to bucket {}.".format(
                destination_file_name, source_blob_name, bucket_name
            )
        )
        print(f'uploaded {destination_file_name}')
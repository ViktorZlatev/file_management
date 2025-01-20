import os
from minio import Minio


os.environ.setdefault('MINIO_ENDPOINT', 'minio:9000')  
os.environ.setdefault('MINIO_ACCESS_KEY', 'minioadmin')
os.environ.setdefault('MINIO_SECRET_KEY', 'minioadmin')
os.environ.setdefault('MINIO_BUCKET', 'files')

minio_client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False  
)

bucket_name = os.getenv("MINIO_BUCKET")


if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)

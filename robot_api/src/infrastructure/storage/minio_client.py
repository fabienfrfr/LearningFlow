from minio import Minio

class MinioClientWrapper:
    def __init__(self, endpoint: str, access_key: str, secret_key: str):
        self.client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=False)

    def upload_file(self, bucket_name: str, file_path: str, object_name: str):
        self.client.fput_object(bucket_name, object_name, file_path)


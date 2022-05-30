import sys
from google.cloud import storage
import glob
from pathlib import Path

class GcsInterfase:
   def __init__(self, project_id :str, bucket_name: str) -> None:
       self.storage_client = storage.Client(project= project_id)
       self.bucket = self.storage_client.bucket(bucket_name)
   
   def upload(self, blob_name: str, contents: str):
       blob = self.bucket.blob(blob_name)
       try:
           blob.upload_from_string(contents, content_type="application/json")
           print(f"{blob_name}をアップロードしました")
       except Exception as e:
           raise ConnectionError(f"GcsInterFace::サーバーへの保存に失敗しました{e}")

def main():
  gcsInterfase = GcsInterfase("contents-mikiri-net", "contents.mikiri.net")

  p = Path("./public/")

  file_list = p.glob("*.*")
  print(file_list)
  for file_one in file_list:
    with open(file=file_one, mode="r") as f:
      gcsInterfase.upload(file_one, f.read())

if __name__ == "__main__":
    main()
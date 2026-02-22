"""
Upload split JSON files to AWS S3
"""

import boto3
import os
from tqdm import tqdm

def upload_to_s3(local_folder, bucket_name, s3_folder):
    """
    Upload files from local folder to S3
    Args:
        local_folder: C:\Users\Rucha Joshi\Desktop\DataEngg\yelp\split_data
        bucket_name: yelp-etl-210226
        s3_folder: yelp_etl
    """
    
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # Get list of files to upload
    files = [f for f in os.listdir(local_folder) if f.endswith('.json')]
    
    print(f"Found {len(files)} files to upload")
    print(f"Uploading to s3://{bucket_name}/{s3_folder}\n")
    
    # Upload each file
    for filename in tqdm(files, desc="Uploading"):
        local_path = os.path.join(local_folder, filename)
        s3_key = f"{s3_folder}/{filename}"
        
        try:
            s3_client.upload_file(local_path, bucket_name, s3_key)
            # print(f"✅ Uploaded: {filename}")
        except Exception as e:
            print(f"❌ Error uploading {filename}: {e}")
    
    print(f"\n🎉 Upload complete! {len(files)} files uploaded to S3")

if __name__ == "__main__":
    # Configuration (DO NOT commit real values to GitHub!)
    LOCAL_FOLDER = "data/split_files"
    BUCKET_NAME = "your-bucket-name"  # Replace with your bucket
    S3_FOLDER = "yelp-data"
    
    upload_to_s3(LOCAL_FOLDER, BUCKET_NAME, S3_FOLDER)
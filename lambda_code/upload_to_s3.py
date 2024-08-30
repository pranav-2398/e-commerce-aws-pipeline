import boto3

s3 = boto3.client("s3")

def upload_to_s3(filename, current_date, bucket_name):
    """Uploads a CSV file to S3 with Hive-style partitioning"""
    # Extract year, month, day from current_date
    year = current_date.year
    month = current_date.month
    day = current_date.day
    file_path = f"transactions/year={year}/month={month}/day={day}/{filename}"  # Hive-style partitioning
    s3.upload_file(f'/tmp/{filename}', bucket_name, file_path)
    logger.info(f"File uploaded to S3 Bucket {bucket_name}/{file_path}")
    return
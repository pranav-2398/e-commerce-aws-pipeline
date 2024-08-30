import json
from generate_mock_data import generate_data
from datetime import date, datetime, timedelta
from upload_to_s3 import upload_to_s3
import os
import logging

logger = logging.getLogger()
logger.setLevel("INFO")

# Define date range (modify as needed)
start_date = datetime.strptime(os.environ["StartDate"], "%Y-%m-%d").date()
end_date = datetime.strptime(os.environ["EndDate"], "%Y-%m-%d").date()
bucket_name = os.environ["BucketName"]

def lambda_handler(event, context):
    for current_date in range((end_date - start_date).days + 1):
        # Generate Date
        current_date = start_date + timedelta(days=current_date)
        date_str = str(current_date)
        generate_data(current_date, date_str)
        upload_to_s3(f"transactions_{date_str}.csv", current_date, bucket_name)

    return {
        'statusCode': 200,
        'body': json.dumps(f'Ecommerce Data Generated.')
    }
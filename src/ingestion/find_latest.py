import boto3
import re


def get_previous_update_dt(table_name):
    """Connects to s3 bucket using boto resource
    searches the bucket for keys with table name
    pushes the date from the key to a previous updates list
    sorts the previous updates list
    returns the most recent date

    the sort functionality may need some work as at the moment it just sorts strings which is not reliable
    """
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("marble-test-bucket")
    previous_updates = []
    for obj in bucket.objects.all():
        if f"{table_name}" in obj.key:
            date = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}", obj.key)
            previous_updates.append(date.group())

    if len(previous_updates) > 0:
        previous_updates.sort(reverse=True)
        return previous_updates[0]

import boto3
from botocore.exceptions import ClientError
session = boto3.Session(profile_name='JavierAWS')
client = session.client('rekognition')
response = client.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': "rekofacesnf",
                    'Name': "eagle.jpg",
                }
            },
            MaxLabels=10
        )
labels = {label["Name"]:{"N": str(label["Confidence"])} 
          for label in response["Labels"]}

print(labels)

client = session.client('dynamodb')
try:
    client.put_item(TableName= "reco2023",
                        Item={'images': {'S': "eagle.jpg"},
                              'Labels': {'M': labels}
                              })
except ClientError:
    print("error")

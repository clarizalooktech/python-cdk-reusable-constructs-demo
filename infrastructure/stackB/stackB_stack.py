from aws_cdk import core as cdk
from cdk_constructs.s3.s3_bucket import ReusableS3Bucket

class StackBStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        another_reusable_bucket = ReusableS3Bucket(self, 
            "StackB-Bucket", 
            bucket_name="stackb-bucket", 
            versioned=False
        )
        
        # Access the bucket using another_reusable_bucket.bucket

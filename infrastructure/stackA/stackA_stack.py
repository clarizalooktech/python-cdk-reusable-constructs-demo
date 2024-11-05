from aws_cdk import core as cdk
from cdk_constructs.s3.s3_bucket import ReusableS3Bucket

class StackAStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        reusable_bucket = ReusableS3Bucket(self, 
            "Stack-A-Bucket", 
            bucket_name="stacka-bucket", 
            versioned=True
        )
        
        # You can access the bucket using reusable_bucket.bucket

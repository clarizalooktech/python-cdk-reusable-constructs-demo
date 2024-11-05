from aws_cdk import aws_s3 as s3
from aws_cdk import core as cdk

class ReusableS3Bucket(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id: str, bucket_name: str = None, versioned: bool = False, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        self.bucket = s3.Bucket(
            self, 
            "Bucket",
            bucket_name=bucket_name,
            versioned=versioned
        )

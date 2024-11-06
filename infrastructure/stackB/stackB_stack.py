from aws_cdk import Stack, Duration, aws_s3 as s3
from constructs import Construct
from cdk_constructs.s3 import CustomS3Bucket

class StackB(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.logs_bucket = CustomS3Bucket(
            self, "StackBBucket",
            bucket_name="stack-b-logs-bucket",
            encryption=True,
            versioned=False,
            lifecycle_rules=[
                s3.LifecycleRule(
                    expiration=Duration.days(90)
                )
            ]
        )
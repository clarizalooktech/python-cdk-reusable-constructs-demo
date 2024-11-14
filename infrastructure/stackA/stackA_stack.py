from aws_cdk import Stack, Duration, aws_s3 as s3
from constructs import Construct
from cdk_constructs.s3.s3_bucket import CustomS3Bucket

class StackA(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.storage_bucket = CustomS3Bucket(
            self, "StackABucket",
            bucket_name="stack-a-storage-bucket",
            encryption=False,
            versioned=True,
            lifecycle_rules=[
                s3.LifecycleRule(
                    transitions=[
                        s3.Transition(
                            storage_class=s3.StorageClass.INTELLIGENT_TIERING,
                            transition_after=Duration.days(90)
                        )
                    ]
                )
            ]
        )
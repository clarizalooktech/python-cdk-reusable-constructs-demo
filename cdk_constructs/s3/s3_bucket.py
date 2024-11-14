from aws_cdk import (
    aws_s3 as s3,
    aws_kms as kms,
    RemovalPolicy,
    Stack,
    CfnOutput,
    Duration
)
from constructs import Construct

class CustomS3Bucket(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        # Get optional configuration parameters
        bucket_name = kwargs.get('bucket_name', None)
        encryption = kwargs.get('encryption', False)  
        versioned = kwargs.get('versioned', True)
        public_access = kwargs.get('public_access', False)
        lifecycle_rules = kwargs.get('lifecycle_rules', [])

        # Create KMS key if encryption is enabled
        if encryption:
            self.kms_key = kms.Key(
                self, f"{id}-key",
                removal_policy=RemovalPolicy.DESTROY,
                enable_key_rotation=True,
                description=f"KMS key for {id} bucket"
            )
        
        # Create the S3 bucket with encryption only if needed
        encryption_type = s3.BucketEncryption.KMS if encryption else None
        self.bucket = s3.Bucket(
            self, f"{id}-bucket",
            bucket_name=bucket_name,
            encryption=encryption_type,
            encryption_key=self.kms_key if encryption else None,
            versioned=versioned,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL if not public_access else None,
            removal_policy=RemovalPolicy.RETAIN,
            lifecycle_rules=lifecycle_rules
        )

        # Create output for bucket ARN
        CfnOutput(
            self, f"{id}-bucket-arn",
            value=self.bucket.bucket_arn,
            description=f"ARN of the {id} bucket"
        )

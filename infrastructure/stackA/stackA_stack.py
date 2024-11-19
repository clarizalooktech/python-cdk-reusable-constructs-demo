from aws_cdk import Stack, Duration, aws_s3 as s3
from constructs import Construct
from cdk_constructs.s3.s3_bucket import CustomS3Bucket
from cdk_constructs.sns.sns_topic import SnsTopic, SnsTopicProps

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

        notification_props = SnsTopicProps(
            topic_name="stack-a-notifications",
            email_subscriptions=["myemail@example.com"],
            retention_days=14,
            tags={
                "Environment": "Development",
                "Team": "TeamA",
                "CostCenter": "123456678"
            }
        )

        self.notification_topic = SnsTopic(
            self,
            "NotificationTopic",
            props=notification_props
        )
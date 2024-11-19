from aws_cdk import Stack, Duration, aws_s3 as s3
from constructs import Construct
from cdk_constructs.s3.s3_bucket import CustomS3Bucket
from cdk_constructs.sns.sns_topic import SnsTopic, SnsTopicProps

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

        # Create SNS Topic without any subscribers
        alert_topic_props = SnsTopicProps(
            topic_name="stack-b-alerts",
            tags={
                "Environment": "Development",
                "Team": "TeamB",
                "Project": "Alerts"
            }
        )

        self.alert_topic = SnsTopic(
            self,
            "AlertTopic",
            props=alert_topic_props
        )
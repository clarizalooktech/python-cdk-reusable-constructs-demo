from typing import List, Optional
from aws_cdk import (
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_kms as kms,
    aws_lambda as lambda_,
    Duration,
    CfnOutput,
    Tags,
)
from constructs import Construct
from dataclasses import dataclass, field

@dataclass
class SnsTopicProps:
    topic_name: str
    display_name: Optional[str] = None
    email_subscriptions: Optional[List[str]] = None
    lambda_subscriptions: Optional[List[str]] = None
    kms_key_id: Optional[str] = None
    retention_days: Optional[int] = None
    tags: Optional[dict] = field(default_factory=dict)

class SnsTopic(Construct):
    def __init__(
        self,
        scope: Construct,
        id_: str,
        *,
        props: SnsTopicProps
    ) -> None:
        super().__init__(scope, id_)

        # Prepare topic configuration
        topic_kwargs = {
            "topic_name": props.topic_name
        }

        # Add display name if provided
        if props.display_name:
            topic_kwargs["display_name"] = props.display_name

        # Configure KMS encryption if key is provided
        if props.kms_key_id:
            encryption_key = kms.Key.from_key_arn(
                self, 
                "TopicEncryptionKey",
                key_arn=props.kms_key_id
            )
            topic_kwargs["master_key"] = encryption_key

        # Create SNS Topic
        self.topic = sns.Topic(
            self,
            "Topic",
            **topic_kwargs
        )

        # Add email subscriptions
        if props.email_subscriptions:
            for email in props.email_subscriptions:
                self.topic.add_subscription(
                    subs.EmailSubscription(email)
                )

        # Add Lambda subscriptions
        if props.lambda_subscriptions:
            for fn_arn in props.lambda_subscriptions:
                lambda_fn = lambda_.Function.from_function_arn(
                    self,
                    f"SubscriberFn-{fn_arn.split(':')[-1]}",
                    function_arn=fn_arn
                )
                self.topic.add_subscription(
                    subs.LambdaSubscription(lambda_fn)
                )

        # Add tags
        if props.tags:
            for key, value in props.tags.items():
                Tags.of(self).add(key, value)

        # Output the SNS Topic ARN
        CfnOutput(
            self,
            "TopicArn",
            value=self.topic.topic_arn,
            description=f"ARN for SNS Topic {props.topic_name}"
        )
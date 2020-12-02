from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_lambda as _lambda,
    core,
)

from aws_solutions_constructs import aws_s3_lambda as s3_lambda


class DbgPdsDataPipelinePracticeStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3_bucket = s3.Bucket.from_bucket_arn(
            self, "TestBucket", bucket_arn="arn:aws:s3:::deutsche-boerse-eurex-pds"
        )

        s3_bucket_test = s3.Bucket(self, "TestBucketTwo")

        s3_lambda.S3ToLambda(
            self,
            "S3ToLambdaTest",
            existing_bucket_obj=s3_bucket_test,
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.asset("lambda"),
                handler="test.handler",
                runtime=_lambda.Runtime.PYTHON_3_8,
            ),
        )

        # queue = sqs.Queue(
        #     self,
        #     "DbgPdsDataPipelinePracticeQueue",
        #     visibility_timeout=core.Duration.seconds(300),
        # )

        # topic = sns.Topic(self, "DbgPdsDataPipelinePracticeTopic")

        # topic.add_subscription(subs.SqsSubscription(queue))

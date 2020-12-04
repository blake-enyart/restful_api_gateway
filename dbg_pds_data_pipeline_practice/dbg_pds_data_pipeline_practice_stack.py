from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _lambda_event,
    aws_ec2 as ec2,
    core,
)

# from aws_solutions_constructs import (
#     aws_s3_lambda as s3_lambda,
#     aws_lambda_sqs_lambda as lsl,
# )


class DbgPdsDataPipelinePracticeStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "MyVpc")

        vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC)

        # s3_bucket = s3.Bucket(
        #     self,
        #     "TestBucketTwo",
        #     bucket_name="blake-enyart-test-data-pipeline",
        # )

        # s3_fn = s3_lambda.S3ToLambda(
        #     self,
        #     "S3ToLambdaTest",
        #     existing_bucket_obj=s3_bucket,
        #     lambda_function_props=_lambda.FunctionProps(
        #         code=_lambda.Code.asset("lambda"),
        #         handler="test.handler",
        #         runtime=_lambda.Runtime.PYTHON_3_8,
        #     ),
        #     s3_event_source_props=_lambda_event.S3EventSourceProps(
        #         events=[s3.EventType.OBJECT_CREATED]
        #     )
        # )

        # lsl.LambdaToSqsToLambda(self,
        #     "LambdaToSQSToLambda",
        #     existing_producer_lambda_obj=s3_fn.lambda_function,
        #     consumer_lambda_function_props=_lambda.FunctionProps(
        #         code=_lambda.Code.asset("lambda"),
        #         handler="consumer.handler",
        #         runtime=_lambda.Runtime.PYTHON_3_8,
        #     )
        # )


# aws s3 sync s3://deutsche-boerse-eurex-pds/2017-05-27/ s3://blake-enyart-test-data-pipeline/

from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    core,
)


class RestfulApiGatewayStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = _lambda.DockerImageFunction(
            self,
            "RestfulApiFxn",
            code=_lambda.DockerImageCode.from_image_asset("api"),
        )

        api = apigw.LambdaRestApi(self, "TestRoute", handler=fn,)

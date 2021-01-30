import json
import pytest

from aws_cdk import core
from restful_api_gateway.restful_api_gateway_stack import (
    RestfulApiGatewayStack,
)


def get_template():
    app = core.App()
    RestfulApiGatewayStack(app, "restful-api-gateway-stack")
    return json.dumps(app.synth().get_stack("restful-api-gateway-stack").template)


def test_sqs_queue_created():
    assert "AWS::SQS::Queue" in get_template()

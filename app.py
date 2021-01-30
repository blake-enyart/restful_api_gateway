#!/usr/bin/env python3

from aws_cdk import core

from restful_api_gateway.restful_api_gateway_stack import (
    RestfulApiGatewayStack,
)

app = core.App()

RestfulApiGatewayStack(app, "restful-api-gateway-stack")

app.synth()

#!/usr/bin/env python3

from aws_cdk import core

from dbg_pds_data_pipeline_practice.dbg_pds_data_pipeline_practice_stack import (
    DbgPdsDataPipelinePracticeStack,
)

from dbg_pds_data_pipeline_practice.restful_api_gateway_stack import (
    RestfulApiGatewayStack,
)

app = core.App()
DbgPdsDataPipelinePracticeStack(app, "dbg-pds-data-pipeline-practice")

RestfulApiGatewayStack(app, "restful-api-gateway-stack")

app.synth()

#!/usr/bin/env python3

from aws_cdk import core

from dbg_pds_data_pipeline_practice.dbg_pds_data_pipeline_practice_stack import (
    DbgPdsDataPipelinePracticeStack,
)


app = core.App()
DbgPdsDataPipelinePracticeStack(
    app, "dbg-pds-data-pipeline-practice", env={"region": "us-west-2"}
)

app.synth()

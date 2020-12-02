import json
import pytest

from aws_cdk import core
from dbg_pds_data_pipeline_practice.dbg_pds_data_pipeline_practice_stack import (
    DbgPdsDataPipelinePracticeStack,
)


def get_template():
    app = core.App()
    DbgPdsDataPipelinePracticeStack(app, "dbg-pds-data-pipeline-practice")
    return json.dumps(app.synth().get_stack("dbg-pds-data-pipeline-practice").template)


def test_sqs_queue_created():
    assert "AWS::SQS::Queue" in get_template()


def test_sns_topic_created():
    assert "AWS::SNS::Topic" in get_template()

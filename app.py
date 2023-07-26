#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_codepipeline.aws_codepipeline_stack import AwsCodepipelineStack


app = cdk.App()
AwsCodepipelineStack(app, "AwsCodepipelineStack",
  

    env=cdk.Environment(account='079774713790', region='us-east-1'),
    stack_name='github-codepipeline-stack'

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )
cdk.Tags.of(app).add(key='feature',value='resource_stack')
cdk.Tags.of(app).add(key='contact',value='abc@againabc.com')
cdk.Tags.of(app).add(key='team',value='best_team')
app.synth()

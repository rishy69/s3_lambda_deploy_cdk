import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_s3_lambda.cdk_s3_lambda_stack import CdkS3LambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_s3_lambda/cdk_s3_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkS3LambdaStack(app, "cdk-s3-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

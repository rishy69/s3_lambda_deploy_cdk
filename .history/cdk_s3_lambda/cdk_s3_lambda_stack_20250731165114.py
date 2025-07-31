from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_iam as iam,
    RemovalPolicy,
    Duration
)
from constructs import Construct

class S3LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket
        bucket = s3.Bucket(
            self, "MyBucket",
            bucket_name="testing-bucket_creation",  # Make this globally unique
            removal_policy=RemovalPolicy.DESTROY,  # For development only
            auto_delete_objects=True,  # For development only
            versioned=False,
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )

        # Create Lambda function
        lambda_function = _lambda.Function(
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),  # Code will be in ./lambda directory
            function_name="my-lambda-function",
            timeout=Duration.seconds(30),
            memory_size=128,
            environment={
                "BUCKET_NAME": bucket.bucket_name
            }
        )

        # Grant Lambda permissions to read/write to S3 bucket
        bucket.grant_read_write(lambda_function)

        # Optional: Add specific IAM permissions if needed
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:DeleteObject"
                ],
                resources=[f"{bucket.bucket_arn}/*"]
            )
        )
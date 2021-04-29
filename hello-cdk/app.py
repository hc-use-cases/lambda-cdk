from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_iam as _iam
)

class SimpleLambda(core.Stack):

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:

    super().__init__(scope, id, **kwargs)

    # Create role
    lambda_role = _iam.Role(scope=self, id='cdk-lambda-role',
      assumed_by =_iam.ServicePrincipal('lambda.amazonaws.com'),
      role_name='cdk-lambda-role',
      managed_policies=[
        _iam.ManagedPolicy.from_aws_managed_policy_name(
        'service-role/AWSLambdaVPCAccessExecutionRole'),
        _iam.ManagedPolicy.from_aws_managed_policy_name(
        'service-role/AWSLambdaBasicExecutionRole')
    ])

    # Defines an AWS Lambda resource
    cdk_lambda = _lambda.Function(
      self, 'cdk-simple-lambda',
      runtime=_lambda.Runtime.PYTHON_3_7,
      function_name='cdk-simple-lambda',
      description='Simple Lambda function deployed using AWS CDK',
      code=_lambda.Code.asset('./lambda'),
      handler='SimpleLambda.handler',
      role=lambda_role,
      environment={
          'NAME': 'cdk-simple-lambda'
      }
    )

    #Output of created resource
    core.CfnOutput(scope=self, id='cdk-output', value=cdk_lambda.function_name)

app = core.App()
SimpleLambda(app, "SimpleLambda")
app.synth()
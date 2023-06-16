import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_iac_project.aws_iac_project_stack import AwsIacProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_iac_project/aws_iac_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsIacProjectStack(app, "aws-iac-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

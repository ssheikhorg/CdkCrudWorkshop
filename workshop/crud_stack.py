from aws_cdk import (
    Duration,
    Stack,
)
from constructs import Construct
from aws_cdk.aws_lambda import Function, Code, Runtime


class CrudStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Function(
            self,
            "CreateFunction",
            function_name="CreateFunction",
            code=Code.from_asset(f"workshop/crud/create"),
            runtime=Runtime.PYTHON_3_9,
            handler="index.handler",
        )

        Function(
            self,
            "ReadFunction",
            function_name="ReadFunction",
            code=Code.from_asset(f"workshop/crud/read"),
            runtime=Runtime.PYTHON_3_9,
            handler="index.handler",
        )

        Function(
            self,
            "UpdateFunction",
            function_name="UpdateFunction",
            code=Code.from_asset(f"workshop/crud/update"),
            runtime=Runtime.PYTHON_3_9,
            handler="index.handler",
        )

        Function(
            self,
            "DeleteFunction",
            function_name="DeleteFunction",
            code=Code.from_asset(f"workshop/crud/delete"),
            runtime=Runtime.PYTHON_3_9,
            handler="index.handler",
        )

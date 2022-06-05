from aws_cdk import (
    Duration,
    Stack,
)
from constructs import Construct

from aws_cdk.aws_lambda import Code
from .base_function import BaseFunction


class CrudStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.create = BaseFunction(
            self,
            "Create",
            function_name="Create",
            code=Code.from_asset(f"workshop/crud/create"),
        )

        self.read = BaseFunction(
            self,
            "Read",
            function_name="Read",
            code=Code.from_asset(f"workshop/crud/read"),
        )

        self.update = BaseFunction(
            self,
            "Update",
            function_name="Update",
            code=Code.from_asset(f"workshop/crud/update"),
        )

        self.delete = BaseFunction(
            self,
            "Delete",
            function_name="Delete",
            code=Code.from_asset(f"workshop/crud/delete"),
        )

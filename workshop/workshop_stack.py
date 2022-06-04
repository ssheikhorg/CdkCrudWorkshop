from aws_cdk import (
    Duration,
    Stack,
)
from constructs import Construct
from .crud_stack import CrudStack


class WorkshopStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        CrudStack(
            self,
            "CrudStack",
            stack_name="CrudStack",
        )

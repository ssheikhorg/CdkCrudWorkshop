from aws_cdk import (
    Duration,
    Stack,
)
from constructs import Construct
from .crud_stack import CrudStack
from .api_stack import ApiStack


class WorkshopStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        crud_stack = CrudStack(
            self,
            "CrudStack",
            stack_name="CrudStack",
        )

        api_stack = ApiStack(
            self,
            "ApiStack",
            create_backend=crud_stack.create,
            read_backend=crud_stack.read,
            update_backend=crud_stack.update,
            delete_backend=crud_stack.delete,
            stack_name="ApiStack",
        )
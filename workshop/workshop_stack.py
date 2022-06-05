from aws_cdk import (
    Duration,
    Stack,
    RemovalPolicy
)
from constructs import Construct
from .crud_stack import CrudStack
from .api_stack import ApiStack
# from .db_stack import DbStack

from aws_cdk.aws_dynamodb import (
    Table,
    AttributeType,
    Attribute,
    TableEncryption,
    # RemovalPolicy,
)


class WorkshopStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """dynamodb table"""
        crud_table = Table(
            self,
            "crud_table",
            partition_key=Attribute(name="id", type=AttributeType.STRING),
            table_name="crud_table",
            removal_policy=RemovalPolicy.DESTROY,            
            read_capacity=1,
            write_capacity=1,
        )

        """lambda crud stack"""
        crud_lambda_stack = CrudStack(
            self,
            "CrudStack",
            stack_name="CrudStack",
        )
        crud_lambda_stack.create.add_environment("crud_table", crud_table.table_name)
        crud_table.grant_read_write_data(crud_lambda_stack.create)
        crud_lambda_stack.read.add_environment("crud_table", crud_table.table_name)
        crud_table.grant_read_write_data(crud_lambda_stack.read)
        crud_lambda_stack.update.add_environment("crud_table", crud_table.table_name)
        crud_table.grant_read_write_data(crud_lambda_stack.update)
        crud_lambda_stack.delete.add_environment("crud_table", crud_table.table_name)
        crud_table.grant_read_write_data(crud_lambda_stack.delete)

        """apigateway stack"""
        api_stack = ApiStack(
            self,
            "ApiStack",
            create_backend=crud_lambda_stack.create,
            read_backend=crud_lambda_stack.read,
            update_backend=crud_lambda_stack.update,
            delete_backend=crud_lambda_stack.delete,
            stack_name="ApiStack",
        )

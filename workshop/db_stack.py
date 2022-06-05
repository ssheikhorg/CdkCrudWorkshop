from aws_cdk import Stack, RemovalPolicy
from constructs import Construct
from aws_cdk.aws_dynamodb import Table, AttributeType, Attribute, TableEncryption


class DBStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.table = Table(
            self,
            "crud_table",
            partition_key=Attribute(name="id", type=AttributeType.STRING),
            read_capacity=1,
            write_capacity=1,
        )

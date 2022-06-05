from aws_cdk.aws_lambda import Function, Code, Runtime
from constructs import Construct

# from .db_stack import DbStack, CrudTable


class BaseFunction(Function):
    def __init__(
        self,
        scope: Construct,
        id: str,
        function_name: str,
        code: Code,
        # crud_table: CrudTable,
        **kwargs,
    ) -> None:
        super().__init__(
            scope,
            id,
            function_name=function_name,
            code=code,
            runtime=Runtime.PYTHON_3_9,
            handler="index.handler",            
            **kwargs,
        )

from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
)
from aws_cdk.aws_lambda import Function
from constructs import Construct
from aws_cdk.aws_apigatewayv2_alpha import (
    CorsHttpMethod,
    HttpApi,
    HttpMethod,
    CorsPreflightOptions,
    HttpStage,
)
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration


class ApiStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        create_backend: Function,
        read_backend: Function,
        update_backend: Function,
        delete_backend: Function,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create our HTTP Api
        http_api = HttpApi(
            self,
            "crud-api",
            description="CRUD API",
            api_name="crud-api",
            cors_preflight=CorsPreflightOptions(
                allow_origins=["*"],
                allow_headers=["*"],
                allow_methods=[
                    CorsHttpMethod.GET,
                    CorsHttpMethod.POST,
                    CorsHttpMethod.PUT,
                    CorsHttpMethod.DELETE,                    
                    CorsHttpMethod.OPTIONS,
                ],
                max_age=Duration.days(1),
            ),
        )

        # create integration for create
        create_integration = HttpLambdaIntegration("create-integration", create_backend)
        read_integration = HttpLambdaIntegration("read-integration", read_backend)
        update_integration = HttpLambdaIntegration("update-integration", update_backend)
        delete_integration = HttpLambdaIntegration("delete-integration", delete_backend)

        # create routes for apis
        create_route = http_api.add_routes(
            path="/create", methods=[HttpMethod.POST], integration=create_integration
        )
        read_route = http_api.add_routes(
            path="/read/{id}", methods=[HttpMethod.GET], integration=read_integration
        )
        update_route = http_api.add_routes(
            path="/update/{id}", methods=[HttpMethod.PUT], integration=update_integration
        )
        delete_route = http_api.add_routes(
            path="/delete/{id}", methods=[HttpMethod.DELETE], integration=delete_integration
        )

        # create output url for api
        CfnOutput(
            self,
            "curd-api-url",
            value=http_api.url,
            description="CRUD API URL",
        )

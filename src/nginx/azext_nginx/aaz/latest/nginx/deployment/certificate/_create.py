# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "nginx deployment certificate create",
)
class Create(AAZCommand):
    """Create a certificate for an NGINX deployment

    :example: Certificate Create
        az nginx deployment certificate create --certificate-name myCertificate --deployment-name myDeployment --resource-group myResourceGroup --certificate-path /etc/nginx/test.cert --key-path /etc/nginx/test.key --key-vault-secret-id keyVaultSecretId
    """

    _aaz_info = {
        "version": "2024-06-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/nginx.nginxplus/nginxdeployments/{}/certificates/{}", "2024-06-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.certificate_name = AAZStrArg(
            options=["-n", "--name", "--certificate-name"],
            help="The name of certificate",
            required=True,
        )
        _args_schema.deployment_name = AAZStrArg(
            options=["--deployment-name"],
            help="The name of targeted Nginx deployment",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^([a-z0-9A-Z][a-z0-9A-Z-]{0,28}[a-z0-9A-Z]|[a-z0-9A-Z])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.certificate_path = AAZStrArg(
            options=["--certificate-path"],
            arg_group="Properties",
            help={"short-summary": "Certificate path in Nginx configuration structure", "long-summary": "This path must match one or more ssl_certificate directive file argument in your Nginx configuration. This path must be unique between certificates within the same deployment"},
        )
        _args_schema.key_vault_secret_id = AAZStrArg(
            options=["--key-vault-secret-id"],
            arg_group="Properties",
            help="The secret ID for your certificate from Azure Key Vault",
        )
        _args_schema.key_path = AAZStrArg(
            options=["--key-path"],
            arg_group="Properties",
            help={"short-summary": "Key path in Nginx configuration structure", "long-summary": "This path must match one or more ssl_certificate_key directive file argument in your Nginx configuration. This path must be unique between certificates within the same deployment"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.CertificatesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CertificatesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/certificates/{certificateName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "certificateName", self.ctx.args.certificate_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("certificateVirtualPath", AAZStrType, ".certificate_path")
                properties.set_prop("keyVaultSecretId", AAZStrType, ".key_vault_secret_id")
                properties.set_prop("keyVirtualPath", AAZStrType, ".key_path")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType()
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.certificate_error = AAZObjectType(
                serialized_name="certificateError",
            )
            properties.certificate_virtual_path = AAZStrType(
                serialized_name="certificateVirtualPath",
            )
            properties.key_vault_secret_created = AAZStrType(
                serialized_name="keyVaultSecretCreated",
                flags={"read_only": True},
            )
            properties.key_vault_secret_id = AAZStrType(
                serialized_name="keyVaultSecretId",
            )
            properties.key_vault_secret_version = AAZStrType(
                serialized_name="keyVaultSecretVersion",
                flags={"read_only": True},
            )
            properties.key_virtual_path = AAZStrType(
                serialized_name="keyVirtualPath",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sha1_thumbprint = AAZStrType(
                serialized_name="sha1Thumbprint",
                flags={"read_only": True},
            )

            certificate_error = cls._schema_on_200_201.properties.certificate_error
            certificate_error.code = AAZStrType()
            certificate_error.message = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]

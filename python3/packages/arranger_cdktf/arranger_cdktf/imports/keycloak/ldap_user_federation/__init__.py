"""
# `keycloak_ldap_user_federation`

Refer to the Terraform Registory for docs: [`keycloak_ldap_user_federation`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation).
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class LdapUserFederation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.ldapUserFederation.LdapUserFederation",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation keycloak_ldap_user_federation}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        connection_url: builtins.str,
        name: builtins.str,
        rdn_ldap_attribute: builtins.str,
        realm_id: builtins.str,
        username_ldap_attribute: builtins.str,
        user_object_classes: typing.Sequence[builtins.str],
        users_dn: builtins.str,
        uuid_ldap_attribute: builtins.str,
        batch_size_for_sync: typing.Optional[jsii.Number] = None,
        bind_credential: typing.Optional[builtins.str] = None,
        bind_dn: typing.Optional[builtins.str] = None,
        cache: typing.Optional[
            typing.Union[
                "LdapUserFederationCache", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        changed_sync_period: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[builtins.str] = None,
        custom_user_search_filter: typing.Optional[builtins.str] = None,
        delete_default_mappers: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        edit_mode: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        full_sync_period: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        import_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        kerberos: typing.Optional[
            typing.Union[
                "LdapUserFederationKerberos", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        pagination: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        priority: typing.Optional[jsii.Number] = None,
        read_timeout: typing.Optional[builtins.str] = None,
        search_scope: typing.Optional[builtins.str] = None,
        start_tls: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_registrations: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_password_modify_extended_op: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_truststore_spi: typing.Optional[builtins.str] = None,
        validate_password_policy: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        vendor: typing.Optional[builtins.str] = None,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation keycloak_ldap_user_federation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_url: Connection URL to the LDAP server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#connection_url LdapUserFederation#connection_url}
        :param name: Display name of the provider when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#name LdapUserFederation#name}
        :param rdn_ldap_attribute: Name of the LDAP attribute to use as the relative distinguished name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#rdn_ldap_attribute LdapUserFederation#rdn_ldap_attribute}
        :param realm_id: The realm this provider will provide user federation for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#realm_id LdapUserFederation#realm_id}
        :param username_ldap_attribute: Name of the LDAP attribute to use as the Keycloak username. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#username_ldap_attribute LdapUserFederation#username_ldap_attribute}
        :param user_object_classes: All values of LDAP objectClass attribute for users in LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#user_object_classes LdapUserFederation#user_object_classes}
        :param users_dn: Full DN of LDAP tree where your users are. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#users_dn LdapUserFederation#users_dn}
        :param uuid_ldap_attribute: Name of the LDAP attribute to use as a unique object identifier for objects in LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#uuid_ldap_attribute LdapUserFederation#uuid_ldap_attribute}
        :param batch_size_for_sync: The number of users to sync within a single transaction. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#batch_size_for_sync LdapUserFederation#batch_size_for_sync}
        :param bind_credential: Password of LDAP admin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#bind_credential LdapUserFederation#bind_credential}
        :param bind_dn: DN of LDAP admin, which will be used by Keycloak to access LDAP server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#bind_dn LdapUserFederation#bind_dn}
        :param cache: cache block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#cache LdapUserFederation#cache}
        :param changed_sync_period: How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#changed_sync_period LdapUserFederation#changed_sync_period}
        :param connection_timeout: LDAP connection timeout (duration string). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#connection_timeout LdapUserFederation#connection_timeout}
        :param custom_user_search_filter: Additional LDAP filter for filtering searched users. Must begin with '(' and end with ')'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#custom_user_search_filter LdapUserFederation#custom_user_search_filter}
        :param delete_default_mappers: When true, the provider will delete the default mappers which are normally created by Keycloak when creating an LDAP user federation provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#delete_default_mappers LdapUserFederation#delete_default_mappers}
        :param edit_mode: READ_ONLY and WRITABLE are self-explanatory. UNSYNCED allows user data to be imported but not synced back to LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#edit_mode LdapUserFederation#edit_mode}
        :param enabled: When false, this provider will not be used when performing queries for users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#enabled LdapUserFederation#enabled}
        :param full_sync_period: How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#full_sync_period LdapUserFederation#full_sync_period}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#id LdapUserFederation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_enabled: When true, LDAP users will be imported into the Keycloak database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#import_enabled LdapUserFederation#import_enabled}
        :param kerberos: kerberos block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#kerberos LdapUserFederation#kerberos}
        :param pagination: When true, Keycloak assumes the LDAP server supports pagination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#pagination LdapUserFederation#pagination}
        :param priority: Priority of this provider when looking up users. Lower values are first. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#priority LdapUserFederation#priority}
        :param read_timeout: LDAP read timeout (duration string). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#read_timeout LdapUserFederation#read_timeout}
        :param search_scope: ONE_LEVEL: only search for users in the DN specified by user_dn. SUBTREE: search entire LDAP subtree. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#search_scope LdapUserFederation#search_scope}
        :param start_tls: When true, Keycloak will encrypt the connection to LDAP using STARTTLS, which will disable connection pooling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#start_tls LdapUserFederation#start_tls}
        :param sync_registrations: When true, newly created users will be synced back to LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#sync_registrations LdapUserFederation#sync_registrations}
        :param trust_email: If enabled, email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#trust_email LdapUserFederation#trust_email}
        :param use_password_modify_extended_op: When ``true``, use the LDAPv3 Password Modify Extended Operation (RFC-3062). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_password_modify_extended_op LdapUserFederation#use_password_modify_extended_op}
        :param use_truststore_spi: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_truststore_spi LdapUserFederation#use_truststore_spi}.
        :param validate_password_policy: When true, Keycloak will validate passwords using the realm policy before updating it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#validate_password_policy LdapUserFederation#validate_password_policy}
        :param vendor: LDAP vendor. I am almost certain this field does nothing, but the UI indicates that it is required. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#vendor LdapUserFederation#vendor}
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4d9ec54577e521031be59ee398adfbb4988c8ea336dface5be90385316251633
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = LdapUserFederationConfig(
            connection_url=connection_url,
            name=name,
            rdn_ldap_attribute=rdn_ldap_attribute,
            realm_id=realm_id,
            username_ldap_attribute=username_ldap_attribute,
            user_object_classes=user_object_classes,
            users_dn=users_dn,
            uuid_ldap_attribute=uuid_ldap_attribute,
            batch_size_for_sync=batch_size_for_sync,
            bind_credential=bind_credential,
            bind_dn=bind_dn,
            cache=cache,
            changed_sync_period=changed_sync_period,
            connection_timeout=connection_timeout,
            custom_user_search_filter=custom_user_search_filter,
            delete_default_mappers=delete_default_mappers,
            edit_mode=edit_mode,
            enabled=enabled,
            full_sync_period=full_sync_period,
            id=id,
            import_enabled=import_enabled,
            kerberos=kerberos,
            pagination=pagination,
            priority=priority,
            read_timeout=read_timeout,
            search_scope=search_scope,
            start_tls=start_tls,
            sync_registrations=sync_registrations,
            trust_email=trust_email,
            use_password_modify_extended_op=use_password_modify_extended_op,
            use_truststore_spi=use_truststore_spi,
            validate_password_policy=validate_password_policy,
            vendor=vendor,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCache")
    def put_cache(
        self,
        *,
        eviction_day: typing.Optional[jsii.Number] = None,
        eviction_hour: typing.Optional[jsii.Number] = None,
        eviction_minute: typing.Optional[jsii.Number] = None,
        max_lifespan: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param eviction_day: Day of the week the entry will become invalid on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_day LdapUserFederation#eviction_day}
        :param eviction_hour: Hour of day the entry will become invalid on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_hour LdapUserFederation#eviction_hour}
        :param eviction_minute: Minute of day the entry will become invalid on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_minute LdapUserFederation#eviction_minute}
        :param max_lifespan: Max lifespan of cache entry (duration string). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#max_lifespan LdapUserFederation#max_lifespan}
        :param policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#policy LdapUserFederation#policy}.
        """
        value = LdapUserFederationCache(
            eviction_day=eviction_day,
            eviction_hour=eviction_hour,
            eviction_minute=eviction_minute,
            max_lifespan=max_lifespan,
            policy=policy,
        )

        return typing.cast(None, jsii.invoke(self, "putCache", [value]))

    @jsii.member(jsii_name="putKerberos")
    def put_kerberos(
        self,
        *,
        kerberos_realm: builtins.str,
        key_tab: builtins.str,
        server_principal: builtins.str,
        use_kerberos_for_password_authentication: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param kerberos_realm: The name of the kerberos realm, e.g. FOO.LOCAL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#kerberos_realm LdapUserFederation#kerberos_realm}
        :param key_tab: Path to the kerberos keytab file on the server with credentials of the service principal. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#key_tab LdapUserFederation#key_tab}
        :param server_principal: The kerberos server principal, e.g. 'HTTP/host.foo.com@FOO.LOCAL'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#server_principal LdapUserFederation#server_principal}
        :param use_kerberos_for_password_authentication: Use kerberos login module instead of ldap service api. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_kerberos_for_password_authentication LdapUserFederation#use_kerberos_for_password_authentication}
        """
        value = LdapUserFederationKerberos(
            kerberos_realm=kerberos_realm,
            key_tab=key_tab,
            server_principal=server_principal,
            use_kerberos_for_password_authentication=use_kerberos_for_password_authentication,
        )

        return typing.cast(None, jsii.invoke(self, "putKerberos", [value]))

    @jsii.member(jsii_name="resetBatchSizeForSync")
    def reset_batch_size_for_sync(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchSizeForSync", []))

    @jsii.member(jsii_name="resetBindCredential")
    def reset_bind_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBindCredential", []))

    @jsii.member(jsii_name="resetBindDn")
    def reset_bind_dn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBindDn", []))

    @jsii.member(jsii_name="resetCache")
    def reset_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCache", []))

    @jsii.member(jsii_name="resetChangedSyncPeriod")
    def reset_changed_sync_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangedSyncPeriod", []))

    @jsii.member(jsii_name="resetConnectionTimeout")
    def reset_connection_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionTimeout", []))

    @jsii.member(jsii_name="resetCustomUserSearchFilter")
    def reset_custom_user_search_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomUserSearchFilter", []))

    @jsii.member(jsii_name="resetDeleteDefaultMappers")
    def reset_delete_default_mappers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteDefaultMappers", []))

    @jsii.member(jsii_name="resetEditMode")
    def reset_edit_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEditMode", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFullSyncPeriod")
    def reset_full_sync_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullSyncPeriod", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportEnabled")
    def reset_import_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportEnabled", []))

    @jsii.member(jsii_name="resetKerberos")
    def reset_kerberos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberos", []))

    @jsii.member(jsii_name="resetPagination")
    def reset_pagination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPagination", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetReadTimeout")
    def reset_read_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadTimeout", []))

    @jsii.member(jsii_name="resetSearchScope")
    def reset_search_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchScope", []))

    @jsii.member(jsii_name="resetStartTls")
    def reset_start_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTls", []))

    @jsii.member(jsii_name="resetSyncRegistrations")
    def reset_sync_registrations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncRegistrations", []))

    @jsii.member(jsii_name="resetTrustEmail")
    def reset_trust_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustEmail", []))

    @jsii.member(jsii_name="resetUsePasswordModifyExtendedOp")
    def reset_use_password_modify_extended_op(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetUsePasswordModifyExtendedOp", [])
        )

    @jsii.member(jsii_name="resetUseTruststoreSpi")
    def reset_use_truststore_spi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseTruststoreSpi", []))

    @jsii.member(jsii_name="resetValidatePasswordPolicy")
    def reset_validate_password_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidatePasswordPolicy", []))

    @jsii.member(jsii_name="resetVendor")
    def reset_vendor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVendor", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(
            typing.Mapping[builtins.str, typing.Any],
            jsii.invoke(self, "synthesizeAttributes", []),
        )

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cache")
    def cache(self) -> "LdapUserFederationCacheOutputReference":
        return typing.cast(
            "LdapUserFederationCacheOutputReference", jsii.get(self, "cache")
        )

    @builtins.property
    @jsii.member(jsii_name="kerberos")
    def kerberos(self) -> "LdapUserFederationKerberosOutputReference":
        return typing.cast(
            "LdapUserFederationKerberosOutputReference", jsii.get(self, "kerberos")
        )

    @builtins.property
    @jsii.member(jsii_name="batchSizeForSyncInput")
    def batch_size_for_sync_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "batchSizeForSyncInput")
        )

    @builtins.property
    @jsii.member(jsii_name="bindCredentialInput")
    def bind_credential_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "bindCredentialInput")
        )

    @builtins.property
    @jsii.member(jsii_name="bindDnInput")
    def bind_dn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bindDnInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheInput")
    def cache_input(self) -> typing.Optional["LdapUserFederationCache"]:
        return typing.cast(
            typing.Optional["LdapUserFederationCache"], jsii.get(self, "cacheInput")
        )

    @builtins.property
    @jsii.member(jsii_name="changedSyncPeriodInput")
    def changed_sync_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "changedSyncPeriodInput")
        )

    @builtins.property
    @jsii.member(jsii_name="connectionTimeoutInput")
    def connection_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "connectionTimeoutInput")
        )

    @builtins.property
    @jsii.member(jsii_name="connectionUrlInput")
    def connection_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "connectionUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="customUserSearchFilterInput")
    def custom_user_search_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "customUserSearchFilterInput")
        )

    @builtins.property
    @jsii.member(jsii_name="deleteDefaultMappersInput")
    def delete_default_mappers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "deleteDefaultMappersInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="editModeInput")
    def edit_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "editModeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "enabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="fullSyncPeriodInput")
    def full_sync_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "fullSyncPeriodInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importEnabledInput")
    def import_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "importEnabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="kerberosInput")
    def kerberos_input(self) -> typing.Optional["LdapUserFederationKerberos"]:
        return typing.cast(
            typing.Optional["LdapUserFederationKerberos"],
            jsii.get(self, "kerberosInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="paginationInput")
    def pagination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "paginationInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "priorityInput")
        )

    @builtins.property
    @jsii.member(jsii_name="rdnLdapAttributeInput")
    def rdn_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "rdnLdapAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="readTimeoutInput")
    def read_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "readTimeoutInput")
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="searchScopeInput")
    def search_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "searchScopeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="startTlsInput")
    def start_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "startTlsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="syncRegistrationsInput")
    def sync_registrations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "syncRegistrationsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="trustEmailInput")
    def trust_email_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "trustEmailInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="usePasswordModifyExtendedOpInput")
    def use_password_modify_extended_op_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "usePasswordModifyExtendedOpInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="usernameLdapAttributeInput")
    def username_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "usernameLdapAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="userObjectClassesInput")
    def user_object_classes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "userObjectClassesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="usersDnInput")
    def users_dn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "usersDnInput")
        )

    @builtins.property
    @jsii.member(jsii_name="useTruststoreSpiInput")
    def use_truststore_spi_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "useTruststoreSpiInput")
        )

    @builtins.property
    @jsii.member(jsii_name="uuidLdapAttributeInput")
    def uuid_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "uuidLdapAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="validatePasswordPolicyInput")
    def validate_password_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "validatePasswordPolicyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="vendorInput")
    def vendor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendorInput"))

    @builtins.property
    @jsii.member(jsii_name="batchSizeForSync")
    def batch_size_for_sync(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "batchSizeForSync"))

    @batch_size_for_sync.setter
    def batch_size_for_sync(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c2b80f7895ce3a83ab330399171ab2a0ee2069cc997be70723ea9233d0436b48
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "batchSizeForSync", value)

    @builtins.property
    @jsii.member(jsii_name="bindCredential")
    def bind_credential(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bindCredential"))

    @bind_credential.setter
    def bind_credential(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f30436108c467f348d50385f3eaa93b3d30a0cf681544d8b3b4b1f272f531de3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "bindCredential", value)

    @builtins.property
    @jsii.member(jsii_name="bindDn")
    def bind_dn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bindDn"))

    @bind_dn.setter
    def bind_dn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b668caf05c5d29897f5425799cba8319a0d09dab89bb53e2d3095685b82a695f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "bindDn", value)

    @builtins.property
    @jsii.member(jsii_name="changedSyncPeriod")
    def changed_sync_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "changedSyncPeriod"))

    @changed_sync_period.setter
    def changed_sync_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7949b87c7ebb1c2f61d3b9c09f4c01cf671a6a0dcabf5203c9ccb2bedeec86b3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "changedSyncPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="connectionTimeout")
    def connection_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionTimeout"))

    @connection_timeout.setter
    def connection_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c1b06d14ae9a708fe0160fcd5f93e2bef322c4fb3be63a4821959fb9c8331720
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "connectionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="connectionUrl")
    def connection_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionUrl"))

    @connection_url.setter
    def connection_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__45bb298e07f837bf93328bafd0e5d49722f75dc0d793f0b3598d694cae1ab393
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "connectionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="customUserSearchFilter")
    def custom_user_search_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customUserSearchFilter"))

    @custom_user_search_filter.setter
    def custom_user_search_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b70aecd2e4751d75e50364477ed76230ed760a9d36a453a0fe4831d3c61e9d42
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "customUserSearchFilter", value)

    @builtins.property
    @jsii.member(jsii_name="deleteDefaultMappers")
    def delete_default_mappers(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "deleteDefaultMappers"),
        )

    @delete_default_mappers.setter
    def delete_default_mappers(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ddfcea9e2f161f1937b8e31b3c342b2f4f85901db359632d1211d124ac52dc02
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "deleteDefaultMappers", value)

    @builtins.property
    @jsii.member(jsii_name="editMode")
    def edit_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "editMode"))

    @edit_mode.setter
    def edit_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b3383c048e2d6a41b53458e3c9e440a1b75add65b1ed1c8adaa73a65747ded75
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "editMode", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "enabled"),
        )

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__da261c7843c9bba96bc970b5d71d3528e68c3bba66ec75d10d1f9a04df10bca8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="fullSyncPeriod")
    def full_sync_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fullSyncPeriod"))

    @full_sync_period.setter
    def full_sync_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__926ed29780ebcf0785e1610f8c55cc597c6d678d7faa782f4177e93791de97db
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "fullSyncPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__34ed1d55ff0effe9108873f45d0e15666e8aaa87bd39d498b8c255ec741c4d78
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importEnabled")
    def import_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "importEnabled"),
        )

    @import_enabled.setter
    def import_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__68869993e30e12257a152c0713d4d96a32b96a9d849ab0fbe39b599580d1c793
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "importEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0738e96714242e00f769af0fc6a18b9988ff76ddcb51db2ec66613fe03ed67e5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pagination")
    def pagination(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "pagination"),
        )

    @pagination.setter
    def pagination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a7f73b5fa78f4d0f84000328dbd2da2ec3714f728e36ec8520a708ec8976e200
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "pagination", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5971d72054917d3fdf04bcb568064e73509f467c25e2ea2d49420003c1924d73
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="rdnLdapAttribute")
    def rdn_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rdnLdapAttribute"))

    @rdn_ldap_attribute.setter
    def rdn_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__694089ff3a7920e321a5b47357603747883700e6342ee73f10f7691ffc412bc8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "rdnLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="readTimeout")
    def read_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readTimeout"))

    @read_timeout.setter
    def read_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__86ce6fc2bb57dfacbba3e2d58b3b1beca013f13e290fea7c04851696198f5fea
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "readTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1348006e07dfdc85704e537f24cfc0b4988e70b81e9f1b0a7b3b9b6c3effa6e6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="searchScope")
    def search_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "searchScope"))

    @search_scope.setter
    def search_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c2312348236931bd014f254e21b7748add18d87cfe8c06844d6bb98acb62f721
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "searchScope", value)

    @builtins.property
    @jsii.member(jsii_name="startTls")
    def start_tls(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "startTls"),
        )

    @start_tls.setter
    def start_tls(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7a073182d3c07ffb97ac1951fb56da9eee6b2d85516b6cdc3bc27cc64c90846f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "startTls", value)

    @builtins.property
    @jsii.member(jsii_name="syncRegistrations")
    def sync_registrations(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "syncRegistrations"),
        )

    @sync_registrations.setter
    def sync_registrations(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a4ce81fb1cb11fb3a8e7ea638dbb404503e0a23327687c97f2086e54440684eb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "syncRegistrations", value)

    @builtins.property
    @jsii.member(jsii_name="trustEmail")
    def trust_email(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "trustEmail"),
        )

    @trust_email.setter
    def trust_email(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2f84e390d542abade19db6c6a1424a8b3720b3abbec81d029934c92a411f52a3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "trustEmail", value)

    @builtins.property
    @jsii.member(jsii_name="usePasswordModifyExtendedOp")
    def use_password_modify_extended_op(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "usePasswordModifyExtendedOp"),
        )

    @use_password_modify_extended_op.setter
    def use_password_modify_extended_op(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__61ca871a07efcda8899b1528d4484ebda7fe5769d72a11f833a244df4488aa2d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "usePasswordModifyExtendedOp", value)

    @builtins.property
    @jsii.member(jsii_name="usernameLdapAttribute")
    def username_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameLdapAttribute"))

    @username_ldap_attribute.setter
    def username_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2da999742cabaec8153305cc856cb786e52f772baf27f99c0c34b845c5d625b3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "usernameLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="userObjectClasses")
    def user_object_classes(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "userObjectClasses")
        )

    @user_object_classes.setter
    def user_object_classes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4e9834c3ba47b8f6a4a8ad7cb09e5277c89e75f27643f2d12fa66325878f79ba
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userObjectClasses", value)

    @builtins.property
    @jsii.member(jsii_name="usersDn")
    def users_dn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usersDn"))

    @users_dn.setter
    def users_dn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__be173eb2a41e9514f015da2255c70da787a6d8d6cff6da303b5ce28f5870092b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "usersDn", value)

    @builtins.property
    @jsii.member(jsii_name="useTruststoreSpi")
    def use_truststore_spi(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useTruststoreSpi"))

    @use_truststore_spi.setter
    def use_truststore_spi(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__714470d46ff59bd14339df1401cadaf220b548c4523e8a30d4f3182780e8516d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "useTruststoreSpi", value)

    @builtins.property
    @jsii.member(jsii_name="uuidLdapAttribute")
    def uuid_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuidLdapAttribute"))

    @uuid_ldap_attribute.setter
    def uuid_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__26a434ac7a4f5f4b12f738558c6f6248086717a259738545ea79d8b1698ec113
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "uuidLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="validatePasswordPolicy")
    def validate_password_policy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "validatePasswordPolicy"),
        )

    @validate_password_policy.setter
    def validate_password_policy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f459fda8bcba872a66f582b02d635e3e4837748b102eadeaa1dc819d4d551e97
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "validatePasswordPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__72267cc4157d6a78378ecfe5ca5fcd0e397ebbf753e496fb39bf24b316b071d0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "vendor", value)


@jsii.data_type(
    jsii_type="keycloak.ldapUserFederation.LdapUserFederationCache",
    jsii_struct_bases=[],
    name_mapping={
        "eviction_day": "evictionDay",
        "eviction_hour": "evictionHour",
        "eviction_minute": "evictionMinute",
        "max_lifespan": "maxLifespan",
        "policy": "policy",
    },
)
class LdapUserFederationCache:
    def __init__(
        self,
        *,
        eviction_day: typing.Optional[jsii.Number] = None,
        eviction_hour: typing.Optional[jsii.Number] = None,
        eviction_minute: typing.Optional[jsii.Number] = None,
        max_lifespan: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param eviction_day: Day of the week the entry will become invalid on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_day LdapUserFederation#eviction_day}
        :param eviction_hour: Hour of day the entry will become invalid on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_hour LdapUserFederation#eviction_hour}
        :param eviction_minute: Minute of day the entry will become invalid on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_minute LdapUserFederation#eviction_minute}
        :param max_lifespan: Max lifespan of cache entry (duration string). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#max_lifespan LdapUserFederation#max_lifespan}
        :param policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#policy LdapUserFederation#policy}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3bcaffd363bb3d22326184cf1828eb2131664d9d1c3985c03ced2eeb950afbe0
            )
            check_type(
                argname="argument eviction_day",
                value=eviction_day,
                expected_type=type_hints["eviction_day"],
            )
            check_type(
                argname="argument eviction_hour",
                value=eviction_hour,
                expected_type=type_hints["eviction_hour"],
            )
            check_type(
                argname="argument eviction_minute",
                value=eviction_minute,
                expected_type=type_hints["eviction_minute"],
            )
            check_type(
                argname="argument max_lifespan",
                value=max_lifespan,
                expected_type=type_hints["max_lifespan"],
            )
            check_type(
                argname="argument policy",
                value=policy,
                expected_type=type_hints["policy"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if eviction_day is not None:
            self._values["eviction_day"] = eviction_day
        if eviction_hour is not None:
            self._values["eviction_hour"] = eviction_hour
        if eviction_minute is not None:
            self._values["eviction_minute"] = eviction_minute
        if max_lifespan is not None:
            self._values["max_lifespan"] = max_lifespan
        if policy is not None:
            self._values["policy"] = policy

    @builtins.property
    def eviction_day(self) -> typing.Optional[jsii.Number]:
        """Day of the week the entry will become invalid on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_day LdapUserFederation#eviction_day}
        """
        result = self._values.get("eviction_day")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def eviction_hour(self) -> typing.Optional[jsii.Number]:
        """Hour of day the entry will become invalid on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_hour LdapUserFederation#eviction_hour}
        """
        result = self._values.get("eviction_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def eviction_minute(self) -> typing.Optional[jsii.Number]:
        """Minute of day the entry will become invalid on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#eviction_minute LdapUserFederation#eviction_minute}
        """
        result = self._values.get("eviction_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_lifespan(self) -> typing.Optional[builtins.str]:
        """Max lifespan of cache entry (duration string).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#max_lifespan LdapUserFederation#max_lifespan}
        """
        result = self._values.get("max_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#policy LdapUserFederation#policy}."""
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LdapUserFederationCache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LdapUserFederationCacheOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.ldapUserFederation.LdapUserFederationCacheOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b51a005647b5b81bbd4c794406ecc3cdb083e3c04d04807bbfa24fc0cb8db201
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvictionDay")
    def reset_eviction_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvictionDay", []))

    @jsii.member(jsii_name="resetEvictionHour")
    def reset_eviction_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvictionHour", []))

    @jsii.member(jsii_name="resetEvictionMinute")
    def reset_eviction_minute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvictionMinute", []))

    @jsii.member(jsii_name="resetMaxLifespan")
    def reset_max_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLifespan", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="evictionDayInput")
    def eviction_day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "evictionDayInput")
        )

    @builtins.property
    @jsii.member(jsii_name="evictionHourInput")
    def eviction_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "evictionHourInput")
        )

    @builtins.property
    @jsii.member(jsii_name="evictionMinuteInput")
    def eviction_minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "evictionMinuteInput")
        )

    @builtins.property
    @jsii.member(jsii_name="maxLifespanInput")
    def max_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "maxLifespanInput")
        )

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="evictionDay")
    def eviction_day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evictionDay"))

    @eviction_day.setter
    def eviction_day(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__50c23fc36902aba4b8a09d6eb2398f9c58febc929a65c9ef75b4b5d208e558e7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "evictionDay", value)

    @builtins.property
    @jsii.member(jsii_name="evictionHour")
    def eviction_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evictionHour"))

    @eviction_hour.setter
    def eviction_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a7e9d434537138565eb2605195f2af9ee069f05fa2024dc6b9cd25420f970f96
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "evictionHour", value)

    @builtins.property
    @jsii.member(jsii_name="evictionMinute")
    def eviction_minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evictionMinute"))

    @eviction_minute.setter
    def eviction_minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c3c4f62cba0cdcee6efad987c922df7b7e7bf3ddcde72a1eac2bbfde412a6385
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "evictionMinute", value)

    @builtins.property
    @jsii.member(jsii_name="maxLifespan")
    def max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxLifespan"))

    @max_lifespan.setter
    def max_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a6afd8b19e5b36540d564113f6958fd0b482ffc4ab1219f78fd45df4f0020640
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "maxLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cb16078bd64add9bd1d05d3d0109e2d4911349332d95293796a2b1ca860b061b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LdapUserFederationCache]:
        return typing.cast(
            typing.Optional[LdapUserFederationCache], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LdapUserFederationCache]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0b1345d040460360f56be2dae2f887ca8a89a48ba9b81e7c12c87701ed530350
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.ldapUserFederation.LdapUserFederationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connection_url": "connectionUrl",
        "name": "name",
        "rdn_ldap_attribute": "rdnLdapAttribute",
        "realm_id": "realmId",
        "username_ldap_attribute": "usernameLdapAttribute",
        "user_object_classes": "userObjectClasses",
        "users_dn": "usersDn",
        "uuid_ldap_attribute": "uuidLdapAttribute",
        "batch_size_for_sync": "batchSizeForSync",
        "bind_credential": "bindCredential",
        "bind_dn": "bindDn",
        "cache": "cache",
        "changed_sync_period": "changedSyncPeriod",
        "connection_timeout": "connectionTimeout",
        "custom_user_search_filter": "customUserSearchFilter",
        "delete_default_mappers": "deleteDefaultMappers",
        "edit_mode": "editMode",
        "enabled": "enabled",
        "full_sync_period": "fullSyncPeriod",
        "id": "id",
        "import_enabled": "importEnabled",
        "kerberos": "kerberos",
        "pagination": "pagination",
        "priority": "priority",
        "read_timeout": "readTimeout",
        "search_scope": "searchScope",
        "start_tls": "startTls",
        "sync_registrations": "syncRegistrations",
        "trust_email": "trustEmail",
        "use_password_modify_extended_op": "usePasswordModifyExtendedOp",
        "use_truststore_spi": "useTruststoreSpi",
        "validate_password_policy": "validatePasswordPolicy",
        "vendor": "vendor",
    },
)
class LdapUserFederationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
        connection_url: builtins.str,
        name: builtins.str,
        rdn_ldap_attribute: builtins.str,
        realm_id: builtins.str,
        username_ldap_attribute: builtins.str,
        user_object_classes: typing.Sequence[builtins.str],
        users_dn: builtins.str,
        uuid_ldap_attribute: builtins.str,
        batch_size_for_sync: typing.Optional[jsii.Number] = None,
        bind_credential: typing.Optional[builtins.str] = None,
        bind_dn: typing.Optional[builtins.str] = None,
        cache: typing.Optional[
            typing.Union[LdapUserFederationCache, typing.Dict[builtins.str, typing.Any]]
        ] = None,
        changed_sync_period: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[builtins.str] = None,
        custom_user_search_filter: typing.Optional[builtins.str] = None,
        delete_default_mappers: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        edit_mode: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        full_sync_period: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        import_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        kerberos: typing.Optional[
            typing.Union[
                "LdapUserFederationKerberos", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        pagination: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        priority: typing.Optional[jsii.Number] = None,
        read_timeout: typing.Optional[builtins.str] = None,
        search_scope: typing.Optional[builtins.str] = None,
        start_tls: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_registrations: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_password_modify_extended_op: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_truststore_spi: typing.Optional[builtins.str] = None,
        validate_password_policy: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param connection_url: Connection URL to the LDAP server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#connection_url LdapUserFederation#connection_url}
        :param name: Display name of the provider when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#name LdapUserFederation#name}
        :param rdn_ldap_attribute: Name of the LDAP attribute to use as the relative distinguished name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#rdn_ldap_attribute LdapUserFederation#rdn_ldap_attribute}
        :param realm_id: The realm this provider will provide user federation for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#realm_id LdapUserFederation#realm_id}
        :param username_ldap_attribute: Name of the LDAP attribute to use as the Keycloak username. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#username_ldap_attribute LdapUserFederation#username_ldap_attribute}
        :param user_object_classes: All values of LDAP objectClass attribute for users in LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#user_object_classes LdapUserFederation#user_object_classes}
        :param users_dn: Full DN of LDAP tree where your users are. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#users_dn LdapUserFederation#users_dn}
        :param uuid_ldap_attribute: Name of the LDAP attribute to use as a unique object identifier for objects in LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#uuid_ldap_attribute LdapUserFederation#uuid_ldap_attribute}
        :param batch_size_for_sync: The number of users to sync within a single transaction. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#batch_size_for_sync LdapUserFederation#batch_size_for_sync}
        :param bind_credential: Password of LDAP admin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#bind_credential LdapUserFederation#bind_credential}
        :param bind_dn: DN of LDAP admin, which will be used by Keycloak to access LDAP server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#bind_dn LdapUserFederation#bind_dn}
        :param cache: cache block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#cache LdapUserFederation#cache}
        :param changed_sync_period: How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#changed_sync_period LdapUserFederation#changed_sync_period}
        :param connection_timeout: LDAP connection timeout (duration string). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#connection_timeout LdapUserFederation#connection_timeout}
        :param custom_user_search_filter: Additional LDAP filter for filtering searched users. Must begin with '(' and end with ')'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#custom_user_search_filter LdapUserFederation#custom_user_search_filter}
        :param delete_default_mappers: When true, the provider will delete the default mappers which are normally created by Keycloak when creating an LDAP user federation provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#delete_default_mappers LdapUserFederation#delete_default_mappers}
        :param edit_mode: READ_ONLY and WRITABLE are self-explanatory. UNSYNCED allows user data to be imported but not synced back to LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#edit_mode LdapUserFederation#edit_mode}
        :param enabled: When false, this provider will not be used when performing queries for users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#enabled LdapUserFederation#enabled}
        :param full_sync_period: How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#full_sync_period LdapUserFederation#full_sync_period}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#id LdapUserFederation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_enabled: When true, LDAP users will be imported into the Keycloak database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#import_enabled LdapUserFederation#import_enabled}
        :param kerberos: kerberos block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#kerberos LdapUserFederation#kerberos}
        :param pagination: When true, Keycloak assumes the LDAP server supports pagination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#pagination LdapUserFederation#pagination}
        :param priority: Priority of this provider when looking up users. Lower values are first. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#priority LdapUserFederation#priority}
        :param read_timeout: LDAP read timeout (duration string). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#read_timeout LdapUserFederation#read_timeout}
        :param search_scope: ONE_LEVEL: only search for users in the DN specified by user_dn. SUBTREE: search entire LDAP subtree. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#search_scope LdapUserFederation#search_scope}
        :param start_tls: When true, Keycloak will encrypt the connection to LDAP using STARTTLS, which will disable connection pooling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#start_tls LdapUserFederation#start_tls}
        :param sync_registrations: When true, newly created users will be synced back to LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#sync_registrations LdapUserFederation#sync_registrations}
        :param trust_email: If enabled, email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#trust_email LdapUserFederation#trust_email}
        :param use_password_modify_extended_op: When ``true``, use the LDAPv3 Password Modify Extended Operation (RFC-3062). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_password_modify_extended_op LdapUserFederation#use_password_modify_extended_op}
        :param use_truststore_spi: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_truststore_spi LdapUserFederation#use_truststore_spi}.
        :param validate_password_policy: When true, Keycloak will validate passwords using the realm policy before updating it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#validate_password_policy LdapUserFederation#validate_password_policy}
        :param vendor: LDAP vendor. I am almost certain this field does nothing, but the UI indicates that it is required. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#vendor LdapUserFederation#vendor}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cache, dict):
            cache = LdapUserFederationCache(**cache)
        if isinstance(kerberos, dict):
            kerberos = LdapUserFederationKerberos(**kerberos)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__95e3c2e85e31988a66861b150649655e3a3b11f631eb0f64bf90545de93aa049
            )
            check_type(
                argname="argument connection",
                value=connection,
                expected_type=type_hints["connection"],
            )
            check_type(
                argname="argument count", value=count, expected_type=type_hints["count"]
            )
            check_type(
                argname="argument depends_on",
                value=depends_on,
                expected_type=type_hints["depends_on"],
            )
            check_type(
                argname="argument for_each",
                value=for_each,
                expected_type=type_hints["for_each"],
            )
            check_type(
                argname="argument lifecycle",
                value=lifecycle,
                expected_type=type_hints["lifecycle"],
            )
            check_type(
                argname="argument provider",
                value=provider,
                expected_type=type_hints["provider"],
            )
            check_type(
                argname="argument provisioners",
                value=provisioners,
                expected_type=type_hints["provisioners"],
            )
            check_type(
                argname="argument connection_url",
                value=connection_url,
                expected_type=type_hints["connection_url"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument rdn_ldap_attribute",
                value=rdn_ldap_attribute,
                expected_type=type_hints["rdn_ldap_attribute"],
            )
            check_type(
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
            )
            check_type(
                argname="argument username_ldap_attribute",
                value=username_ldap_attribute,
                expected_type=type_hints["username_ldap_attribute"],
            )
            check_type(
                argname="argument user_object_classes",
                value=user_object_classes,
                expected_type=type_hints["user_object_classes"],
            )
            check_type(
                argname="argument users_dn",
                value=users_dn,
                expected_type=type_hints["users_dn"],
            )
            check_type(
                argname="argument uuid_ldap_attribute",
                value=uuid_ldap_attribute,
                expected_type=type_hints["uuid_ldap_attribute"],
            )
            check_type(
                argname="argument batch_size_for_sync",
                value=batch_size_for_sync,
                expected_type=type_hints["batch_size_for_sync"],
            )
            check_type(
                argname="argument bind_credential",
                value=bind_credential,
                expected_type=type_hints["bind_credential"],
            )
            check_type(
                argname="argument bind_dn",
                value=bind_dn,
                expected_type=type_hints["bind_dn"],
            )
            check_type(
                argname="argument cache", value=cache, expected_type=type_hints["cache"]
            )
            check_type(
                argname="argument changed_sync_period",
                value=changed_sync_period,
                expected_type=type_hints["changed_sync_period"],
            )
            check_type(
                argname="argument connection_timeout",
                value=connection_timeout,
                expected_type=type_hints["connection_timeout"],
            )
            check_type(
                argname="argument custom_user_search_filter",
                value=custom_user_search_filter,
                expected_type=type_hints["custom_user_search_filter"],
            )
            check_type(
                argname="argument delete_default_mappers",
                value=delete_default_mappers,
                expected_type=type_hints["delete_default_mappers"],
            )
            check_type(
                argname="argument edit_mode",
                value=edit_mode,
                expected_type=type_hints["edit_mode"],
            )
            check_type(
                argname="argument enabled",
                value=enabled,
                expected_type=type_hints["enabled"],
            )
            check_type(
                argname="argument full_sync_period",
                value=full_sync_period,
                expected_type=type_hints["full_sync_period"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument import_enabled",
                value=import_enabled,
                expected_type=type_hints["import_enabled"],
            )
            check_type(
                argname="argument kerberos",
                value=kerberos,
                expected_type=type_hints["kerberos"],
            )
            check_type(
                argname="argument pagination",
                value=pagination,
                expected_type=type_hints["pagination"],
            )
            check_type(
                argname="argument priority",
                value=priority,
                expected_type=type_hints["priority"],
            )
            check_type(
                argname="argument read_timeout",
                value=read_timeout,
                expected_type=type_hints["read_timeout"],
            )
            check_type(
                argname="argument search_scope",
                value=search_scope,
                expected_type=type_hints["search_scope"],
            )
            check_type(
                argname="argument start_tls",
                value=start_tls,
                expected_type=type_hints["start_tls"],
            )
            check_type(
                argname="argument sync_registrations",
                value=sync_registrations,
                expected_type=type_hints["sync_registrations"],
            )
            check_type(
                argname="argument trust_email",
                value=trust_email,
                expected_type=type_hints["trust_email"],
            )
            check_type(
                argname="argument use_password_modify_extended_op",
                value=use_password_modify_extended_op,
                expected_type=type_hints["use_password_modify_extended_op"],
            )
            check_type(
                argname="argument use_truststore_spi",
                value=use_truststore_spi,
                expected_type=type_hints["use_truststore_spi"],
            )
            check_type(
                argname="argument validate_password_policy",
                value=validate_password_policy,
                expected_type=type_hints["validate_password_policy"],
            )
            check_type(
                argname="argument vendor",
                value=vendor,
                expected_type=type_hints["vendor"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_url": connection_url,
            "name": name,
            "rdn_ldap_attribute": rdn_ldap_attribute,
            "realm_id": realm_id,
            "username_ldap_attribute": username_ldap_attribute,
            "user_object_classes": user_object_classes,
            "users_dn": users_dn,
            "uuid_ldap_attribute": uuid_ldap_attribute,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if batch_size_for_sync is not None:
            self._values["batch_size_for_sync"] = batch_size_for_sync
        if bind_credential is not None:
            self._values["bind_credential"] = bind_credential
        if bind_dn is not None:
            self._values["bind_dn"] = bind_dn
        if cache is not None:
            self._values["cache"] = cache
        if changed_sync_period is not None:
            self._values["changed_sync_period"] = changed_sync_period
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_user_search_filter is not None:
            self._values["custom_user_search_filter"] = custom_user_search_filter
        if delete_default_mappers is not None:
            self._values["delete_default_mappers"] = delete_default_mappers
        if edit_mode is not None:
            self._values["edit_mode"] = edit_mode
        if enabled is not None:
            self._values["enabled"] = enabled
        if full_sync_period is not None:
            self._values["full_sync_period"] = full_sync_period
        if id is not None:
            self._values["id"] = id
        if import_enabled is not None:
            self._values["import_enabled"] = import_enabled
        if kerberos is not None:
            self._values["kerberos"] = kerberos
        if pagination is not None:
            self._values["pagination"] = pagination
        if priority is not None:
            self._values["priority"] = priority
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout
        if search_scope is not None:
            self._values["search_scope"] = search_scope
        if start_tls is not None:
            self._values["start_tls"] = start_tls
        if sync_registrations is not None:
            self._values["sync_registrations"] = sync_registrations
        if trust_email is not None:
            self._values["trust_email"] = trust_email
        if use_password_modify_extended_op is not None:
            self._values[
                "use_password_modify_extended_op"
            ] = use_password_modify_extended_op
        if use_truststore_spi is not None:
            self._values["use_truststore_spi"] = use_truststore_spi
        if validate_password_policy is not None:
            self._values["validate_password_policy"] = validate_password_policy
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.SSHProvisionerConnection,
            _cdktf_9a9027ec.WinrmProvisionerConnection,
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("connection")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                ]
            ],
            result,
        )

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        """
        :stability: experimental
        """
        result = self._values.get("count")
        return typing.cast(
            typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]],
            result,
        )

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        """
        :stability: experimental
        """
        result = self._values.get("depends_on")
        return typing.cast(
            typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result
        )

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        """
        :stability: experimental
        """
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        """
        :stability: experimental
        """
        result = self._values.get("lifecycle")
        return typing.cast(
            typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result
        )

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        """
        :stability: experimental
        """
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[
        typing.List[
            typing.Union[
                _cdktf_9a9027ec.FileProvisioner,
                _cdktf_9a9027ec.LocalExecProvisioner,
                _cdktf_9a9027ec.RemoteExecProvisioner,
            ]
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("provisioners")
        return typing.cast(
            typing.Optional[
                typing.List[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                    ]
                ]
            ],
            result,
        )

    @builtins.property
    def connection_url(self) -> builtins.str:
        """Connection URL to the LDAP server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#connection_url LdapUserFederation#connection_url}
        """
        result = self._values.get("connection_url")
        assert result is not None, "Required property 'connection_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Display name of the provider when displayed in the console.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#name LdapUserFederation#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rdn_ldap_attribute(self) -> builtins.str:
        """Name of the LDAP attribute to use as the relative distinguished name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#rdn_ldap_attribute LdapUserFederation#rdn_ldap_attribute}
        """
        result = self._values.get("rdn_ldap_attribute")
        assert result is not None, "Required property 'rdn_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """The realm this provider will provide user federation for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#realm_id LdapUserFederation#realm_id}
        """
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username_ldap_attribute(self) -> builtins.str:
        """Name of the LDAP attribute to use as the Keycloak username.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#username_ldap_attribute LdapUserFederation#username_ldap_attribute}
        """
        result = self._values.get("username_ldap_attribute")
        assert (
            result is not None
        ), "Required property 'username_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_object_classes(self) -> typing.List[builtins.str]:
        """All values of LDAP objectClass attribute for users in LDAP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#user_object_classes LdapUserFederation#user_object_classes}
        """
        result = self._values.get("user_object_classes")
        assert result is not None, "Required property 'user_object_classes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def users_dn(self) -> builtins.str:
        """Full DN of LDAP tree where your users are.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#users_dn LdapUserFederation#users_dn}
        """
        result = self._values.get("users_dn")
        assert result is not None, "Required property 'users_dn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uuid_ldap_attribute(self) -> builtins.str:
        """Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#uuid_ldap_attribute LdapUserFederation#uuid_ldap_attribute}
        """
        result = self._values.get("uuid_ldap_attribute")
        assert result is not None, "Required property 'uuid_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_size_for_sync(self) -> typing.Optional[jsii.Number]:
        """The number of users to sync within a single transaction.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#batch_size_for_sync LdapUserFederation#batch_size_for_sync}
        """
        result = self._values.get("batch_size_for_sync")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bind_credential(self) -> typing.Optional[builtins.str]:
        """Password of LDAP admin.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#bind_credential LdapUserFederation#bind_credential}
        """
        result = self._values.get("bind_credential")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bind_dn(self) -> typing.Optional[builtins.str]:
        """DN of LDAP admin, which will be used by Keycloak to access LDAP server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#bind_dn LdapUserFederation#bind_dn}
        """
        result = self._values.get("bind_dn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache(self) -> typing.Optional[LdapUserFederationCache]:
        """cache block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#cache LdapUserFederation#cache}
        """
        result = self._values.get("cache")
        return typing.cast(typing.Optional[LdapUserFederationCache], result)

    @builtins.property
    def changed_sync_period(self) -> typing.Optional[jsii.Number]:
        """How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users sync.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#changed_sync_period LdapUserFederation#changed_sync_period}
        """
        result = self._values.get("changed_sync_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[builtins.str]:
        """LDAP connection timeout (duration string).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#connection_timeout LdapUserFederation#connection_timeout}
        """
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_user_search_filter(self) -> typing.Optional[builtins.str]:
        """Additional LDAP filter for filtering searched users. Must begin with '(' and end with ')'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#custom_user_search_filter LdapUserFederation#custom_user_search_filter}
        """
        result = self._values.get("custom_user_search_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_default_mappers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, the provider will delete the default mappers which are normally created by Keycloak when creating an LDAP user federation provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#delete_default_mappers LdapUserFederation#delete_default_mappers}
        """
        result = self._values.get("delete_default_mappers")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def edit_mode(self) -> typing.Optional[builtins.str]:
        """READ_ONLY and WRITABLE are self-explanatory. UNSYNCED allows user data to be imported but not synced back to LDAP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#edit_mode LdapUserFederation#edit_mode}
        """
        result = self._values.get("edit_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When false, this provider will not be used when performing queries for users.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#enabled LdapUserFederation#enabled}
        """
        result = self._values.get("enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def full_sync_period(self) -> typing.Optional[jsii.Number]:
        """How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#full_sync_period LdapUserFederation#full_sync_period}
        """
        result = self._values.get("full_sync_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#id LdapUserFederation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, LDAP users will be imported into the Keycloak database.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#import_enabled LdapUserFederation#import_enabled}
        """
        result = self._values.get("import_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def kerberos(self) -> typing.Optional["LdapUserFederationKerberos"]:
        """kerberos block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#kerberos LdapUserFederation#kerberos}
        """
        result = self._values.get("kerberos")
        return typing.cast(typing.Optional["LdapUserFederationKerberos"], result)

    @builtins.property
    def pagination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, Keycloak assumes the LDAP server supports pagination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#pagination LdapUserFederation#pagination}
        """
        result = self._values.get("pagination")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        """Priority of this provider when looking up users. Lower values are first.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#priority LdapUserFederation#priority}
        """
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[builtins.str]:
        """LDAP read timeout (duration string).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#read_timeout LdapUserFederation#read_timeout}
        """
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_scope(self) -> typing.Optional[builtins.str]:
        """ONE_LEVEL: only search for users in the DN specified by user_dn. SUBTREE: search entire LDAP subtree.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#search_scope LdapUserFederation#search_scope}
        """
        result = self._values.get("search_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, Keycloak will encrypt the connection to LDAP using STARTTLS, which will disable connection pooling.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#start_tls LdapUserFederation#start_tls}
        """
        result = self._values.get("start_tls")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def sync_registrations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, newly created users will be synced back to LDAP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#sync_registrations LdapUserFederation#sync_registrations}
        """
        result = self._values.get("sync_registrations")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def trust_email(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """If enabled, email provided by this provider is not verified even if verification is enabled for the realm.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#trust_email LdapUserFederation#trust_email}
        """
        result = self._values.get("trust_email")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def use_password_modify_extended_op(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When ``true``, use the LDAPv3 Password Modify Extended Operation (RFC-3062).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_password_modify_extended_op LdapUserFederation#use_password_modify_extended_op}
        """
        result = self._values.get("use_password_modify_extended_op")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def use_truststore_spi(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_truststore_spi LdapUserFederation#use_truststore_spi}."""
        result = self._values.get("use_truststore_spi")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validate_password_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, Keycloak will validate passwords using the realm policy before updating it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#validate_password_policy LdapUserFederation#validate_password_policy}
        """
        result = self._values.get("validate_password_policy")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        """LDAP vendor. I am almost certain this field does nothing, but the UI indicates that it is required.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#vendor LdapUserFederation#vendor}
        """
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LdapUserFederationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.ldapUserFederation.LdapUserFederationKerberos",
    jsii_struct_bases=[],
    name_mapping={
        "kerberos_realm": "kerberosRealm",
        "key_tab": "keyTab",
        "server_principal": "serverPrincipal",
        "use_kerberos_for_password_authentication": "useKerberosForPasswordAuthentication",
    },
)
class LdapUserFederationKerberos:
    def __init__(
        self,
        *,
        kerberos_realm: builtins.str,
        key_tab: builtins.str,
        server_principal: builtins.str,
        use_kerberos_for_password_authentication: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param kerberos_realm: The name of the kerberos realm, e.g. FOO.LOCAL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#kerberos_realm LdapUserFederation#kerberos_realm}
        :param key_tab: Path to the kerberos keytab file on the server with credentials of the service principal. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#key_tab LdapUserFederation#key_tab}
        :param server_principal: The kerberos server principal, e.g. 'HTTP/host.foo.com@FOO.LOCAL'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#server_principal LdapUserFederation#server_principal}
        :param use_kerberos_for_password_authentication: Use kerberos login module instead of ldap service api. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_kerberos_for_password_authentication LdapUserFederation#use_kerberos_for_password_authentication}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8fbb3d7373aa215bcf9887eecfcaf9ac99f06bb83197bfa6ffc459c253790a2b
            )
            check_type(
                argname="argument kerberos_realm",
                value=kerberos_realm,
                expected_type=type_hints["kerberos_realm"],
            )
            check_type(
                argname="argument key_tab",
                value=key_tab,
                expected_type=type_hints["key_tab"],
            )
            check_type(
                argname="argument server_principal",
                value=server_principal,
                expected_type=type_hints["server_principal"],
            )
            check_type(
                argname="argument use_kerberos_for_password_authentication",
                value=use_kerberos_for_password_authentication,
                expected_type=type_hints["use_kerberos_for_password_authentication"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kerberos_realm": kerberos_realm,
            "key_tab": key_tab,
            "server_principal": server_principal,
        }
        if use_kerberos_for_password_authentication is not None:
            self._values[
                "use_kerberos_for_password_authentication"
            ] = use_kerberos_for_password_authentication

    @builtins.property
    def kerberos_realm(self) -> builtins.str:
        """The name of the kerberos realm, e.g. FOO.LOCAL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#kerberos_realm LdapUserFederation#kerberos_realm}
        """
        result = self._values.get("kerberos_realm")
        assert result is not None, "Required property 'kerberos_realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_tab(self) -> builtins.str:
        """Path to the kerberos keytab file on the server with credentials of the service principal.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#key_tab LdapUserFederation#key_tab}
        """
        result = self._values.get("key_tab")
        assert result is not None, "Required property 'key_tab' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_principal(self) -> builtins.str:
        """The kerberos server principal, e.g. 'HTTP/host.foo.com@FOO.LOCAL'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#server_principal LdapUserFederation#server_principal}
        """
        result = self._values.get("server_principal")
        assert result is not None, "Required property 'server_principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_kerberos_for_password_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Use kerberos login module instead of ldap service api. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_federation#use_kerberos_for_password_authentication LdapUserFederation#use_kerberos_for_password_authentication}
        """
        result = self._values.get("use_kerberos_for_password_authentication")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LdapUserFederationKerberos(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LdapUserFederationKerberosOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.ldapUserFederation.LdapUserFederationKerberosOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4c0b4b234f115cf72c151e77efa921b91fd491b609dafa25994d9a4981d12fa0
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUseKerberosForPasswordAuthentication")
    def reset_use_kerberos_for_password_authentication(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetUseKerberosForPasswordAuthentication", [])
        )

    @builtins.property
    @jsii.member(jsii_name="kerberosRealmInput")
    def kerberos_realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "kerberosRealmInput")
        )

    @builtins.property
    @jsii.member(jsii_name="keyTabInput")
    def key_tab_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTabInput"))

    @builtins.property
    @jsii.member(jsii_name="serverPrincipalInput")
    def server_principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "serverPrincipalInput")
        )

    @builtins.property
    @jsii.member(jsii_name="useKerberosForPasswordAuthenticationInput")
    def use_kerberos_for_password_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "useKerberosForPasswordAuthenticationInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="kerberosRealm")
    def kerberos_realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kerberosRealm"))

    @kerberos_realm.setter
    def kerberos_realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5810b27c5324183b94e4688e23eaa22a182902a2b6e0fe029fac305404ddabfc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "kerberosRealm", value)

    @builtins.property
    @jsii.member(jsii_name="keyTab")
    def key_tab(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyTab"))

    @key_tab.setter
    def key_tab(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__59b679882d7aeac8bd3dba9bfcb002683e3658081f9a741be8df7b9420e5d89f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "keyTab", value)

    @builtins.property
    @jsii.member(jsii_name="serverPrincipal")
    def server_principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverPrincipal"))

    @server_principal.setter
    def server_principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ee786b2a5309dee394e9461b7ede7f3a02d3599571bc6d18ebcfbccef5ce7b4f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "serverPrincipal", value)

    @builtins.property
    @jsii.member(jsii_name="useKerberosForPasswordAuthentication")
    def use_kerberos_for_password_authentication(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "useKerberosForPasswordAuthentication"),
        )

    @use_kerberos_for_password_authentication.setter
    def use_kerberos_for_password_authentication(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b159955a49f3dfa0d108534c96bc0c21a787714b7092828f71f4d034e5d8f055
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "useKerberosForPasswordAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LdapUserFederationKerberos]:
        return typing.cast(
            typing.Optional[LdapUserFederationKerberos], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LdapUserFederationKerberos],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b5f827c9d4a12d45eb0451e877818a430f20269b7fe183f04cd297effbbd17a8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "LdapUserFederation",
    "LdapUserFederationCache",
    "LdapUserFederationCacheOutputReference",
    "LdapUserFederationConfig",
    "LdapUserFederationKerberos",
    "LdapUserFederationKerberosOutputReference",
]

publication.publish()


def _typecheckingstub__4d9ec54577e521031be59ee398adfbb4988c8ea336dface5be90385316251633(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    connection_url: builtins.str,
    name: builtins.str,
    rdn_ldap_attribute: builtins.str,
    realm_id: builtins.str,
    username_ldap_attribute: builtins.str,
    user_object_classes: typing.Sequence[builtins.str],
    users_dn: builtins.str,
    uuid_ldap_attribute: builtins.str,
    batch_size_for_sync: typing.Optional[jsii.Number] = None,
    bind_credential: typing.Optional[builtins.str] = None,
    bind_dn: typing.Optional[builtins.str] = None,
    cache: typing.Optional[
        typing.Union[LdapUserFederationCache, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    changed_sync_period: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[builtins.str] = None,
    custom_user_search_filter: typing.Optional[builtins.str] = None,
    delete_default_mappers: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    edit_mode: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    full_sync_period: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    import_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    kerberos: typing.Optional[
        typing.Union[LdapUserFederationKerberos, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    pagination: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    priority: typing.Optional[jsii.Number] = None,
    read_timeout: typing.Optional[builtins.str] = None,
    search_scope: typing.Optional[builtins.str] = None,
    start_tls: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_registrations: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_password_modify_extended_op: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_truststore_spi: typing.Optional[builtins.str] = None,
    validate_password_policy: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    vendor: typing.Optional[builtins.str] = None,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c2b80f7895ce3a83ab330399171ab2a0ee2069cc997be70723ea9233d0436b48(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f30436108c467f348d50385f3eaa93b3d30a0cf681544d8b3b4b1f272f531de3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b668caf05c5d29897f5425799cba8319a0d09dab89bb53e2d3095685b82a695f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7949b87c7ebb1c2f61d3b9c09f4c01cf671a6a0dcabf5203c9ccb2bedeec86b3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c1b06d14ae9a708fe0160fcd5f93e2bef322c4fb3be63a4821959fb9c8331720(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__45bb298e07f837bf93328bafd0e5d49722f75dc0d793f0b3598d694cae1ab393(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b70aecd2e4751d75e50364477ed76230ed760a9d36a453a0fe4831d3c61e9d42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ddfcea9e2f161f1937b8e31b3c342b2f4f85901db359632d1211d124ac52dc02(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b3383c048e2d6a41b53458e3c9e440a1b75add65b1ed1c8adaa73a65747ded75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__da261c7843c9bba96bc970b5d71d3528e68c3bba66ec75d10d1f9a04df10bca8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__926ed29780ebcf0785e1610f8c55cc597c6d678d7faa782f4177e93791de97db(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__34ed1d55ff0effe9108873f45d0e15666e8aaa87bd39d498b8c255ec741c4d78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__68869993e30e12257a152c0713d4d96a32b96a9d849ab0fbe39b599580d1c793(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0738e96714242e00f769af0fc6a18b9988ff76ddcb51db2ec66613fe03ed67e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a7f73b5fa78f4d0f84000328dbd2da2ec3714f728e36ec8520a708ec8976e200(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5971d72054917d3fdf04bcb568064e73509f467c25e2ea2d49420003c1924d73(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__694089ff3a7920e321a5b47357603747883700e6342ee73f10f7691ffc412bc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__86ce6fc2bb57dfacbba3e2d58b3b1beca013f13e290fea7c04851696198f5fea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1348006e07dfdc85704e537f24cfc0b4988e70b81e9f1b0a7b3b9b6c3effa6e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c2312348236931bd014f254e21b7748add18d87cfe8c06844d6bb98acb62f721(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7a073182d3c07ffb97ac1951fb56da9eee6b2d85516b6cdc3bc27cc64c90846f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a4ce81fb1cb11fb3a8e7ea638dbb404503e0a23327687c97f2086e54440684eb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2f84e390d542abade19db6c6a1424a8b3720b3abbec81d029934c92a411f52a3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__61ca871a07efcda8899b1528d4484ebda7fe5769d72a11f833a244df4488aa2d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2da999742cabaec8153305cc856cb786e52f772baf27f99c0c34b845c5d625b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e9834c3ba47b8f6a4a8ad7cb09e5277c89e75f27643f2d12fa66325878f79ba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__be173eb2a41e9514f015da2255c70da787a6d8d6cff6da303b5ce28f5870092b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__714470d46ff59bd14339df1401cadaf220b548c4523e8a30d4f3182780e8516d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__26a434ac7a4f5f4b12f738558c6f6248086717a259738545ea79d8b1698ec113(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f459fda8bcba872a66f582b02d635e3e4837748b102eadeaa1dc819d4d551e97(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__72267cc4157d6a78378ecfe5ca5fcd0e397ebbf753e496fb39bf24b316b071d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3bcaffd363bb3d22326184cf1828eb2131664d9d1c3985c03ced2eeb950afbe0(
    *,
    eviction_day: typing.Optional[jsii.Number] = None,
    eviction_hour: typing.Optional[jsii.Number] = None,
    eviction_minute: typing.Optional[jsii.Number] = None,
    max_lifespan: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b51a005647b5b81bbd4c794406ecc3cdb083e3c04d04807bbfa24fc0cb8db201(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__50c23fc36902aba4b8a09d6eb2398f9c58febc929a65c9ef75b4b5d208e558e7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a7e9d434537138565eb2605195f2af9ee069f05fa2024dc6b9cd25420f970f96(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c3c4f62cba0cdcee6efad987c922df7b7e7bf3ddcde72a1eac2bbfde412a6385(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a6afd8b19e5b36540d564113f6958fd0b482ffc4ab1219f78fd45df4f0020640(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cb16078bd64add9bd1d05d3d0109e2d4911349332d95293796a2b1ca860b061b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0b1345d040460360f56be2dae2f887ca8a89a48ba9b81e7c12c87701ed530350(
    value: typing.Optional[LdapUserFederationCache],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__95e3c2e85e31988a66861b150649655e3a3b11f631eb0f64bf90545de93aa049(
    *,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
    connection_url: builtins.str,
    name: builtins.str,
    rdn_ldap_attribute: builtins.str,
    realm_id: builtins.str,
    username_ldap_attribute: builtins.str,
    user_object_classes: typing.Sequence[builtins.str],
    users_dn: builtins.str,
    uuid_ldap_attribute: builtins.str,
    batch_size_for_sync: typing.Optional[jsii.Number] = None,
    bind_credential: typing.Optional[builtins.str] = None,
    bind_dn: typing.Optional[builtins.str] = None,
    cache: typing.Optional[
        typing.Union[LdapUserFederationCache, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    changed_sync_period: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[builtins.str] = None,
    custom_user_search_filter: typing.Optional[builtins.str] = None,
    delete_default_mappers: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    edit_mode: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    full_sync_period: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    import_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    kerberos: typing.Optional[
        typing.Union[LdapUserFederationKerberos, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    pagination: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    priority: typing.Optional[jsii.Number] = None,
    read_timeout: typing.Optional[builtins.str] = None,
    search_scope: typing.Optional[builtins.str] = None,
    start_tls: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_registrations: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_password_modify_extended_op: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_truststore_spi: typing.Optional[builtins.str] = None,
    validate_password_policy: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    vendor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8fbb3d7373aa215bcf9887eecfcaf9ac99f06bb83197bfa6ffc459c253790a2b(
    *,
    kerberos_realm: builtins.str,
    key_tab: builtins.str,
    server_principal: builtins.str,
    use_kerberos_for_password_authentication: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4c0b4b234f115cf72c151e77efa921b91fd491b609dafa25994d9a4981d12fa0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5810b27c5324183b94e4688e23eaa22a182902a2b6e0fe029fac305404ddabfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__59b679882d7aeac8bd3dba9bfcb002683e3658081f9a741be8df7b9420e5d89f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ee786b2a5309dee394e9461b7ede7f3a02d3599571bc6d18ebcfbccef5ce7b4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b159955a49f3dfa0d108534c96bc0c21a787714b7092828f71f4d034e5d8f055(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b5f827c9d4a12d45eb0451e877818a430f20269b7fe183f04cd297effbbd17a8(
    value: typing.Optional[LdapUserFederationKerberos],
) -> None:
    """Type checking stubs"""
    pass

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

__all__ = [
    "accessanalyzer_analyzer",
    "accessanalyzer_archive_rule",
    "account_alternate_contact",
    "acm_certificate",
    "acm_certificate_validation",
    "acmpca_certificate",
    "acmpca_certificate_authority",
    "acmpca_certificate_authority_certificate",
    "acmpca_permission",
    "acmpca_policy",
    "alb",
    "alb_listener",
    "alb_listener_certificate",
    "alb_listener_rule",
    "alb_target_group",
    "alb_target_group_attachment",
    "ami",
    "ami_copy",
    "ami_from_instance",
    "ami_launch_permission",
    "amplify_app",
    "amplify_backend_environment",
    "amplify_branch",
    "amplify_domain_association",
    "amplify_webhook",
    "api_gateway_account",
    "api_gateway_api_key",
    "api_gateway_authorizer",
    "api_gateway_base_path_mapping",
    "api_gateway_client_certificate",
    "api_gateway_deployment",
    "api_gateway_documentation_part",
    "api_gateway_documentation_version",
    "api_gateway_domain_name",
    "api_gateway_gateway_response",
    "api_gateway_integration",
    "api_gateway_integration_response",
    "api_gateway_method",
    "api_gateway_method_response",
    "api_gateway_method_settings",
    "api_gateway_model",
    "api_gateway_request_validator",
    "api_gateway_resource",
    "api_gateway_rest_api",
    "api_gateway_rest_api_policy",
    "api_gateway_stage",
    "api_gateway_usage_plan",
    "api_gateway_usage_plan_key",
    "api_gateway_vpc_link",
    "apigatewayv2_api",
    "apigatewayv2_api_mapping",
    "apigatewayv2_authorizer",
    "apigatewayv2_deployment",
    "apigatewayv2_domain_name",
    "apigatewayv2_integration",
    "apigatewayv2_integration_response",
    "apigatewayv2_model",
    "apigatewayv2_route",
    "apigatewayv2_route_response",
    "apigatewayv2_stage",
    "apigatewayv2_vpc_link",
    "app_cookie_stickiness_policy",
    "appautoscaling_policy",
    "appautoscaling_scheduled_action",
    "appautoscaling_target",
    "appconfig_application",
    "appconfig_configuration_profile",
    "appconfig_deployment",
    "appconfig_deployment_strategy",
    "appconfig_environment",
    "appconfig_extension",
    "appconfig_extension_association",
    "appconfig_hosted_configuration_version",
    "appflow_connector_profile",
    "appflow_flow",
    "appintegrations_event_integration",
    "applicationinsights_application",
    "appmesh_gateway_route",
    "appmesh_mesh",
    "appmesh_route",
    "appmesh_virtual_gateway",
    "appmesh_virtual_node",
    "appmesh_virtual_router",
    "appmesh_virtual_service",
    "apprunner_auto_scaling_configuration_version",
    "apprunner_connection",
    "apprunner_custom_domain_association",
    "apprunner_observability_configuration",
    "apprunner_service",
    "apprunner_vpc_connector",
    "apprunner_vpc_ingress_connection",
    "appstream_directory_config",
    "appstream_fleet",
    "appstream_fleet_stack_association",
    "appstream_image_builder",
    "appstream_stack",
    "appstream_user",
    "appstream_user_stack_association",
    "appsync_api_cache",
    "appsync_api_key",
    "appsync_datasource",
    "appsync_domain_name",
    "appsync_domain_name_api_association",
    "appsync_function",
    "appsync_graphql_api",
    "appsync_resolver",
    "appsync_type",
    "athena_data_catalog",
    "athena_database",
    "athena_named_query",
    "athena_workgroup",
    "auditmanager_account_registration",
    "auditmanager_assessment",
    "auditmanager_assessment_report",
    "auditmanager_control",
    "auditmanager_framework",
    "autoscaling_attachment",
    "autoscaling_group",
    "autoscaling_group_tag",
    "autoscaling_lifecycle_hook",
    "autoscaling_notification",
    "autoscaling_policy",
    "autoscaling_schedule",
    "autoscalingplans_scaling_plan",
    "backup_framework",
    "backup_global_settings",
    "backup_plan",
    "backup_region_settings",
    "backup_report_plan",
    "backup_selection",
    "backup_vault",
    "backup_vault_lock_configuration",
    "backup_vault_notifications",
    "backup_vault_policy",
    "batch_compute_environment",
    "batch_job_definition",
    "batch_job_queue",
    "batch_scheduling_policy",
    "budgets_budget",
    "budgets_budget_action",
    "ce_anomaly_monitor",
    "ce_anomaly_subscription",
    "ce_cost_allocation_tag",
    "ce_cost_category",
    "chime_voice_connector",
    "chime_voice_connector_group",
    "chime_voice_connector_logging",
    "chime_voice_connector_origination",
    "chime_voice_connector_streaming",
    "chime_voice_connector_termination",
    "chime_voice_connector_termination_credentials",
    "cloud9_environment_ec2",
    "cloud9_environment_membership",
    "cloudcontrolapi_resource",
    "cloudformation_stack",
    "cloudformation_stack_set",
    "cloudformation_stack_set_instance",
    "cloudformation_type",
    "cloudfront_cache_policy",
    "cloudfront_distribution",
    "cloudfront_field_level_encryption_config",
    "cloudfront_field_level_encryption_profile",
    "cloudfront_function",
    "cloudfront_key_group",
    "cloudfront_monitoring_subscription",
    "cloudfront_origin_access_control",
    "cloudfront_origin_access_identity",
    "cloudfront_origin_request_policy",
    "cloudfront_public_key",
    "cloudfront_realtime_log_config",
    "cloudfront_response_headers_policy",
    "cloudhsm_v2_cluster",
    "cloudhsm_v2_hsm",
    "cloudsearch_domain",
    "cloudsearch_domain_service_access_policy",
    "cloudtrail",
    "cloudtrail_event_data_store",
    "cloudwatch_composite_alarm",
    "cloudwatch_dashboard",
    "cloudwatch_event_api_destination",
    "cloudwatch_event_archive",
    "cloudwatch_event_bus",
    "cloudwatch_event_bus_policy",
    "cloudwatch_event_connection",
    "cloudwatch_event_permission",
    "cloudwatch_event_rule",
    "cloudwatch_event_target",
    "cloudwatch_log_data_protection_policy",
    "cloudwatch_log_destination",
    "cloudwatch_log_destination_policy",
    "cloudwatch_log_group",
    "cloudwatch_log_metric_filter",
    "cloudwatch_log_resource_policy",
    "cloudwatch_log_stream",
    "cloudwatch_log_subscription_filter",
    "cloudwatch_metric_alarm",
    "cloudwatch_metric_stream",
    "cloudwatch_query_definition",
    "codeartifact_domain",
    "codeartifact_domain_permissions_policy",
    "codeartifact_repository",
    "codeartifact_repository_permissions_policy",
    "codebuild_project",
    "codebuild_report_group",
    "codebuild_resource_policy",
    "codebuild_source_credential",
    "codebuild_webhook",
    "codecommit_approval_rule_template",
    "codecommit_approval_rule_template_association",
    "codecommit_repository",
    "codecommit_trigger",
    "codedeploy_app",
    "codedeploy_deployment_config",
    "codedeploy_deployment_group",
    "codepipeline",
    "codepipeline_custom_action_type",
    "codepipeline_webhook",
    "codestarconnections_connection",
    "codestarconnections_host",
    "codestarnotifications_notification_rule",
    "cognito_identity_pool",
    "cognito_identity_pool_provider_principal_tag",
    "cognito_identity_pool_roles_attachment",
    "cognito_identity_provider",
    "cognito_resource_server",
    "cognito_risk_configuration",
    "cognito_user",
    "cognito_user_group",
    "cognito_user_in_group",
    "cognito_user_pool",
    "cognito_user_pool_client",
    "cognito_user_pool_domain",
    "cognito_user_pool_ui_customization",
    "comprehend_document_classifier",
    "comprehend_entity_recognizer",
    "config_aggregate_authorization",
    "config_config_rule",
    "config_configuration_aggregator",
    "config_configuration_recorder",
    "config_configuration_recorder_status",
    "config_conformance_pack",
    "config_delivery_channel",
    "config_organization_conformance_pack",
    "config_organization_custom_rule",
    "config_organization_managed_rule",
    "config_remediation_configuration",
    "connect_bot_association",
    "connect_contact_flow",
    "connect_contact_flow_module",
    "connect_hours_of_operation",
    "connect_instance",
    "connect_instance_storage_config",
    "connect_lambda_function_association",
    "connect_phone_number",
    "connect_queue",
    "connect_quick_connect",
    "connect_routing_profile",
    "connect_security_profile",
    "connect_user",
    "connect_user_hierarchy_group",
    "connect_user_hierarchy_structure",
    "connect_vocabulary",
    "controltower_control",
    "cur_report_definition",
    "customer_gateway",
    "data_aws_acm_certificate",
    "data_aws_acmpca_certificate",
    "data_aws_acmpca_certificate_authority",
    "data_aws_alb",
    "data_aws_alb_listener",
    "data_aws_alb_target_group",
    "data_aws_ami",
    "data_aws_ami_ids",
    "data_aws_api_gateway_api_key",
    "data_aws_api_gateway_domain_name",
    "data_aws_api_gateway_export",
    "data_aws_api_gateway_resource",
    "data_aws_api_gateway_rest_api",
    "data_aws_api_gateway_sdk",
    "data_aws_api_gateway_vpc_link",
    "data_aws_apigatewayv2_api",
    "data_aws_apigatewayv2_apis",
    "data_aws_apigatewayv2_export",
    "data_aws_appconfig_configuration_profile",
    "data_aws_appconfig_configuration_profiles",
    "data_aws_appconfig_environment",
    "data_aws_appconfig_environments",
    "data_aws_appmesh_mesh",
    "data_aws_appmesh_virtual_service",
    "data_aws_arn",
    "data_aws_autoscaling_group",
    "data_aws_autoscaling_groups",
    "data_aws_availability_zone",
    "data_aws_availability_zones",
    "data_aws_backup_framework",
    "data_aws_backup_plan",
    "data_aws_backup_report_plan",
    "data_aws_backup_selection",
    "data_aws_backup_vault",
    "data_aws_batch_compute_environment",
    "data_aws_batch_job_queue",
    "data_aws_batch_scheduling_policy",
    "data_aws_billing_service_account",
    "data_aws_caller_identity",
    "data_aws_canonical_user_id",
    "data_aws_ce_cost_category",
    "data_aws_ce_tags",
    "data_aws_cloudcontrolapi_resource",
    "data_aws_cloudformation_export",
    "data_aws_cloudformation_stack",
    "data_aws_cloudformation_type",
    "data_aws_cloudfront_cache_policy",
    "data_aws_cloudfront_distribution",
    "data_aws_cloudfront_function",
    "data_aws_cloudfront_log_delivery_canonical_user_id",
    "data_aws_cloudfront_origin_access_identities",
    "data_aws_cloudfront_origin_access_identity",
    "data_aws_cloudfront_origin_request_policy",
    "data_aws_cloudfront_realtime_log_config",
    "data_aws_cloudfront_response_headers_policy",
    "data_aws_cloudhsm_v2_cluster",
    "data_aws_cloudtrail_service_account",
    "data_aws_cloudwatch_event_bus",
    "data_aws_cloudwatch_event_connection",
    "data_aws_cloudwatch_event_source",
    "data_aws_cloudwatch_log_data_protection_policy_document",
    "data_aws_cloudwatch_log_group",
    "data_aws_cloudwatch_log_groups",
    "data_aws_codeartifact_authorization_token",
    "data_aws_codeartifact_repository_endpoint",
    "data_aws_codecommit_approval_rule_template",
    "data_aws_codecommit_repository",
    "data_aws_codestarconnections_connection",
    "data_aws_cognito_user_pool_client",
    "data_aws_cognito_user_pool_clients",
    "data_aws_cognito_user_pool_signing_certificate",
    "data_aws_cognito_user_pools",
    "data_aws_connect_bot_association",
    "data_aws_connect_contact_flow",
    "data_aws_connect_contact_flow_module",
    "data_aws_connect_hours_of_operation",
    "data_aws_connect_instance",
    "data_aws_connect_instance_storage_config",
    "data_aws_connect_lambda_function_association",
    "data_aws_connect_prompt",
    "data_aws_connect_queue",
    "data_aws_connect_quick_connect",
    "data_aws_connect_routing_profile",
    "data_aws_connect_security_profile",
    "data_aws_connect_user_hierarchy_group",
    "data_aws_connect_user_hierarchy_structure",
    "data_aws_controltower_controls",
    "data_aws_cur_report_definition",
    "data_aws_customer_gateway",
    "data_aws_datapipeline_pipeline",
    "data_aws_datapipeline_pipeline_definition",
    "data_aws_db_cluster_snapshot",
    "data_aws_db_event_categories",
    "data_aws_db_instance",
    "data_aws_db_instances",
    "data_aws_db_proxy",
    "data_aws_db_snapshot",
    "data_aws_db_subnet_group",
    "data_aws_default_tags",
    "data_aws_directory_service_directory",
    "data_aws_docdb_engine_version",
    "data_aws_docdb_orderable_db_instance",
    "data_aws_dx_connection",
    "data_aws_dx_gateway",
    "data_aws_dx_location",
    "data_aws_dx_locations",
    "data_aws_dx_router_configuration",
    "data_aws_dynamodb_table",
    "data_aws_dynamodb_table_item",
    "data_aws_ebs_default_kms_key",
    "data_aws_ebs_encryption_by_default",
    "data_aws_ebs_snapshot",
    "data_aws_ebs_snapshot_ids",
    "data_aws_ebs_volume",
    "data_aws_ebs_volumes",
    "data_aws_ec2_client_vpn_endpoint",
    "data_aws_ec2_coip_pool",
    "data_aws_ec2_coip_pools",
    "data_aws_ec2_host",
    "data_aws_ec2_instance_type",
    "data_aws_ec2_instance_type_offering",
    "data_aws_ec2_instance_type_offerings",
    "data_aws_ec2_instance_types",
    "data_aws_ec2_local_gateway",
    "data_aws_ec2_local_gateway_route_table",
    "data_aws_ec2_local_gateway_route_tables",
    "data_aws_ec2_local_gateway_virtual_interface",
    "data_aws_ec2_local_gateway_virtual_interface_group",
    "data_aws_ec2_local_gateway_virtual_interface_groups",
    "data_aws_ec2_local_gateways",
    "data_aws_ec2_managed_prefix_list",
    "data_aws_ec2_managed_prefix_lists",
    "data_aws_ec2_network_insights_analysis",
    "data_aws_ec2_network_insights_path",
    "data_aws_ec2_serial_console_access",
    "data_aws_ec2_spot_price",
    "data_aws_ec2_transit_gateway",
    "data_aws_ec2_transit_gateway_attachment",
    "data_aws_ec2_transit_gateway_connect",
    "data_aws_ec2_transit_gateway_connect_peer",
    "data_aws_ec2_transit_gateway_dx_gateway_attachment",
    "data_aws_ec2_transit_gateway_multicast_domain",
    "data_aws_ec2_transit_gateway_peering_attachment",
    "data_aws_ec2_transit_gateway_route_table",
    "data_aws_ec2_transit_gateway_route_tables",
    "data_aws_ec2_transit_gateway_vpc_attachment",
    "data_aws_ec2_transit_gateway_vpc_attachments",
    "data_aws_ec2_transit_gateway_vpn_attachment",
    "data_aws_ecr_authorization_token",
    "data_aws_ecr_image",
    "data_aws_ecr_repository",
    "data_aws_ecrpublic_authorization_token",
    "data_aws_ecs_cluster",
    "data_aws_ecs_container_definition",
    "data_aws_ecs_service",
    "data_aws_ecs_task_definition",
    "data_aws_efs_access_point",
    "data_aws_efs_access_points",
    "data_aws_efs_file_system",
    "data_aws_efs_mount_target",
    "data_aws_eip",
    "data_aws_eips",
    "data_aws_eks_addon",
    "data_aws_eks_addon_version",
    "data_aws_eks_cluster",
    "data_aws_eks_cluster_auth",
    "data_aws_eks_clusters",
    "data_aws_eks_node_group",
    "data_aws_eks_node_groups",
    "data_aws_elastic_beanstalk_application",
    "data_aws_elastic_beanstalk_hosted_zone",
    "data_aws_elastic_beanstalk_solution_stack",
    "data_aws_elasticache_cluster",
    "data_aws_elasticache_replication_group",
    "data_aws_elasticache_subnet_group",
    "data_aws_elasticache_user",
    "data_aws_elasticsearch_domain",
    "data_aws_elb",
    "data_aws_elb_hosted_zone_id",
    "data_aws_elb_service_account",
    "data_aws_emr_release_labels",
    "data_aws_emrcontainers_virtual_cluster",
    "data_aws_fsx_openzfs_snapshot",
    "data_aws_globalaccelerator_accelerator",
    "data_aws_glue_catalog_table",
    "data_aws_glue_connection",
    "data_aws_glue_data_catalog_encryption_settings",
    "data_aws_glue_script",
    "data_aws_grafana_workspace",
    "data_aws_guardduty_detector",
    "data_aws_iam_account_alias",
    "data_aws_iam_group",
    "data_aws_iam_instance_profile",
    "data_aws_iam_instance_profiles",
    "data_aws_iam_openid_connect_provider",
    "data_aws_iam_policy",
    "data_aws_iam_policy_document",
    "data_aws_iam_role",
    "data_aws_iam_roles",
    "data_aws_iam_saml_provider",
    "data_aws_iam_server_certificate",
    "data_aws_iam_session_context",
    "data_aws_iam_user",
    "data_aws_iam_user_ssh_key",
    "data_aws_iam_users",
    "data_aws_identitystore_group",
    "data_aws_identitystore_user",
    "data_aws_imagebuilder_component",
    "data_aws_imagebuilder_components",
    "data_aws_imagebuilder_container_recipe",
    "data_aws_imagebuilder_container_recipes",
    "data_aws_imagebuilder_distribution_configuration",
    "data_aws_imagebuilder_distribution_configurations",
    "data_aws_imagebuilder_image",
    "data_aws_imagebuilder_image_pipeline",
    "data_aws_imagebuilder_image_pipelines",
    "data_aws_imagebuilder_image_recipe",
    "data_aws_imagebuilder_image_recipes",
    "data_aws_imagebuilder_infrastructure_configuration",
    "data_aws_imagebuilder_infrastructure_configurations",
    "data_aws_inspector_rules_packages",
    "data_aws_instance",
    "data_aws_instances",
    "data_aws_internet_gateway",
    "data_aws_iot_endpoint",
    "data_aws_ip_ranges",
    "data_aws_ivs_stream_key",
    "data_aws_kendra_experience",
    "data_aws_kendra_faq",
    "data_aws_kendra_index",
    "data_aws_kendra_query_suggestions_block_list",
    "data_aws_kendra_thesaurus",
    "data_aws_key_pair",
    "data_aws_kinesis_firehose_delivery_stream",
    "data_aws_kinesis_stream",
    "data_aws_kinesis_stream_consumer",
    "data_aws_kms_alias",
    "data_aws_kms_ciphertext",
    "data_aws_kms_custom_key_store",
    "data_aws_kms_key",
    "data_aws_kms_public_key",
    "data_aws_kms_secret",
    "data_aws_kms_secrets",
    "data_aws_lakeformation_data_lake_settings",
    "data_aws_lakeformation_permissions",
    "data_aws_lakeformation_resource",
    "data_aws_lambda_alias",
    "data_aws_lambda_code_signing_config",
    "data_aws_lambda_function",
    "data_aws_lambda_function_url",
    "data_aws_lambda_functions",
    "data_aws_lambda_invocation",
    "data_aws_lambda_layer_version",
    "data_aws_launch_configuration",
    "data_aws_launch_template",
    "data_aws_lb",
    "data_aws_lb_hosted_zone_id",
    "data_aws_lb_listener",
    "data_aws_lb_target_group",
    "data_aws_lex_bot",
    "data_aws_lex_bot_alias",
    "data_aws_lex_intent",
    "data_aws_lex_slot_type",
    "data_aws_location_geofence_collection",
    "data_aws_location_map",
    "data_aws_location_place_index",
    "data_aws_location_route_calculator",
    "data_aws_location_tracker",
    "data_aws_location_tracker_association",
    "data_aws_location_tracker_associations",
    "data_aws_memorydb_acl",
    "data_aws_memorydb_cluster",
    "data_aws_memorydb_parameter_group",
    "data_aws_memorydb_snapshot",
    "data_aws_memorydb_subnet_group",
    "data_aws_memorydb_user",
    "data_aws_mq_broker",
    "data_aws_mq_broker_instance_type_offerings",
    "data_aws_msk_broker_nodes",
    "data_aws_msk_cluster",
    "data_aws_msk_configuration",
    "data_aws_msk_kafka_version",
    "data_aws_mskconnect_connector",
    "data_aws_mskconnect_custom_plugin",
    "data_aws_mskconnect_worker_configuration",
    "data_aws_nat_gateway",
    "data_aws_nat_gateways",
    "data_aws_neptune_engine_version",
    "data_aws_neptune_orderable_db_instance",
    "data_aws_network_acls",
    "data_aws_network_interface",
    "data_aws_network_interfaces",
    "data_aws_networkfirewall_firewall",
    "data_aws_networkfirewall_firewall_policy",
    "data_aws_networkmanager_connection",
    "data_aws_networkmanager_connections",
    "data_aws_networkmanager_core_network_policy_document",
    "data_aws_networkmanager_device",
    "data_aws_networkmanager_devices",
    "data_aws_networkmanager_global_network",
    "data_aws_networkmanager_global_networks",
    "data_aws_networkmanager_link",
    "data_aws_networkmanager_links",
    "data_aws_networkmanager_site",
    "data_aws_networkmanager_sites",
    "data_aws_opensearch_domain",
    "data_aws_organizations_delegated_administrators",
    "data_aws_organizations_delegated_services",
    "data_aws_organizations_organization",
    "data_aws_organizations_organizational_units",
    "data_aws_organizations_resource_tags",
    "data_aws_outposts_asset",
    "data_aws_outposts_assets",
    "data_aws_outposts_outpost",
    "data_aws_outposts_outpost_instance_type",
    "data_aws_outposts_outpost_instance_types",
    "data_aws_outposts_outposts",
    "data_aws_outposts_site",
    "data_aws_outposts_sites",
    "data_aws_partition",
    "data_aws_prefix_list",
    "data_aws_pricing_product",
    "data_aws_prometheus_workspace",
    "data_aws_qldb_ledger",
    "data_aws_ram_resource_share",
    "data_aws_rds_certificate",
    "data_aws_rds_cluster",
    "data_aws_rds_clusters",
    "data_aws_rds_engine_version",
    "data_aws_rds_orderable_db_instance",
    "data_aws_rds_reserved_instance_offering",
    "data_aws_redshift_cluster",
    "data_aws_redshift_cluster_credentials",
    "data_aws_redshift_orderable_cluster",
    "data_aws_redshift_service_account",
    "data_aws_redshift_subnet_group",
    "data_aws_redshiftserverless_credentials",
    "data_aws_region",
    "data_aws_regions",
    "data_aws_resourcegroupstaggingapi_resources",
    "data_aws_route",
    "data_aws_route53_delegation_set",
    "data_aws_route53_resolver_endpoint",
    "data_aws_route53_resolver_firewall_config",
    "data_aws_route53_resolver_firewall_domain_list",
    "data_aws_route53_resolver_firewall_rule_group",
    "data_aws_route53_resolver_firewall_rule_group_association",
    "data_aws_route53_resolver_firewall_rules",
    "data_aws_route53_resolver_rule",
    "data_aws_route53_resolver_rules",
    "data_aws_route53_traffic_policy_document",
    "data_aws_route53_zone",
    "data_aws_route_table",
    "data_aws_route_tables",
    "data_aws_s3_account_public_access_block",
    "data_aws_s3_bucket",
    "data_aws_s3_bucket_object",
    "data_aws_s3_bucket_objects",
    "data_aws_s3_bucket_policy",
    "data_aws_s3_control_multi_region_access_point",
    "data_aws_s3_object",
    "data_aws_s3_objects",
    "data_aws_sagemaker_prebuilt_ecr_image",
    "data_aws_secretsmanager_random_password",
    "data_aws_secretsmanager_secret",
    "data_aws_secretsmanager_secret_rotation",
    "data_aws_secretsmanager_secret_version",
    "data_aws_secretsmanager_secrets",
    "data_aws_security_group",
    "data_aws_security_groups",
    "data_aws_serverlessapplicationrepository_application",
    "data_aws_service",
    "data_aws_service_discovery_dns_namespace",
    "data_aws_service_discovery_http_namespace",
    "data_aws_service_discovery_service",
    "data_aws_servicecatalog_constraint",
    "data_aws_servicecatalog_launch_paths",
    "data_aws_servicecatalog_portfolio",
    "data_aws_servicecatalog_portfolio_constraints",
    "data_aws_servicecatalog_product",
    "data_aws_servicequotas_service",
    "data_aws_servicequotas_service_quota",
    "data_aws_ses_active_receipt_rule_set",
    "data_aws_ses_domain_identity",
    "data_aws_ses_email_identity",
    "data_aws_sesv2_dedicated_ip_pool",
    "data_aws_sfn_activity",
    "data_aws_sfn_state_machine",
    "data_aws_signer_signing_job",
    "data_aws_signer_signing_profile",
    "data_aws_sns_topic",
    "data_aws_sqs_queue",
    "data_aws_sqs_queues",
    "data_aws_ssm_document",
    "data_aws_ssm_instances",
    "data_aws_ssm_maintenance_windows",
    "data_aws_ssm_parameter",
    "data_aws_ssm_parameters_by_path",
    "data_aws_ssm_patch_baseline",
    "data_aws_ssoadmin_instances",
    "data_aws_ssoadmin_permission_set",
    "data_aws_storagegateway_local_disk",
    "data_aws_subnet",
    "data_aws_subnet_ids",
    "data_aws_subnets",
    "data_aws_transfer_server",
    "data_aws_vpc",
    "data_aws_vpc_dhcp_options",
    "data_aws_vpc_endpoint",
    "data_aws_vpc_endpoint_service",
    "data_aws_vpc_ipam_pool",
    "data_aws_vpc_ipam_pool_cidrs",
    "data_aws_vpc_ipam_pools",
    "data_aws_vpc_ipam_preview_next_cidr",
    "data_aws_vpc_peering_connection",
    "data_aws_vpc_peering_connections",
    "data_aws_vpcs",
    "data_aws_vpn_gateway",
    "data_aws_waf_ipset",
    "data_aws_waf_rate_based_rule",
    "data_aws_waf_rule",
    "data_aws_waf_subscribed_rule_group",
    "data_aws_waf_web_acl",
    "data_aws_wafregional_ipset",
    "data_aws_wafregional_rate_based_rule",
    "data_aws_wafregional_rule",
    "data_aws_wafregional_subscribed_rule_group",
    "data_aws_wafregional_web_acl",
    "data_aws_wafv2_ip_set",
    "data_aws_wafv2_regex_pattern_set",
    "data_aws_wafv2_rule_group",
    "data_aws_wafv2_web_acl",
    "data_aws_workspaces_bundle",
    "data_aws_workspaces_directory",
    "data_aws_workspaces_image",
    "data_aws_workspaces_workspace",
    "dataexchange_data_set",
    "dataexchange_revision",
    "datapipeline_pipeline",
    "datapipeline_pipeline_definition",
    "datasync_agent",
    "datasync_location_efs",
    "datasync_location_fsx_lustre_file_system",
    "datasync_location_fsx_openzfs_file_system",
    "datasync_location_fsx_windows_file_system",
    "datasync_location_hdfs",
    "datasync_location_nfs",
    "datasync_location_s3",
    "datasync_location_smb",
    "datasync_task",
    "dax_cluster",
    "dax_parameter_group",
    "dax_subnet_group",
    "db_cluster_snapshot",
    "db_event_subscription",
    "db_instance",
    "db_instance_automated_backups_replication",
    "db_instance_role_association",
    "db_option_group",
    "db_parameter_group",
    "db_proxy",
    "db_proxy_default_target_group",
    "db_proxy_endpoint",
    "db_proxy_target",
    "db_security_group",
    "db_snapshot",
    "db_snapshot_copy",
    "db_subnet_group",
    "default_network_acl",
    "default_route_table",
    "default_security_group",
    "default_subnet",
    "default_vpc",
    "default_vpc_dhcp_options",
    "detective_graph",
    "detective_invitation_accepter",
    "detective_member",
    "devicefarm_device_pool",
    "devicefarm_instance_profile",
    "devicefarm_network_profile",
    "devicefarm_project",
    "devicefarm_test_grid_project",
    "devicefarm_upload",
    "directory_service_conditional_forwarder",
    "directory_service_directory",
    "directory_service_log_subscription",
    "directory_service_radius_settings",
    "directory_service_region",
    "directory_service_shared_directory",
    "directory_service_shared_directory_accepter",
    "dlm_lifecycle_policy",
    "dms_certificate",
    "dms_endpoint",
    "dms_event_subscription",
    "dms_replication_instance",
    "dms_replication_subnet_group",
    "dms_replication_task",
    "dms_s3_endpoint",
    "docdb_cluster",
    "docdb_cluster_instance",
    "docdb_cluster_parameter_group",
    "docdb_cluster_snapshot",
    "docdb_event_subscription",
    "docdb_global_cluster",
    "docdb_subnet_group",
    "dx_bgp_peer",
    "dx_connection",
    "dx_connection_association",
    "dx_connection_confirmation",
    "dx_gateway",
    "dx_gateway_association",
    "dx_gateway_association_proposal",
    "dx_hosted_connection",
    "dx_hosted_private_virtual_interface",
    "dx_hosted_private_virtual_interface_accepter",
    "dx_hosted_public_virtual_interface",
    "dx_hosted_public_virtual_interface_accepter",
    "dx_hosted_transit_virtual_interface",
    "dx_hosted_transit_virtual_interface_accepter",
    "dx_lag",
    "dx_macsec_key_association",
    "dx_private_virtual_interface",
    "dx_public_virtual_interface",
    "dx_transit_virtual_interface",
    "dynamodb_contributor_insights",
    "dynamodb_global_table",
    "dynamodb_kinesis_streaming_destination",
    "dynamodb_table",
    "dynamodb_table_item",
    "dynamodb_table_replica",
    "dynamodb_tag",
    "ebs_default_kms_key",
    "ebs_encryption_by_default",
    "ebs_snapshot",
    "ebs_snapshot_copy",
    "ebs_snapshot_import",
    "ebs_volume",
    "ec2_availability_zone_group",
    "ec2_capacity_reservation",
    "ec2_carrier_gateway",
    "ec2_client_vpn_authorization_rule",
    "ec2_client_vpn_endpoint",
    "ec2_client_vpn_network_association",
    "ec2_client_vpn_route",
    "ec2_fleet",
    "ec2_host",
    "ec2_instance_state",
    "ec2_local_gateway_route",
    "ec2_local_gateway_route_table_vpc_association",
    "ec2_managed_prefix_list",
    "ec2_managed_prefix_list_entry",
    "ec2_network_insights_analysis",
    "ec2_network_insights_path",
    "ec2_serial_console_access",
    "ec2_subnet_cidr_reservation",
    "ec2_tag",
    "ec2_traffic_mirror_filter",
    "ec2_traffic_mirror_filter_rule",
    "ec2_traffic_mirror_session",
    "ec2_traffic_mirror_target",
    "ec2_transit_gateway",
    "ec2_transit_gateway_connect",
    "ec2_transit_gateway_connect_peer",
    "ec2_transit_gateway_multicast_domain",
    "ec2_transit_gateway_multicast_domain_association",
    "ec2_transit_gateway_multicast_group_member",
    "ec2_transit_gateway_multicast_group_source",
    "ec2_transit_gateway_peering_attachment",
    "ec2_transit_gateway_peering_attachment_accepter",
    "ec2_transit_gateway_policy_table",
    "ec2_transit_gateway_policy_table_association",
    "ec2_transit_gateway_prefix_list_reference",
    "ec2_transit_gateway_route",
    "ec2_transit_gateway_route_table",
    "ec2_transit_gateway_route_table_association",
    "ec2_transit_gateway_route_table_propagation",
    "ec2_transit_gateway_vpc_attachment",
    "ec2_transit_gateway_vpc_attachment_accepter",
    "ecr_lifecycle_policy",
    "ecr_pull_through_cache_rule",
    "ecr_registry_policy",
    "ecr_registry_scanning_configuration",
    "ecr_replication_configuration",
    "ecr_repository",
    "ecr_repository_policy",
    "ecrpublic_repository",
    "ecrpublic_repository_policy",
    "ecs_account_setting_default",
    "ecs_capacity_provider",
    "ecs_cluster",
    "ecs_cluster_capacity_providers",
    "ecs_service",
    "ecs_tag",
    "ecs_task_definition",
    "ecs_task_set",
    "efs_access_point",
    "efs_backup_policy",
    "efs_file_system",
    "efs_file_system_policy",
    "efs_mount_target",
    "efs_replication_configuration",
    "egress_only_internet_gateway",
    "eip",
    "eip_association",
    "eks_addon",
    "eks_cluster",
    "eks_fargate_profile",
    "eks_identity_provider_config",
    "eks_node_group",
    "elastic_beanstalk_application",
    "elastic_beanstalk_application_version",
    "elastic_beanstalk_configuration_template",
    "elastic_beanstalk_environment",
    "elasticache_cluster",
    "elasticache_global_replication_group",
    "elasticache_parameter_group",
    "elasticache_replication_group",
    "elasticache_security_group",
    "elasticache_subnet_group",
    "elasticache_user",
    "elasticache_user_group",
    "elasticache_user_group_association",
    "elasticsearch_domain",
    "elasticsearch_domain_policy",
    "elasticsearch_domain_saml_options",
    "elastictranscoder_pipeline",
    "elastictranscoder_preset",
    "elb",
    "elb_attachment",
    "emr_cluster",
    "emr_instance_fleet",
    "emr_instance_group",
    "emr_managed_scaling_policy",
    "emr_security_configuration",
    "emr_studio",
    "emr_studio_session_mapping",
    "emrcontainers_virtual_cluster",
    "emrserverless_application",
    "evidently_feature",
    "evidently_project",
    "evidently_segment",
    "fis_experiment_template",
    "flow_log",
    "fms_admin_account",
    "fms_policy",
    "fsx_backup",
    "fsx_data_repository_association",
    "fsx_file_cache",
    "fsx_lustre_file_system",
    "fsx_ontap_file_system",
    "fsx_ontap_storage_virtual_machine",
    "fsx_ontap_volume",
    "fsx_openzfs_file_system",
    "fsx_openzfs_snapshot",
    "fsx_openzfs_volume",
    "fsx_windows_file_system",
    "gamelift_alias",
    "gamelift_build",
    "gamelift_fleet",
    "gamelift_game_server_group",
    "gamelift_game_session_queue",
    "gamelift_script",
    "glacier_vault",
    "glacier_vault_lock",
    "globalaccelerator_accelerator",
    "globalaccelerator_endpoint_group",
    "globalaccelerator_listener",
    "glue_catalog_database",
    "glue_catalog_table",
    "glue_classifier",
    "glue_connection",
    "glue_crawler",
    "glue_data_catalog_encryption_settings",
    "glue_dev_endpoint",
    "glue_job",
    "glue_ml_transform",
    "glue_partition",
    "glue_partition_index",
    "glue_registry",
    "glue_resource_policy",
    "glue_schema",
    "glue_security_configuration",
    "glue_trigger",
    "glue_user_defined_function",
    "glue_workflow",
    "grafana_license_association",
    "grafana_role_association",
    "grafana_workspace",
    "grafana_workspace_api_key",
    "grafana_workspace_saml_configuration",
    "guardduty_detector",
    "guardduty_filter",
    "guardduty_invite_accepter",
    "guardduty_ipset",
    "guardduty_member",
    "guardduty_organization_admin_account",
    "guardduty_organization_configuration",
    "guardduty_publishing_destination",
    "guardduty_threatintelset",
    "iam_access_key",
    "iam_account_alias",
    "iam_account_password_policy",
    "iam_group",
    "iam_group_membership",
    "iam_group_policy",
    "iam_group_policy_attachment",
    "iam_instance_profile",
    "iam_openid_connect_provider",
    "iam_policy",
    "iam_policy_attachment",
    "iam_role",
    "iam_role_policy",
    "iam_role_policy_attachment",
    "iam_saml_provider",
    "iam_server_certificate",
    "iam_service_linked_role",
    "iam_service_specific_credential",
    "iam_signing_certificate",
    "iam_user",
    "iam_user_group_membership",
    "iam_user_login_profile",
    "iam_user_policy",
    "iam_user_policy_attachment",
    "iam_user_ssh_key",
    "iam_virtual_mfa_device",
    "identitystore_group",
    "identitystore_group_membership",
    "identitystore_user",
    "imagebuilder_component",
    "imagebuilder_container_recipe",
    "imagebuilder_distribution_configuration",
    "imagebuilder_image",
    "imagebuilder_image_pipeline",
    "imagebuilder_image_recipe",
    "imagebuilder_infrastructure_configuration",
    "inspector2_delegated_admin_account",
    "inspector2_enabler",
    "inspector2_organization_configuration",
    "inspector_assessment_target",
    "inspector_assessment_template",
    "inspector_resource_group",
    "instance",
    "internet_gateway",
    "internet_gateway_attachment",
    "iot_authorizer",
    "iot_certificate",
    "iot_indexing_configuration",
    "iot_logging_options",
    "iot_policy",
    "iot_policy_attachment",
    "iot_provisioning_template",
    "iot_role_alias",
    "iot_thing",
    "iot_thing_group",
    "iot_thing_group_membership",
    "iot_thing_principal_attachment",
    "iot_thing_type",
    "iot_topic_rule",
    "iot_topic_rule_destination",
    "ivs_channel",
    "ivs_playback_key_pair",
    "ivs_recording_configuration",
    "ivschat_logging_configuration",
    "ivschat_room",
    "kendra_data_source",
    "kendra_experience",
    "kendra_faq",
    "kendra_index",
    "kendra_query_suggestions_block_list",
    "kendra_thesaurus",
    "key_pair",
    "keyspaces_keyspace",
    "keyspaces_table",
    "kinesis_analytics_application",
    "kinesis_firehose_delivery_stream",
    "kinesis_stream",
    "kinesis_stream_consumer",
    "kinesis_video_stream",
    "kinesisanalyticsv2_application",
    "kinesisanalyticsv2_application_snapshot",
    "kms_alias",
    "kms_ciphertext",
    "kms_custom_key_store",
    "kms_external_key",
    "kms_grant",
    "kms_key",
    "kms_replica_external_key",
    "kms_replica_key",
    "lakeformation_data_lake_settings",
    "lakeformation_lf_tag",
    "lakeformation_permissions",
    "lakeformation_resource",
    "lakeformation_resource_lf_tags",
    "lambda_alias",
    "lambda_code_signing_config",
    "lambda_event_source_mapping",
    "lambda_function",
    "lambda_function_event_invoke_config",
    "lambda_function_url",
    "lambda_invocation",
    "lambda_layer_version",
    "lambda_layer_version_permission",
    "lambda_permission",
    "lambda_provisioned_concurrency_config",
    "launch_configuration",
    "launch_template",
    "lb",
    "lb_cookie_stickiness_policy",
    "lb_listener",
    "lb_listener_certificate",
    "lb_listener_rule",
    "lb_ssl_negotiation_policy",
    "lb_target_group",
    "lb_target_group_attachment",
    "lex_bot",
    "lex_bot_alias",
    "lex_intent",
    "lex_slot_type",
    "licensemanager_association",
    "licensemanager_license_configuration",
    "lightsail_bucket",
    "lightsail_certificate",
    "lightsail_container_service",
    "lightsail_container_service_deployment_version",
    "lightsail_database",
    "lightsail_disk",
    "lightsail_disk_attachment",
    "lightsail_domain",
    "lightsail_domain_entry",
    "lightsail_instance",
    "lightsail_instance_public_ports",
    "lightsail_key_pair",
    "lightsail_lb",
    "lightsail_lb_attachment",
    "lightsail_lb_certificate",
    "lightsail_lb_certificate_attachment",
    "lightsail_lb_https_redirection_policy",
    "lightsail_lb_stickiness_policy",
    "lightsail_static_ip",
    "lightsail_static_ip_attachment",
    "load_balancer_backend_server_policy",
    "load_balancer_listener_policy",
    "load_balancer_policy",
    "location_geofence_collection",
    "location_map",
    "location_place_index",
    "location_route_calculator",
    "location_tracker",
    "location_tracker_association",
    "macie2_account",
    "macie2_classification_export_configuration",
    "macie2_classification_job",
    "macie2_custom_data_identifier",
    "macie2_findings_filter",
    "macie2_invitation_accepter",
    "macie2_member",
    "macie2_organization_admin_account",
    "macie_member_account_association",
    "macie_s3_bucket_association",
    "main_route_table_association",
    "media_convert_queue",
    "media_package_channel",
    "media_store_container",
    "media_store_container_policy",
    "medialive_channel",
    "medialive_input",
    "medialive_input_security_group",
    "medialive_multiplex",
    "medialive_multiplex_program",
    "memorydb_acl",
    "memorydb_cluster",
    "memorydb_parameter_group",
    "memorydb_snapshot",
    "memorydb_subnet_group",
    "memorydb_user",
    "mq_broker",
    "mq_configuration",
    "msk_cluster",
    "msk_configuration",
    "msk_scram_secret_association",
    "msk_serverless_cluster",
    "mskconnect_connector",
    "mskconnect_custom_plugin",
    "mskconnect_worker_configuration",
    "mwaa_environment",
    "nat_gateway",
    "neptune_cluster",
    "neptune_cluster_endpoint",
    "neptune_cluster_instance",
    "neptune_cluster_parameter_group",
    "neptune_cluster_snapshot",
    "neptune_event_subscription",
    "neptune_global_cluster",
    "neptune_parameter_group",
    "neptune_subnet_group",
    "network_acl",
    "network_acl_association",
    "network_acl_rule",
    "network_interface",
    "network_interface_attachment",
    "network_interface_sg_attachment",
    "networkfirewall_firewall",
    "networkfirewall_firewall_policy",
    "networkfirewall_logging_configuration",
    "networkfirewall_resource_policy",
    "networkfirewall_rule_group",
    "networkmanager_attachment_accepter",
    "networkmanager_connect_attachment",
    "networkmanager_connection",
    "networkmanager_core_network",
    "networkmanager_customer_gateway_association",
    "networkmanager_device",
    "networkmanager_global_network",
    "networkmanager_link",
    "networkmanager_link_association",
    "networkmanager_site",
    "networkmanager_site_to_site_vpn_attachment",
    "networkmanager_transit_gateway_connect_peer_association",
    "networkmanager_transit_gateway_peering",
    "networkmanager_transit_gateway_registration",
    "networkmanager_transit_gateway_route_table_attachment",
    "networkmanager_vpc_attachment",
    "opensearch_domain",
    "opensearch_domain_policy",
    "opensearch_domain_saml_options",
    "opensearch_inbound_connection_accepter",
    "opensearch_outbound_connection",
    "opsworks_application",
    "opsworks_custom_layer",
    "opsworks_ecs_cluster_layer",
    "opsworks_ganglia_layer",
    "opsworks_haproxy_layer",
    "opsworks_instance",
    "opsworks_java_app_layer",
    "opsworks_memcached_layer",
    "opsworks_mysql_layer",
    "opsworks_nodejs_app_layer",
    "opsworks_permission",
    "opsworks_php_app_layer",
    "opsworks_rails_app_layer",
    "opsworks_rds_db_instance",
    "opsworks_stack",
    "opsworks_static_web_layer",
    "opsworks_user_profile",
    "organizations_account",
    "organizations_delegated_administrator",
    "organizations_organization",
    "organizations_organizational_unit",
    "organizations_policy",
    "organizations_policy_attachment",
    "pinpoint_adm_channel",
    "pinpoint_apns_channel",
    "pinpoint_apns_sandbox_channel",
    "pinpoint_apns_voip_channel",
    "pinpoint_apns_voip_sandbox_channel",
    "pinpoint_app",
    "pinpoint_baidu_channel",
    "pinpoint_email_channel",
    "pinpoint_event_stream",
    "pinpoint_gcm_channel",
    "pinpoint_sms_channel",
    "placement_group",
    "prometheus_alert_manager_definition",
    "prometheus_rule_group_namespace",
    "prometheus_workspace",
    "provider",
    "proxy_protocol_policy",
    "qldb_ledger",
    "qldb_stream",
    "quicksight_data_source",
    "quicksight_group",
    "quicksight_group_membership",
    "quicksight_user",
    "ram_principal_association",
    "ram_resource_association",
    "ram_resource_share",
    "ram_resource_share_accepter",
    "rds_cluster",
    "rds_cluster_activity_stream",
    "rds_cluster_endpoint",
    "rds_cluster_instance",
    "rds_cluster_parameter_group",
    "rds_cluster_role_association",
    "rds_global_cluster",
    "rds_reserved_instance",
    "redshift_authentication_profile",
    "redshift_cluster",
    "redshift_cluster_iam_roles",
    "redshift_endpoint_access",
    "redshift_endpoint_authorization",
    "redshift_event_subscription",
    "redshift_hsm_client_certificate",
    "redshift_hsm_configuration",
    "redshift_parameter_group",
    "redshift_partner",
    "redshift_scheduled_action",
    "redshift_security_group",
    "redshift_snapshot_copy_grant",
    "redshift_snapshot_schedule",
    "redshift_snapshot_schedule_association",
    "redshift_subnet_group",
    "redshift_usage_limit",
    "redshiftdata_statement",
    "redshiftserverless_endpoint_access",
    "redshiftserverless_namespace",
    "redshiftserverless_resource_policy",
    "redshiftserverless_snapshot",
    "redshiftserverless_usage_limit",
    "redshiftserverless_workgroup",
    "resourceexplorer2_index",
    "resourcegroups_group",
    "rolesanywhere_profile",
    "rolesanywhere_trust_anchor",
    "route",
    "route53_delegation_set",
    "route53_domains_registered_domain",
    "route53_health_check",
    "route53_hosted_zone_dnssec",
    "route53_key_signing_key",
    "route53_query_log",
    "route53_record",
    "route53_recoverycontrolconfig_cluster",
    "route53_recoverycontrolconfig_control_panel",
    "route53_recoverycontrolconfig_routing_control",
    "route53_recoverycontrolconfig_safety_rule",
    "route53_recoveryreadiness_cell",
    "route53_recoveryreadiness_readiness_check",
    "route53_recoveryreadiness_recovery_group",
    "route53_recoveryreadiness_resource_set",
    "route53_resolver_config",
    "route53_resolver_dnssec_config",
    "route53_resolver_endpoint",
    "route53_resolver_firewall_config",
    "route53_resolver_firewall_domain_list",
    "route53_resolver_firewall_rule",
    "route53_resolver_firewall_rule_group",
    "route53_resolver_firewall_rule_group_association",
    "route53_resolver_query_log_config",
    "route53_resolver_query_log_config_association",
    "route53_resolver_rule",
    "route53_resolver_rule_association",
    "route53_traffic_policy",
    "route53_traffic_policy_instance",
    "route53_vpc_association_authorization",
    "route53_zone",
    "route53_zone_association",
    "route_table",
    "route_table_association",
    "rum_app_monitor",
    "rum_metrics_destination",
    "s3_access_point",
    "s3_account_public_access_block",
    "s3_bucket",
    "s3_bucket_accelerate_configuration",
    "s3_bucket_acl",
    "s3_bucket_analytics_configuration",
    "s3_bucket_cors_configuration",
    "s3_bucket_intelligent_tiering_configuration",
    "s3_bucket_inventory",
    "s3_bucket_lifecycle_configuration",
    "s3_bucket_logging",
    "s3_bucket_metric",
    "s3_bucket_notification",
    "s3_bucket_object",
    "s3_bucket_object_lock_configuration",
    "s3_bucket_ownership_controls",
    "s3_bucket_policy",
    "s3_bucket_public_access_block",
    "s3_bucket_replication_configuration",
    "s3_bucket_request_payment_configuration",
    "s3_bucket_server_side_encryption_configuration",
    "s3_bucket_versioning",
    "s3_bucket_website_configuration",
    "s3_control_access_point_policy",
    "s3_control_bucket",
    "s3_control_bucket_lifecycle_configuration",
    "s3_control_bucket_policy",
    "s3_control_multi_region_access_point",
    "s3_control_multi_region_access_point_policy",
    "s3_control_object_lambda_access_point",
    "s3_control_object_lambda_access_point_policy",
    "s3_control_storage_lens_configuration",
    "s3_object",
    "s3_object_copy",
    "s3_outposts_endpoint",
    "sagemaker_app",
    "sagemaker_app_image_config",
    "sagemaker_code_repository",
    "sagemaker_device",
    "sagemaker_device_fleet",
    "sagemaker_domain",
    "sagemaker_endpoint",
    "sagemaker_endpoint_configuration",
    "sagemaker_feature_group",
    "sagemaker_flow_definition",
    "sagemaker_human_task_ui",
    "sagemaker_image",
    "sagemaker_image_version",
    "sagemaker_model",
    "sagemaker_model_package_group",
    "sagemaker_model_package_group_policy",
    "sagemaker_notebook_instance",
    "sagemaker_notebook_instance_lifecycle_configuration",
    "sagemaker_project",
    "sagemaker_servicecatalog_portfolio_status",
    "sagemaker_space",
    "sagemaker_studio_lifecycle_config",
    "sagemaker_user_profile",
    "sagemaker_workforce",
    "sagemaker_workteam",
    "scheduler_schedule",
    "scheduler_schedule_group",
    "schemas_discoverer",
    "schemas_registry",
    "schemas_registry_policy",
    "schemas_schema",
    "secretsmanager_secret",
    "secretsmanager_secret_policy",
    "secretsmanager_secret_rotation",
    "secretsmanager_secret_version",
    "security_group",
    "security_group_rule",
    "securityhub_account",
    "securityhub_action_target",
    "securityhub_finding_aggregator",
    "securityhub_insight",
    "securityhub_invite_accepter",
    "securityhub_member",
    "securityhub_organization_admin_account",
    "securityhub_organization_configuration",
    "securityhub_product_subscription",
    "securityhub_standards_control",
    "securityhub_standards_subscription",
    "serverlessapplicationrepository_cloudformation_stack",
    "service_discovery_http_namespace",
    "service_discovery_instance",
    "service_discovery_private_dns_namespace",
    "service_discovery_public_dns_namespace",
    "service_discovery_service",
    "servicecatalog_budget_resource_association",
    "servicecatalog_constraint",
    "servicecatalog_organizations_access",
    "servicecatalog_portfolio",
    "servicecatalog_portfolio_share",
    "servicecatalog_principal_portfolio_association",
    "servicecatalog_product",
    "servicecatalog_product_portfolio_association",
    "servicecatalog_provisioned_product",
    "servicecatalog_provisioning_artifact",
    "servicecatalog_service_action",
    "servicecatalog_tag_option",
    "servicecatalog_tag_option_resource_association",
    "servicequotas_service_quota",
    "ses_active_receipt_rule_set",
    "ses_configuration_set",
    "ses_domain_dkim",
    "ses_domain_identity",
    "ses_domain_identity_verification",
    "ses_domain_mail_from",
    "ses_email_identity",
    "ses_event_destination",
    "ses_identity_notification_topic",
    "ses_identity_policy",
    "ses_receipt_filter",
    "ses_receipt_rule",
    "ses_receipt_rule_set",
    "ses_template",
    "sesv2_configuration_set",
    "sesv2_dedicated_ip_assignment",
    "sesv2_dedicated_ip_pool",
    "sesv2_email_identity",
    "sesv2_email_identity_feedback_attributes",
    "sesv2_email_identity_mail_from_attributes",
    "sfn_activity",
    "sfn_state_machine",
    "shield_protection",
    "shield_protection_group",
    "shield_protection_health_check_association",
    "signer_signing_job",
    "signer_signing_profile",
    "signer_signing_profile_permission",
    "simpledb_domain",
    "snapshot_create_volume_permission",
    "sns_platform_application",
    "sns_sms_preferences",
    "sns_topic",
    "sns_topic_policy",
    "sns_topic_subscription",
    "spot_datafeed_subscription",
    "spot_fleet_request",
    "spot_instance_request",
    "sqs_queue",
    "sqs_queue_policy",
    "sqs_queue_redrive_allow_policy",
    "sqs_queue_redrive_policy",
    "ssm_activation",
    "ssm_association",
    "ssm_default_patch_baseline",
    "ssm_document",
    "ssm_maintenance_window",
    "ssm_maintenance_window_target",
    "ssm_maintenance_window_task",
    "ssm_parameter",
    "ssm_patch_baseline",
    "ssm_patch_group",
    "ssm_resource_data_sync",
    "ssm_service_setting",
    "ssoadmin_account_assignment",
    "ssoadmin_customer_managed_policy_attachment",
    "ssoadmin_instance_access_control_attributes",
    "ssoadmin_managed_policy_attachment",
    "ssoadmin_permission_set",
    "ssoadmin_permission_set_inline_policy",
    "ssoadmin_permissions_boundary_attachment",
    "storagegateway_cache",
    "storagegateway_cached_iscsi_volume",
    "storagegateway_file_system_association",
    "storagegateway_gateway",
    "storagegateway_nfs_file_share",
    "storagegateway_smb_file_share",
    "storagegateway_stored_iscsi_volume",
    "storagegateway_tape_pool",
    "storagegateway_upload_buffer",
    "storagegateway_working_storage",
    "subnet",
    "swf_domain",
    "synthetics_canary",
    "timestreamwrite_database",
    "timestreamwrite_table",
    "transcribe_language_model",
    "transcribe_medical_vocabulary",
    "transcribe_vocabulary",
    "transcribe_vocabulary_filter",
    "transfer_access",
    "transfer_server",
    "transfer_ssh_key",
    "transfer_tag",
    "transfer_user",
    "transfer_workflow",
    "volume_attachment",
    "vpc",
    "vpc_dhcp_options",
    "vpc_dhcp_options_association",
    "vpc_endpoint",
    "vpc_endpoint_connection_accepter",
    "vpc_endpoint_connection_notification",
    "vpc_endpoint_policy",
    "vpc_endpoint_route_table_association",
    "vpc_endpoint_security_group_association",
    "vpc_endpoint_service",
    "vpc_endpoint_service_allowed_principal",
    "vpc_endpoint_subnet_association",
    "vpc_ipam",
    "vpc_ipam_organization_admin_account",
    "vpc_ipam_pool",
    "vpc_ipam_pool_cidr",
    "vpc_ipam_pool_cidr_allocation",
    "vpc_ipam_preview_next_cidr",
    "vpc_ipam_scope",
    "vpc_ipv4_cidr_block_association",
    "vpc_ipv6_cidr_block_association",
    "vpc_network_performance_metric_subscription",
    "vpc_peering_connection",
    "vpc_peering_connection_accepter",
    "vpc_peering_connection_options",
    "vpn_connection",
    "vpn_connection_route",
    "vpn_gateway",
    "vpn_gateway_attachment",
    "vpn_gateway_route_propagation",
    "waf_byte_match_set",
    "waf_geo_match_set",
    "waf_ipset",
    "waf_rate_based_rule",
    "waf_regex_match_set",
    "waf_regex_pattern_set",
    "waf_rule",
    "waf_rule_group",
    "waf_size_constraint_set",
    "waf_sql_injection_match_set",
    "waf_web_acl",
    "waf_xss_match_set",
    "wafregional_byte_match_set",
    "wafregional_geo_match_set",
    "wafregional_ipset",
    "wafregional_rate_based_rule",
    "wafregional_regex_match_set",
    "wafregional_regex_pattern_set",
    "wafregional_rule",
    "wafregional_rule_group",
    "wafregional_size_constraint_set",
    "wafregional_sql_injection_match_set",
    "wafregional_web_acl",
    "wafregional_web_acl_association",
    "wafregional_xss_match_set",
    "wafv2_ip_set",
    "wafv2_regex_pattern_set",
    "wafv2_rule_group",
    "wafv2_web_acl",
    "wafv2_web_acl_association",
    "wafv2_web_acl_logging_configuration",
    "worklink_fleet",
    "worklink_website_certificate_authority_association",
    "workspaces_directory",
    "workspaces_ip_group",
    "workspaces_workspace",
    "xray_encryption_config",
    "xray_group",
    "xray_sampling_rule",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import accessanalyzer_analyzer
from . import accessanalyzer_archive_rule
from . import account_alternate_contact
from . import acm_certificate
from . import acm_certificate_validation
from . import acmpca_certificate
from . import acmpca_certificate_authority
from . import acmpca_certificate_authority_certificate
from . import acmpca_permission
from . import acmpca_policy
from . import alb
from . import alb_listener
from . import alb_listener_certificate
from . import alb_listener_rule
from . import alb_target_group
from . import alb_target_group_attachment
from . import ami
from . import ami_copy
from . import ami_from_instance
from . import ami_launch_permission
from . import amplify_app
from . import amplify_backend_environment
from . import amplify_branch
from . import amplify_domain_association
from . import amplify_webhook
from . import api_gateway_account
from . import api_gateway_api_key
from . import api_gateway_authorizer
from . import api_gateway_base_path_mapping
from . import api_gateway_client_certificate
from . import api_gateway_deployment
from . import api_gateway_documentation_part
from . import api_gateway_documentation_version
from . import api_gateway_domain_name
from . import api_gateway_gateway_response
from . import api_gateway_integration
from . import api_gateway_integration_response
from . import api_gateway_method
from . import api_gateway_method_response
from . import api_gateway_method_settings
from . import api_gateway_model
from . import api_gateway_request_validator
from . import api_gateway_resource
from . import api_gateway_rest_api
from . import api_gateway_rest_api_policy
from . import api_gateway_stage
from . import api_gateway_usage_plan
from . import api_gateway_usage_plan_key
from . import api_gateway_vpc_link
from . import apigatewayv2_api
from . import apigatewayv2_api_mapping
from . import apigatewayv2_authorizer
from . import apigatewayv2_deployment
from . import apigatewayv2_domain_name
from . import apigatewayv2_integration
from . import apigatewayv2_integration_response
from . import apigatewayv2_model
from . import apigatewayv2_route
from . import apigatewayv2_route_response
from . import apigatewayv2_stage
from . import apigatewayv2_vpc_link
from . import app_cookie_stickiness_policy
from . import appautoscaling_policy
from . import appautoscaling_scheduled_action
from . import appautoscaling_target
from . import appconfig_application
from . import appconfig_configuration_profile
from . import appconfig_deployment
from . import appconfig_deployment_strategy
from . import appconfig_environment
from . import appconfig_extension
from . import appconfig_extension_association
from . import appconfig_hosted_configuration_version
from . import appflow_connector_profile
from . import appflow_flow
from . import appintegrations_event_integration
from . import applicationinsights_application
from . import appmesh_gateway_route
from . import appmesh_mesh
from . import appmesh_route
from . import appmesh_virtual_gateway
from . import appmesh_virtual_node
from . import appmesh_virtual_router
from . import appmesh_virtual_service
from . import apprunner_auto_scaling_configuration_version
from . import apprunner_connection
from . import apprunner_custom_domain_association
from . import apprunner_observability_configuration
from . import apprunner_service
from . import apprunner_vpc_connector
from . import apprunner_vpc_ingress_connection
from . import appstream_directory_config
from . import appstream_fleet
from . import appstream_fleet_stack_association
from . import appstream_image_builder
from . import appstream_stack
from . import appstream_user
from . import appstream_user_stack_association
from . import appsync_api_cache
from . import appsync_api_key
from . import appsync_datasource
from . import appsync_domain_name
from . import appsync_domain_name_api_association
from . import appsync_function
from . import appsync_graphql_api
from . import appsync_resolver
from . import appsync_type
from . import athena_data_catalog
from . import athena_database
from . import athena_named_query
from . import athena_workgroup
from . import auditmanager_account_registration
from . import auditmanager_assessment
from . import auditmanager_assessment_report
from . import auditmanager_control
from . import auditmanager_framework
from . import autoscaling_attachment
from . import autoscaling_group
from . import autoscaling_group_tag
from . import autoscaling_lifecycle_hook
from . import autoscaling_notification
from . import autoscaling_policy
from . import autoscaling_schedule
from . import autoscalingplans_scaling_plan
from . import backup_framework
from . import backup_global_settings
from . import backup_plan
from . import backup_region_settings
from . import backup_report_plan
from . import backup_selection
from . import backup_vault
from . import backup_vault_lock_configuration
from . import backup_vault_notifications
from . import backup_vault_policy
from . import batch_compute_environment
from . import batch_job_definition
from . import batch_job_queue
from . import batch_scheduling_policy
from . import budgets_budget
from . import budgets_budget_action
from . import ce_anomaly_monitor
from . import ce_anomaly_subscription
from . import ce_cost_allocation_tag
from . import ce_cost_category
from . import chime_voice_connector
from . import chime_voice_connector_group
from . import chime_voice_connector_logging
from . import chime_voice_connector_origination
from . import chime_voice_connector_streaming
from . import chime_voice_connector_termination
from . import chime_voice_connector_termination_credentials
from . import cloud9_environment_ec2
from . import cloud9_environment_membership
from . import cloudcontrolapi_resource
from . import cloudformation_stack
from . import cloudformation_stack_set
from . import cloudformation_stack_set_instance
from . import cloudformation_type
from . import cloudfront_cache_policy
from . import cloudfront_distribution
from . import cloudfront_field_level_encryption_config
from . import cloudfront_field_level_encryption_profile
from . import cloudfront_function
from . import cloudfront_key_group
from . import cloudfront_monitoring_subscription
from . import cloudfront_origin_access_control
from . import cloudfront_origin_access_identity
from . import cloudfront_origin_request_policy
from . import cloudfront_public_key
from . import cloudfront_realtime_log_config
from . import cloudfront_response_headers_policy
from . import cloudhsm_v2_cluster
from . import cloudhsm_v2_hsm
from . import cloudsearch_domain
from . import cloudsearch_domain_service_access_policy
from . import cloudtrail
from . import cloudtrail_event_data_store
from . import cloudwatch_composite_alarm
from . import cloudwatch_dashboard
from . import cloudwatch_event_api_destination
from . import cloudwatch_event_archive
from . import cloudwatch_event_bus
from . import cloudwatch_event_bus_policy
from . import cloudwatch_event_connection
from . import cloudwatch_event_permission
from . import cloudwatch_event_rule
from . import cloudwatch_event_target
from . import cloudwatch_log_data_protection_policy
from . import cloudwatch_log_destination
from . import cloudwatch_log_destination_policy
from . import cloudwatch_log_group
from . import cloudwatch_log_metric_filter
from . import cloudwatch_log_resource_policy
from . import cloudwatch_log_stream
from . import cloudwatch_log_subscription_filter
from . import cloudwatch_metric_alarm
from . import cloudwatch_metric_stream
from . import cloudwatch_query_definition
from . import codeartifact_domain
from . import codeartifact_domain_permissions_policy
from . import codeartifact_repository
from . import codeartifact_repository_permissions_policy
from . import codebuild_project
from . import codebuild_report_group
from . import codebuild_resource_policy
from . import codebuild_source_credential
from . import codebuild_webhook
from . import codecommit_approval_rule_template
from . import codecommit_approval_rule_template_association
from . import codecommit_repository
from . import codecommit_trigger
from . import codedeploy_app
from . import codedeploy_deployment_config
from . import codedeploy_deployment_group
from . import codepipeline
from . import codepipeline_custom_action_type
from . import codepipeline_webhook
from . import codestarconnections_connection
from . import codestarconnections_host
from . import codestarnotifications_notification_rule
from . import cognito_identity_pool
from . import cognito_identity_pool_provider_principal_tag
from . import cognito_identity_pool_roles_attachment
from . import cognito_identity_provider
from . import cognito_resource_server
from . import cognito_risk_configuration
from . import cognito_user
from . import cognito_user_group
from . import cognito_user_in_group
from . import cognito_user_pool
from . import cognito_user_pool_client
from . import cognito_user_pool_domain
from . import cognito_user_pool_ui_customization
from . import comprehend_document_classifier
from . import comprehend_entity_recognizer
from . import config_aggregate_authorization
from . import config_config_rule
from . import config_configuration_aggregator
from . import config_configuration_recorder
from . import config_configuration_recorder_status
from . import config_conformance_pack
from . import config_delivery_channel
from . import config_organization_conformance_pack
from . import config_organization_custom_rule
from . import config_organization_managed_rule
from . import config_remediation_configuration
from . import connect_bot_association
from . import connect_contact_flow
from . import connect_contact_flow_module
from . import connect_hours_of_operation
from . import connect_instance
from . import connect_instance_storage_config
from . import connect_lambda_function_association
from . import connect_phone_number
from . import connect_queue
from . import connect_quick_connect
from . import connect_routing_profile
from . import connect_security_profile
from . import connect_user
from . import connect_user_hierarchy_group
from . import connect_user_hierarchy_structure
from . import connect_vocabulary
from . import controltower_control
from . import cur_report_definition
from . import customer_gateway
from . import data_aws_acm_certificate
from . import data_aws_acmpca_certificate
from . import data_aws_acmpca_certificate_authority
from . import data_aws_alb
from . import data_aws_alb_listener
from . import data_aws_alb_target_group
from . import data_aws_ami
from . import data_aws_ami_ids
from . import data_aws_api_gateway_api_key
from . import data_aws_api_gateway_domain_name
from . import data_aws_api_gateway_export
from . import data_aws_api_gateway_resource
from . import data_aws_api_gateway_rest_api
from . import data_aws_api_gateway_sdk
from . import data_aws_api_gateway_vpc_link
from . import data_aws_apigatewayv2_api
from . import data_aws_apigatewayv2_apis
from . import data_aws_apigatewayv2_export
from . import data_aws_appconfig_configuration_profile
from . import data_aws_appconfig_configuration_profiles
from . import data_aws_appconfig_environment
from . import data_aws_appconfig_environments
from . import data_aws_appmesh_mesh
from . import data_aws_appmesh_virtual_service
from . import data_aws_arn
from . import data_aws_autoscaling_group
from . import data_aws_autoscaling_groups
from . import data_aws_availability_zone
from . import data_aws_availability_zones
from . import data_aws_backup_framework
from . import data_aws_backup_plan
from . import data_aws_backup_report_plan
from . import data_aws_backup_selection
from . import data_aws_backup_vault
from . import data_aws_batch_compute_environment
from . import data_aws_batch_job_queue
from . import data_aws_batch_scheduling_policy
from . import data_aws_billing_service_account
from . import data_aws_caller_identity
from . import data_aws_canonical_user_id
from . import data_aws_ce_cost_category
from . import data_aws_ce_tags
from . import data_aws_cloudcontrolapi_resource
from . import data_aws_cloudformation_export
from . import data_aws_cloudformation_stack
from . import data_aws_cloudformation_type
from . import data_aws_cloudfront_cache_policy
from . import data_aws_cloudfront_distribution
from . import data_aws_cloudfront_function
from . import data_aws_cloudfront_log_delivery_canonical_user_id
from . import data_aws_cloudfront_origin_access_identities
from . import data_aws_cloudfront_origin_access_identity
from . import data_aws_cloudfront_origin_request_policy
from . import data_aws_cloudfront_realtime_log_config
from . import data_aws_cloudfront_response_headers_policy
from . import data_aws_cloudhsm_v2_cluster
from . import data_aws_cloudtrail_service_account
from . import data_aws_cloudwatch_event_bus
from . import data_aws_cloudwatch_event_connection
from . import data_aws_cloudwatch_event_source
from . import data_aws_cloudwatch_log_data_protection_policy_document
from . import data_aws_cloudwatch_log_group
from . import data_aws_cloudwatch_log_groups
from . import data_aws_codeartifact_authorization_token
from . import data_aws_codeartifact_repository_endpoint
from . import data_aws_codecommit_approval_rule_template
from . import data_aws_codecommit_repository
from . import data_aws_codestarconnections_connection
from . import data_aws_cognito_user_pool_client
from . import data_aws_cognito_user_pool_clients
from . import data_aws_cognito_user_pool_signing_certificate
from . import data_aws_cognito_user_pools
from . import data_aws_connect_bot_association
from . import data_aws_connect_contact_flow
from . import data_aws_connect_contact_flow_module
from . import data_aws_connect_hours_of_operation
from . import data_aws_connect_instance
from . import data_aws_connect_instance_storage_config
from . import data_aws_connect_lambda_function_association
from . import data_aws_connect_prompt
from . import data_aws_connect_queue
from . import data_aws_connect_quick_connect
from . import data_aws_connect_routing_profile
from . import data_aws_connect_security_profile
from . import data_aws_connect_user_hierarchy_group
from . import data_aws_connect_user_hierarchy_structure
from . import data_aws_controltower_controls
from . import data_aws_cur_report_definition
from . import data_aws_customer_gateway
from . import data_aws_datapipeline_pipeline
from . import data_aws_datapipeline_pipeline_definition
from . import data_aws_db_cluster_snapshot
from . import data_aws_db_event_categories
from . import data_aws_db_instance
from . import data_aws_db_instances
from . import data_aws_db_proxy
from . import data_aws_db_snapshot
from . import data_aws_db_subnet_group
from . import data_aws_default_tags
from . import data_aws_directory_service_directory
from . import data_aws_docdb_engine_version
from . import data_aws_docdb_orderable_db_instance
from . import data_aws_dx_connection
from . import data_aws_dx_gateway
from . import data_aws_dx_location
from . import data_aws_dx_locations
from . import data_aws_dx_router_configuration
from . import data_aws_dynamodb_table
from . import data_aws_dynamodb_table_item
from . import data_aws_ebs_default_kms_key
from . import data_aws_ebs_encryption_by_default
from . import data_aws_ebs_snapshot
from . import data_aws_ebs_snapshot_ids
from . import data_aws_ebs_volume
from . import data_aws_ebs_volumes
from . import data_aws_ec2_client_vpn_endpoint
from . import data_aws_ec2_coip_pool
from . import data_aws_ec2_coip_pools
from . import data_aws_ec2_host
from . import data_aws_ec2_instance_type
from . import data_aws_ec2_instance_type_offering
from . import data_aws_ec2_instance_type_offerings
from . import data_aws_ec2_instance_types
from . import data_aws_ec2_local_gateway
from . import data_aws_ec2_local_gateway_route_table
from . import data_aws_ec2_local_gateway_route_tables
from . import data_aws_ec2_local_gateway_virtual_interface
from . import data_aws_ec2_local_gateway_virtual_interface_group
from . import data_aws_ec2_local_gateway_virtual_interface_groups
from . import data_aws_ec2_local_gateways
from . import data_aws_ec2_managed_prefix_list
from . import data_aws_ec2_managed_prefix_lists
from . import data_aws_ec2_network_insights_analysis
from . import data_aws_ec2_network_insights_path
from . import data_aws_ec2_serial_console_access
from . import data_aws_ec2_spot_price
from . import data_aws_ec2_transit_gateway
from . import data_aws_ec2_transit_gateway_attachment
from . import data_aws_ec2_transit_gateway_connect
from . import data_aws_ec2_transit_gateway_connect_peer
from . import data_aws_ec2_transit_gateway_dx_gateway_attachment
from . import data_aws_ec2_transit_gateway_multicast_domain
from . import data_aws_ec2_transit_gateway_peering_attachment
from . import data_aws_ec2_transit_gateway_route_table
from . import data_aws_ec2_transit_gateway_route_tables
from . import data_aws_ec2_transit_gateway_vpc_attachment
from . import data_aws_ec2_transit_gateway_vpc_attachments
from . import data_aws_ec2_transit_gateway_vpn_attachment
from . import data_aws_ecr_authorization_token
from . import data_aws_ecr_image
from . import data_aws_ecr_repository
from . import data_aws_ecrpublic_authorization_token
from . import data_aws_ecs_cluster
from . import data_aws_ecs_container_definition
from . import data_aws_ecs_service
from . import data_aws_ecs_task_definition
from . import data_aws_efs_access_point
from . import data_aws_efs_access_points
from . import data_aws_efs_file_system
from . import data_aws_efs_mount_target
from . import data_aws_eip
from . import data_aws_eips
from . import data_aws_eks_addon
from . import data_aws_eks_addon_version
from . import data_aws_eks_cluster
from . import data_aws_eks_cluster_auth
from . import data_aws_eks_clusters
from . import data_aws_eks_node_group
from . import data_aws_eks_node_groups
from . import data_aws_elastic_beanstalk_application
from . import data_aws_elastic_beanstalk_hosted_zone
from . import data_aws_elastic_beanstalk_solution_stack
from . import data_aws_elasticache_cluster
from . import data_aws_elasticache_replication_group
from . import data_aws_elasticache_subnet_group
from . import data_aws_elasticache_user
from . import data_aws_elasticsearch_domain
from . import data_aws_elb
from . import data_aws_elb_hosted_zone_id
from . import data_aws_elb_service_account
from . import data_aws_emr_release_labels
from . import data_aws_emrcontainers_virtual_cluster
from . import data_aws_fsx_openzfs_snapshot
from . import data_aws_globalaccelerator_accelerator
from . import data_aws_glue_catalog_table
from . import data_aws_glue_connection
from . import data_aws_glue_data_catalog_encryption_settings
from . import data_aws_glue_script
from . import data_aws_grafana_workspace
from . import data_aws_guardduty_detector
from . import data_aws_iam_account_alias
from . import data_aws_iam_group
from . import data_aws_iam_instance_profile
from . import data_aws_iam_instance_profiles
from . import data_aws_iam_openid_connect_provider
from . import data_aws_iam_policy
from . import data_aws_iam_policy_document
from . import data_aws_iam_role
from . import data_aws_iam_roles
from . import data_aws_iam_saml_provider
from . import data_aws_iam_server_certificate
from . import data_aws_iam_session_context
from . import data_aws_iam_user
from . import data_aws_iam_user_ssh_key
from . import data_aws_iam_users
from . import data_aws_identitystore_group
from . import data_aws_identitystore_user
from . import data_aws_imagebuilder_component
from . import data_aws_imagebuilder_components
from . import data_aws_imagebuilder_container_recipe
from . import data_aws_imagebuilder_container_recipes
from . import data_aws_imagebuilder_distribution_configuration
from . import data_aws_imagebuilder_distribution_configurations
from . import data_aws_imagebuilder_image
from . import data_aws_imagebuilder_image_pipeline
from . import data_aws_imagebuilder_image_pipelines
from . import data_aws_imagebuilder_image_recipe
from . import data_aws_imagebuilder_image_recipes
from . import data_aws_imagebuilder_infrastructure_configuration
from . import data_aws_imagebuilder_infrastructure_configurations
from . import data_aws_inspector_rules_packages
from . import data_aws_instance
from . import data_aws_instances
from . import data_aws_internet_gateway
from . import data_aws_iot_endpoint
from . import data_aws_ip_ranges
from . import data_aws_ivs_stream_key
from . import data_aws_kendra_experience
from . import data_aws_kendra_faq
from . import data_aws_kendra_index
from . import data_aws_kendra_query_suggestions_block_list
from . import data_aws_kendra_thesaurus
from . import data_aws_key_pair
from . import data_aws_kinesis_firehose_delivery_stream
from . import data_aws_kinesis_stream
from . import data_aws_kinesis_stream_consumer
from . import data_aws_kms_alias
from . import data_aws_kms_ciphertext
from . import data_aws_kms_custom_key_store
from . import data_aws_kms_key
from . import data_aws_kms_public_key
from . import data_aws_kms_secret
from . import data_aws_kms_secrets
from . import data_aws_lakeformation_data_lake_settings
from . import data_aws_lakeformation_permissions
from . import data_aws_lakeformation_resource
from . import data_aws_lambda_alias
from . import data_aws_lambda_code_signing_config
from . import data_aws_lambda_function
from . import data_aws_lambda_function_url
from . import data_aws_lambda_functions
from . import data_aws_lambda_invocation
from . import data_aws_lambda_layer_version
from . import data_aws_launch_configuration
from . import data_aws_launch_template
from . import data_aws_lb
from . import data_aws_lb_hosted_zone_id
from . import data_aws_lb_listener
from . import data_aws_lb_target_group
from . import data_aws_lex_bot
from . import data_aws_lex_bot_alias
from . import data_aws_lex_intent
from . import data_aws_lex_slot_type
from . import data_aws_location_geofence_collection
from . import data_aws_location_map
from . import data_aws_location_place_index
from . import data_aws_location_route_calculator
from . import data_aws_location_tracker
from . import data_aws_location_tracker_association
from . import data_aws_location_tracker_associations
from . import data_aws_memorydb_acl
from . import data_aws_memorydb_cluster
from . import data_aws_memorydb_parameter_group
from . import data_aws_memorydb_snapshot
from . import data_aws_memorydb_subnet_group
from . import data_aws_memorydb_user
from . import data_aws_mq_broker
from . import data_aws_mq_broker_instance_type_offerings
from . import data_aws_msk_broker_nodes
from . import data_aws_msk_cluster
from . import data_aws_msk_configuration
from . import data_aws_msk_kafka_version
from . import data_aws_mskconnect_connector
from . import data_aws_mskconnect_custom_plugin
from . import data_aws_mskconnect_worker_configuration
from . import data_aws_nat_gateway
from . import data_aws_nat_gateways
from . import data_aws_neptune_engine_version
from . import data_aws_neptune_orderable_db_instance
from . import data_aws_network_acls
from . import data_aws_network_interface
from . import data_aws_network_interfaces
from . import data_aws_networkfirewall_firewall
from . import data_aws_networkfirewall_firewall_policy
from . import data_aws_networkmanager_connection
from . import data_aws_networkmanager_connections
from . import data_aws_networkmanager_core_network_policy_document
from . import data_aws_networkmanager_device
from . import data_aws_networkmanager_devices
from . import data_aws_networkmanager_global_network
from . import data_aws_networkmanager_global_networks
from . import data_aws_networkmanager_link
from . import data_aws_networkmanager_links
from . import data_aws_networkmanager_site
from . import data_aws_networkmanager_sites
from . import data_aws_opensearch_domain
from . import data_aws_organizations_delegated_administrators
from . import data_aws_organizations_delegated_services
from . import data_aws_organizations_organization
from . import data_aws_organizations_organizational_units
from . import data_aws_organizations_resource_tags
from . import data_aws_outposts_asset
from . import data_aws_outposts_assets
from . import data_aws_outposts_outpost
from . import data_aws_outposts_outpost_instance_type
from . import data_aws_outposts_outpost_instance_types
from . import data_aws_outposts_outposts
from . import data_aws_outposts_site
from . import data_aws_outposts_sites
from . import data_aws_partition
from . import data_aws_prefix_list
from . import data_aws_pricing_product
from . import data_aws_prometheus_workspace
from . import data_aws_qldb_ledger
from . import data_aws_ram_resource_share
from . import data_aws_rds_certificate
from . import data_aws_rds_cluster
from . import data_aws_rds_clusters
from . import data_aws_rds_engine_version
from . import data_aws_rds_orderable_db_instance
from . import data_aws_rds_reserved_instance_offering
from . import data_aws_redshift_cluster
from . import data_aws_redshift_cluster_credentials
from . import data_aws_redshift_orderable_cluster
from . import data_aws_redshift_service_account
from . import data_aws_redshift_subnet_group
from . import data_aws_redshiftserverless_credentials
from . import data_aws_region
from . import data_aws_regions
from . import data_aws_resourcegroupstaggingapi_resources
from . import data_aws_route
from . import data_aws_route_table
from . import data_aws_route_tables
from . import data_aws_route53_delegation_set
from . import data_aws_route53_resolver_endpoint
from . import data_aws_route53_resolver_firewall_config
from . import data_aws_route53_resolver_firewall_domain_list
from . import data_aws_route53_resolver_firewall_rule_group
from . import data_aws_route53_resolver_firewall_rule_group_association
from . import data_aws_route53_resolver_firewall_rules
from . import data_aws_route53_resolver_rule
from . import data_aws_route53_resolver_rules
from . import data_aws_route53_traffic_policy_document
from . import data_aws_route53_zone
from . import data_aws_s3_account_public_access_block
from . import data_aws_s3_bucket
from . import data_aws_s3_bucket_object
from . import data_aws_s3_bucket_objects
from . import data_aws_s3_bucket_policy
from . import data_aws_s3_control_multi_region_access_point
from . import data_aws_s3_object
from . import data_aws_s3_objects
from . import data_aws_sagemaker_prebuilt_ecr_image
from . import data_aws_secretsmanager_random_password
from . import data_aws_secretsmanager_secret
from . import data_aws_secretsmanager_secret_rotation
from . import data_aws_secretsmanager_secret_version
from . import data_aws_secretsmanager_secrets
from . import data_aws_security_group
from . import data_aws_security_groups
from . import data_aws_serverlessapplicationrepository_application
from . import data_aws_service
from . import data_aws_service_discovery_dns_namespace
from . import data_aws_service_discovery_http_namespace
from . import data_aws_service_discovery_service
from . import data_aws_servicecatalog_constraint
from . import data_aws_servicecatalog_launch_paths
from . import data_aws_servicecatalog_portfolio
from . import data_aws_servicecatalog_portfolio_constraints
from . import data_aws_servicecatalog_product
from . import data_aws_servicequotas_service
from . import data_aws_servicequotas_service_quota
from . import data_aws_ses_active_receipt_rule_set
from . import data_aws_ses_domain_identity
from . import data_aws_ses_email_identity
from . import data_aws_sesv2_dedicated_ip_pool
from . import data_aws_sfn_activity
from . import data_aws_sfn_state_machine
from . import data_aws_signer_signing_job
from . import data_aws_signer_signing_profile
from . import data_aws_sns_topic
from . import data_aws_sqs_queue
from . import data_aws_sqs_queues
from . import data_aws_ssm_document
from . import data_aws_ssm_instances
from . import data_aws_ssm_maintenance_windows
from . import data_aws_ssm_parameter
from . import data_aws_ssm_parameters_by_path
from . import data_aws_ssm_patch_baseline
from . import data_aws_ssoadmin_instances
from . import data_aws_ssoadmin_permission_set
from . import data_aws_storagegateway_local_disk
from . import data_aws_subnet
from . import data_aws_subnet_ids
from . import data_aws_subnets
from . import data_aws_transfer_server
from . import data_aws_vpc
from . import data_aws_vpc_dhcp_options
from . import data_aws_vpc_endpoint
from . import data_aws_vpc_endpoint_service
from . import data_aws_vpc_ipam_pool
from . import data_aws_vpc_ipam_pool_cidrs
from . import data_aws_vpc_ipam_pools
from . import data_aws_vpc_ipam_preview_next_cidr
from . import data_aws_vpc_peering_connection
from . import data_aws_vpc_peering_connections
from . import data_aws_vpcs
from . import data_aws_vpn_gateway
from . import data_aws_waf_ipset
from . import data_aws_waf_rate_based_rule
from . import data_aws_waf_rule
from . import data_aws_waf_subscribed_rule_group
from . import data_aws_waf_web_acl
from . import data_aws_wafregional_ipset
from . import data_aws_wafregional_rate_based_rule
from . import data_aws_wafregional_rule
from . import data_aws_wafregional_subscribed_rule_group
from . import data_aws_wafregional_web_acl
from . import data_aws_wafv2_ip_set
from . import data_aws_wafv2_regex_pattern_set
from . import data_aws_wafv2_rule_group
from . import data_aws_wafv2_web_acl
from . import data_aws_workspaces_bundle
from . import data_aws_workspaces_directory
from . import data_aws_workspaces_image
from . import data_aws_workspaces_workspace
from . import dataexchange_data_set
from . import dataexchange_revision
from . import datapipeline_pipeline
from . import datapipeline_pipeline_definition
from . import datasync_agent
from . import datasync_location_efs
from . import datasync_location_fsx_lustre_file_system
from . import datasync_location_fsx_openzfs_file_system
from . import datasync_location_fsx_windows_file_system
from . import datasync_location_hdfs
from . import datasync_location_nfs
from . import datasync_location_s3
from . import datasync_location_smb
from . import datasync_task
from . import dax_cluster
from . import dax_parameter_group
from . import dax_subnet_group
from . import db_cluster_snapshot
from . import db_event_subscription
from . import db_instance
from . import db_instance_automated_backups_replication
from . import db_instance_role_association
from . import db_option_group
from . import db_parameter_group
from . import db_proxy
from . import db_proxy_default_target_group
from . import db_proxy_endpoint
from . import db_proxy_target
from . import db_security_group
from . import db_snapshot
from . import db_snapshot_copy
from . import db_subnet_group
from . import default_network_acl
from . import default_route_table
from . import default_security_group
from . import default_subnet
from . import default_vpc
from . import default_vpc_dhcp_options
from . import detective_graph
from . import detective_invitation_accepter
from . import detective_member
from . import devicefarm_device_pool
from . import devicefarm_instance_profile
from . import devicefarm_network_profile
from . import devicefarm_project
from . import devicefarm_test_grid_project
from . import devicefarm_upload
from . import directory_service_conditional_forwarder
from . import directory_service_directory
from . import directory_service_log_subscription
from . import directory_service_radius_settings
from . import directory_service_region
from . import directory_service_shared_directory
from . import directory_service_shared_directory_accepter
from . import dlm_lifecycle_policy
from . import dms_certificate
from . import dms_endpoint
from . import dms_event_subscription
from . import dms_replication_instance
from . import dms_replication_subnet_group
from . import dms_replication_task
from . import dms_s3_endpoint
from . import docdb_cluster
from . import docdb_cluster_instance
from . import docdb_cluster_parameter_group
from . import docdb_cluster_snapshot
from . import docdb_event_subscription
from . import docdb_global_cluster
from . import docdb_subnet_group
from . import dx_bgp_peer
from . import dx_connection
from . import dx_connection_association
from . import dx_connection_confirmation
from . import dx_gateway
from . import dx_gateway_association
from . import dx_gateway_association_proposal
from . import dx_hosted_connection
from . import dx_hosted_private_virtual_interface
from . import dx_hosted_private_virtual_interface_accepter
from . import dx_hosted_public_virtual_interface
from . import dx_hosted_public_virtual_interface_accepter
from . import dx_hosted_transit_virtual_interface
from . import dx_hosted_transit_virtual_interface_accepter
from . import dx_lag
from . import dx_macsec_key_association
from . import dx_private_virtual_interface
from . import dx_public_virtual_interface
from . import dx_transit_virtual_interface
from . import dynamodb_contributor_insights
from . import dynamodb_global_table
from . import dynamodb_kinesis_streaming_destination
from . import dynamodb_table
from . import dynamodb_table_item
from . import dynamodb_table_replica
from . import dynamodb_tag
from . import ebs_default_kms_key
from . import ebs_encryption_by_default
from . import ebs_snapshot
from . import ebs_snapshot_copy
from . import ebs_snapshot_import
from . import ebs_volume
from . import ec2_availability_zone_group
from . import ec2_capacity_reservation
from . import ec2_carrier_gateway
from . import ec2_client_vpn_authorization_rule
from . import ec2_client_vpn_endpoint
from . import ec2_client_vpn_network_association
from . import ec2_client_vpn_route
from . import ec2_fleet
from . import ec2_host
from . import ec2_instance_state
from . import ec2_local_gateway_route
from . import ec2_local_gateway_route_table_vpc_association
from . import ec2_managed_prefix_list
from . import ec2_managed_prefix_list_entry
from . import ec2_network_insights_analysis
from . import ec2_network_insights_path
from . import ec2_serial_console_access
from . import ec2_subnet_cidr_reservation
from . import ec2_tag
from . import ec2_traffic_mirror_filter
from . import ec2_traffic_mirror_filter_rule
from . import ec2_traffic_mirror_session
from . import ec2_traffic_mirror_target
from . import ec2_transit_gateway
from . import ec2_transit_gateway_connect
from . import ec2_transit_gateway_connect_peer
from . import ec2_transit_gateway_multicast_domain
from . import ec2_transit_gateway_multicast_domain_association
from . import ec2_transit_gateway_multicast_group_member
from . import ec2_transit_gateway_multicast_group_source
from . import ec2_transit_gateway_peering_attachment
from . import ec2_transit_gateway_peering_attachment_accepter
from . import ec2_transit_gateway_policy_table
from . import ec2_transit_gateway_policy_table_association
from . import ec2_transit_gateway_prefix_list_reference
from . import ec2_transit_gateway_route
from . import ec2_transit_gateway_route_table
from . import ec2_transit_gateway_route_table_association
from . import ec2_transit_gateway_route_table_propagation
from . import ec2_transit_gateway_vpc_attachment
from . import ec2_transit_gateway_vpc_attachment_accepter
from . import ecr_lifecycle_policy
from . import ecr_pull_through_cache_rule
from . import ecr_registry_policy
from . import ecr_registry_scanning_configuration
from . import ecr_replication_configuration
from . import ecr_repository
from . import ecr_repository_policy
from . import ecrpublic_repository
from . import ecrpublic_repository_policy
from . import ecs_account_setting_default
from . import ecs_capacity_provider
from . import ecs_cluster
from . import ecs_cluster_capacity_providers
from . import ecs_service
from . import ecs_tag
from . import ecs_task_definition
from . import ecs_task_set
from . import efs_access_point
from . import efs_backup_policy
from . import efs_file_system
from . import efs_file_system_policy
from . import efs_mount_target
from . import efs_replication_configuration
from . import egress_only_internet_gateway
from . import eip
from . import eip_association
from . import eks_addon
from . import eks_cluster
from . import eks_fargate_profile
from . import eks_identity_provider_config
from . import eks_node_group
from . import elastic_beanstalk_application
from . import elastic_beanstalk_application_version
from . import elastic_beanstalk_configuration_template
from . import elastic_beanstalk_environment
from . import elasticache_cluster
from . import elasticache_global_replication_group
from . import elasticache_parameter_group
from . import elasticache_replication_group
from . import elasticache_security_group
from . import elasticache_subnet_group
from . import elasticache_user
from . import elasticache_user_group
from . import elasticache_user_group_association
from . import elasticsearch_domain
from . import elasticsearch_domain_policy
from . import elasticsearch_domain_saml_options
from . import elastictranscoder_pipeline
from . import elastictranscoder_preset
from . import elb
from . import elb_attachment
from . import emr_cluster
from . import emr_instance_fleet
from . import emr_instance_group
from . import emr_managed_scaling_policy
from . import emr_security_configuration
from . import emr_studio
from . import emr_studio_session_mapping
from . import emrcontainers_virtual_cluster
from . import emrserverless_application
from . import evidently_feature
from . import evidently_project
from . import evidently_segment
from . import fis_experiment_template
from . import flow_log
from . import fms_admin_account
from . import fms_policy
from . import fsx_backup
from . import fsx_data_repository_association
from . import fsx_file_cache
from . import fsx_lustre_file_system
from . import fsx_ontap_file_system
from . import fsx_ontap_storage_virtual_machine
from . import fsx_ontap_volume
from . import fsx_openzfs_file_system
from . import fsx_openzfs_snapshot
from . import fsx_openzfs_volume
from . import fsx_windows_file_system
from . import gamelift_alias
from . import gamelift_build
from . import gamelift_fleet
from . import gamelift_game_server_group
from . import gamelift_game_session_queue
from . import gamelift_script
from . import glacier_vault
from . import glacier_vault_lock
from . import globalaccelerator_accelerator
from . import globalaccelerator_endpoint_group
from . import globalaccelerator_listener
from . import glue_catalog_database
from . import glue_catalog_table
from . import glue_classifier
from . import glue_connection
from . import glue_crawler
from . import glue_data_catalog_encryption_settings
from . import glue_dev_endpoint
from . import glue_job
from . import glue_ml_transform
from . import glue_partition
from . import glue_partition_index
from . import glue_registry
from . import glue_resource_policy
from . import glue_schema
from . import glue_security_configuration
from . import glue_trigger
from . import glue_user_defined_function
from . import glue_workflow
from . import grafana_license_association
from . import grafana_role_association
from . import grafana_workspace
from . import grafana_workspace_api_key
from . import grafana_workspace_saml_configuration
from . import guardduty_detector
from . import guardduty_filter
from . import guardduty_invite_accepter
from . import guardduty_ipset
from . import guardduty_member
from . import guardduty_organization_admin_account
from . import guardduty_organization_configuration
from . import guardduty_publishing_destination
from . import guardduty_threatintelset
from . import iam_access_key
from . import iam_account_alias
from . import iam_account_password_policy
from . import iam_group
from . import iam_group_membership
from . import iam_group_policy
from . import iam_group_policy_attachment
from . import iam_instance_profile
from . import iam_openid_connect_provider
from . import iam_policy
from . import iam_policy_attachment
from . import iam_role
from . import iam_role_policy
from . import iam_role_policy_attachment
from . import iam_saml_provider
from . import iam_server_certificate
from . import iam_service_linked_role
from . import iam_service_specific_credential
from . import iam_signing_certificate
from . import iam_user
from . import iam_user_group_membership
from . import iam_user_login_profile
from . import iam_user_policy
from . import iam_user_policy_attachment
from . import iam_user_ssh_key
from . import iam_virtual_mfa_device
from . import identitystore_group
from . import identitystore_group_membership
from . import identitystore_user
from . import imagebuilder_component
from . import imagebuilder_container_recipe
from . import imagebuilder_distribution_configuration
from . import imagebuilder_image
from . import imagebuilder_image_pipeline
from . import imagebuilder_image_recipe
from . import imagebuilder_infrastructure_configuration
from . import inspector_assessment_target
from . import inspector_assessment_template
from . import inspector_resource_group
from . import inspector2_delegated_admin_account
from . import inspector2_enabler
from . import inspector2_organization_configuration
from . import instance
from . import internet_gateway
from . import internet_gateway_attachment
from . import iot_authorizer
from . import iot_certificate
from . import iot_indexing_configuration
from . import iot_logging_options
from . import iot_policy
from . import iot_policy_attachment
from . import iot_provisioning_template
from . import iot_role_alias
from . import iot_thing
from . import iot_thing_group
from . import iot_thing_group_membership
from . import iot_thing_principal_attachment
from . import iot_thing_type
from . import iot_topic_rule
from . import iot_topic_rule_destination
from . import ivs_channel
from . import ivs_playback_key_pair
from . import ivs_recording_configuration
from . import ivschat_logging_configuration
from . import ivschat_room
from . import kendra_data_source
from . import kendra_experience
from . import kendra_faq
from . import kendra_index
from . import kendra_query_suggestions_block_list
from . import kendra_thesaurus
from . import key_pair
from . import keyspaces_keyspace
from . import keyspaces_table
from . import kinesis_analytics_application
from . import kinesis_firehose_delivery_stream
from . import kinesis_stream
from . import kinesis_stream_consumer
from . import kinesis_video_stream
from . import kinesisanalyticsv2_application
from . import kinesisanalyticsv2_application_snapshot
from . import kms_alias
from . import kms_ciphertext
from . import kms_custom_key_store
from . import kms_external_key
from . import kms_grant
from . import kms_key
from . import kms_replica_external_key
from . import kms_replica_key
from . import lakeformation_data_lake_settings
from . import lakeformation_lf_tag
from . import lakeformation_permissions
from . import lakeformation_resource
from . import lakeformation_resource_lf_tags
from . import lambda_alias
from . import lambda_code_signing_config
from . import lambda_event_source_mapping
from . import lambda_function
from . import lambda_function_event_invoke_config
from . import lambda_function_url
from . import lambda_invocation
from . import lambda_layer_version
from . import lambda_layer_version_permission
from . import lambda_permission
from . import lambda_provisioned_concurrency_config
from . import launch_configuration
from . import launch_template
from . import lb
from . import lb_cookie_stickiness_policy
from . import lb_listener
from . import lb_listener_certificate
from . import lb_listener_rule
from . import lb_ssl_negotiation_policy
from . import lb_target_group
from . import lb_target_group_attachment
from . import lex_bot
from . import lex_bot_alias
from . import lex_intent
from . import lex_slot_type
from . import licensemanager_association
from . import licensemanager_license_configuration
from . import lightsail_bucket
from . import lightsail_certificate
from . import lightsail_container_service
from . import lightsail_container_service_deployment_version
from . import lightsail_database
from . import lightsail_disk
from . import lightsail_disk_attachment
from . import lightsail_domain
from . import lightsail_domain_entry
from . import lightsail_instance
from . import lightsail_instance_public_ports
from . import lightsail_key_pair
from . import lightsail_lb
from . import lightsail_lb_attachment
from . import lightsail_lb_certificate
from . import lightsail_lb_certificate_attachment
from . import lightsail_lb_https_redirection_policy
from . import lightsail_lb_stickiness_policy
from . import lightsail_static_ip
from . import lightsail_static_ip_attachment
from . import load_balancer_backend_server_policy
from . import load_balancer_listener_policy
from . import load_balancer_policy
from . import location_geofence_collection
from . import location_map
from . import location_place_index
from . import location_route_calculator
from . import location_tracker
from . import location_tracker_association
from . import macie_member_account_association
from . import macie_s3_bucket_association
from . import macie2_account
from . import macie2_classification_export_configuration
from . import macie2_classification_job
from . import macie2_custom_data_identifier
from . import macie2_findings_filter
from . import macie2_invitation_accepter
from . import macie2_member
from . import macie2_organization_admin_account
from . import main_route_table_association
from . import media_convert_queue
from . import media_package_channel
from . import media_store_container
from . import media_store_container_policy
from . import medialive_channel
from . import medialive_input
from . import medialive_input_security_group
from . import medialive_multiplex
from . import medialive_multiplex_program
from . import memorydb_acl
from . import memorydb_cluster
from . import memorydb_parameter_group
from . import memorydb_snapshot
from . import memorydb_subnet_group
from . import memorydb_user
from . import mq_broker
from . import mq_configuration
from . import msk_cluster
from . import msk_configuration
from . import msk_scram_secret_association
from . import msk_serverless_cluster
from . import mskconnect_connector
from . import mskconnect_custom_plugin
from . import mskconnect_worker_configuration
from . import mwaa_environment
from . import nat_gateway
from . import neptune_cluster
from . import neptune_cluster_endpoint
from . import neptune_cluster_instance
from . import neptune_cluster_parameter_group
from . import neptune_cluster_snapshot
from . import neptune_event_subscription
from . import neptune_global_cluster
from . import neptune_parameter_group
from . import neptune_subnet_group
from . import network_acl
from . import network_acl_association
from . import network_acl_rule
from . import network_interface
from . import network_interface_attachment
from . import network_interface_sg_attachment
from . import networkfirewall_firewall
from . import networkfirewall_firewall_policy
from . import networkfirewall_logging_configuration
from . import networkfirewall_resource_policy
from . import networkfirewall_rule_group
from . import networkmanager_attachment_accepter
from . import networkmanager_connect_attachment
from . import networkmanager_connection
from . import networkmanager_core_network
from . import networkmanager_customer_gateway_association
from . import networkmanager_device
from . import networkmanager_global_network
from . import networkmanager_link
from . import networkmanager_link_association
from . import networkmanager_site
from . import networkmanager_site_to_site_vpn_attachment
from . import networkmanager_transit_gateway_connect_peer_association
from . import networkmanager_transit_gateway_peering
from . import networkmanager_transit_gateway_registration
from . import networkmanager_transit_gateway_route_table_attachment
from . import networkmanager_vpc_attachment
from . import opensearch_domain
from . import opensearch_domain_policy
from . import opensearch_domain_saml_options
from . import opensearch_inbound_connection_accepter
from . import opensearch_outbound_connection
from . import opsworks_application
from . import opsworks_custom_layer
from . import opsworks_ecs_cluster_layer
from . import opsworks_ganglia_layer
from . import opsworks_haproxy_layer
from . import opsworks_instance
from . import opsworks_java_app_layer
from . import opsworks_memcached_layer
from . import opsworks_mysql_layer
from . import opsworks_nodejs_app_layer
from . import opsworks_permission
from . import opsworks_php_app_layer
from . import opsworks_rails_app_layer
from . import opsworks_rds_db_instance
from . import opsworks_stack
from . import opsworks_static_web_layer
from . import opsworks_user_profile
from . import organizations_account
from . import organizations_delegated_administrator
from . import organizations_organization
from . import organizations_organizational_unit
from . import organizations_policy
from . import organizations_policy_attachment
from . import pinpoint_adm_channel
from . import pinpoint_apns_channel
from . import pinpoint_apns_sandbox_channel
from . import pinpoint_apns_voip_channel
from . import pinpoint_apns_voip_sandbox_channel
from . import pinpoint_app
from . import pinpoint_baidu_channel
from . import pinpoint_email_channel
from . import pinpoint_event_stream
from . import pinpoint_gcm_channel
from . import pinpoint_sms_channel
from . import placement_group
from . import prometheus_alert_manager_definition
from . import prometheus_rule_group_namespace
from . import prometheus_workspace
from . import provider
from . import proxy_protocol_policy
from . import qldb_ledger
from . import qldb_stream
from . import quicksight_data_source
from . import quicksight_group
from . import quicksight_group_membership
from . import quicksight_user
from . import ram_principal_association
from . import ram_resource_association
from . import ram_resource_share
from . import ram_resource_share_accepter
from . import rds_cluster
from . import rds_cluster_activity_stream
from . import rds_cluster_endpoint
from . import rds_cluster_instance
from . import rds_cluster_parameter_group
from . import rds_cluster_role_association
from . import rds_global_cluster
from . import rds_reserved_instance
from . import redshift_authentication_profile
from . import redshift_cluster
from . import redshift_cluster_iam_roles
from . import redshift_endpoint_access
from . import redshift_endpoint_authorization
from . import redshift_event_subscription
from . import redshift_hsm_client_certificate
from . import redshift_hsm_configuration
from . import redshift_parameter_group
from . import redshift_partner
from . import redshift_scheduled_action
from . import redshift_security_group
from . import redshift_snapshot_copy_grant
from . import redshift_snapshot_schedule
from . import redshift_snapshot_schedule_association
from . import redshift_subnet_group
from . import redshift_usage_limit
from . import redshiftdata_statement
from . import redshiftserverless_endpoint_access
from . import redshiftserverless_namespace
from . import redshiftserverless_resource_policy
from . import redshiftserverless_snapshot
from . import redshiftserverless_usage_limit
from . import redshiftserverless_workgroup
from . import resourceexplorer2_index
from . import resourcegroups_group
from . import rolesanywhere_profile
from . import rolesanywhere_trust_anchor
from . import route
from . import route_table
from . import route_table_association
from . import route53_delegation_set
from . import route53_domains_registered_domain
from . import route53_health_check
from . import route53_hosted_zone_dnssec
from . import route53_key_signing_key
from . import route53_query_log
from . import route53_record
from . import route53_recoverycontrolconfig_cluster
from . import route53_recoverycontrolconfig_control_panel
from . import route53_recoverycontrolconfig_routing_control
from . import route53_recoverycontrolconfig_safety_rule
from . import route53_recoveryreadiness_cell
from . import route53_recoveryreadiness_readiness_check
from . import route53_recoveryreadiness_recovery_group
from . import route53_recoveryreadiness_resource_set
from . import route53_resolver_config
from . import route53_resolver_dnssec_config
from . import route53_resolver_endpoint
from . import route53_resolver_firewall_config
from . import route53_resolver_firewall_domain_list
from . import route53_resolver_firewall_rule
from . import route53_resolver_firewall_rule_group
from . import route53_resolver_firewall_rule_group_association
from . import route53_resolver_query_log_config
from . import route53_resolver_query_log_config_association
from . import route53_resolver_rule
from . import route53_resolver_rule_association
from . import route53_traffic_policy
from . import route53_traffic_policy_instance
from . import route53_vpc_association_authorization
from . import route53_zone
from . import route53_zone_association
from . import rum_app_monitor
from . import rum_metrics_destination
from . import s3_access_point
from . import s3_account_public_access_block
from . import s3_bucket
from . import s3_bucket_accelerate_configuration
from . import s3_bucket_acl
from . import s3_bucket_analytics_configuration
from . import s3_bucket_cors_configuration
from . import s3_bucket_intelligent_tiering_configuration
from . import s3_bucket_inventory
from . import s3_bucket_lifecycle_configuration
from . import s3_bucket_logging
from . import s3_bucket_metric
from . import s3_bucket_notification
from . import s3_bucket_object
from . import s3_bucket_object_lock_configuration
from . import s3_bucket_ownership_controls
from . import s3_bucket_policy
from . import s3_bucket_public_access_block
from . import s3_bucket_replication_configuration
from . import s3_bucket_request_payment_configuration
from . import s3_bucket_server_side_encryption_configuration
from . import s3_bucket_versioning
from . import s3_bucket_website_configuration
from . import s3_control_access_point_policy
from . import s3_control_bucket
from . import s3_control_bucket_lifecycle_configuration
from . import s3_control_bucket_policy
from . import s3_control_multi_region_access_point
from . import s3_control_multi_region_access_point_policy
from . import s3_control_object_lambda_access_point
from . import s3_control_object_lambda_access_point_policy
from . import s3_control_storage_lens_configuration
from . import s3_object
from . import s3_object_copy
from . import s3_outposts_endpoint
from . import sagemaker_app
from . import sagemaker_app_image_config
from . import sagemaker_code_repository
from . import sagemaker_device
from . import sagemaker_device_fleet
from . import sagemaker_domain
from . import sagemaker_endpoint
from . import sagemaker_endpoint_configuration
from . import sagemaker_feature_group
from . import sagemaker_flow_definition
from . import sagemaker_human_task_ui
from . import sagemaker_image
from . import sagemaker_image_version
from . import sagemaker_model
from . import sagemaker_model_package_group
from . import sagemaker_model_package_group_policy
from . import sagemaker_notebook_instance
from . import sagemaker_notebook_instance_lifecycle_configuration
from . import sagemaker_project
from . import sagemaker_servicecatalog_portfolio_status
from . import sagemaker_space
from . import sagemaker_studio_lifecycle_config
from . import sagemaker_user_profile
from . import sagemaker_workforce
from . import sagemaker_workteam
from . import scheduler_schedule
from . import scheduler_schedule_group
from . import schemas_discoverer
from . import schemas_registry
from . import schemas_registry_policy
from . import schemas_schema
from . import secretsmanager_secret
from . import secretsmanager_secret_policy
from . import secretsmanager_secret_rotation
from . import secretsmanager_secret_version
from . import security_group
from . import security_group_rule
from . import securityhub_account
from . import securityhub_action_target
from . import securityhub_finding_aggregator
from . import securityhub_insight
from . import securityhub_invite_accepter
from . import securityhub_member
from . import securityhub_organization_admin_account
from . import securityhub_organization_configuration
from . import securityhub_product_subscription
from . import securityhub_standards_control
from . import securityhub_standards_subscription
from . import serverlessapplicationrepository_cloudformation_stack
from . import service_discovery_http_namespace
from . import service_discovery_instance
from . import service_discovery_private_dns_namespace
from . import service_discovery_public_dns_namespace
from . import service_discovery_service
from . import servicecatalog_budget_resource_association
from . import servicecatalog_constraint
from . import servicecatalog_organizations_access
from . import servicecatalog_portfolio
from . import servicecatalog_portfolio_share
from . import servicecatalog_principal_portfolio_association
from . import servicecatalog_product
from . import servicecatalog_product_portfolio_association
from . import servicecatalog_provisioned_product
from . import servicecatalog_provisioning_artifact
from . import servicecatalog_service_action
from . import servicecatalog_tag_option
from . import servicecatalog_tag_option_resource_association
from . import servicequotas_service_quota
from . import ses_active_receipt_rule_set
from . import ses_configuration_set
from . import ses_domain_dkim
from . import ses_domain_identity
from . import ses_domain_identity_verification
from . import ses_domain_mail_from
from . import ses_email_identity
from . import ses_event_destination
from . import ses_identity_notification_topic
from . import ses_identity_policy
from . import ses_receipt_filter
from . import ses_receipt_rule
from . import ses_receipt_rule_set
from . import ses_template
from . import sesv2_configuration_set
from . import sesv2_dedicated_ip_assignment
from . import sesv2_dedicated_ip_pool
from . import sesv2_email_identity
from . import sesv2_email_identity_feedback_attributes
from . import sesv2_email_identity_mail_from_attributes
from . import sfn_activity
from . import sfn_state_machine
from . import shield_protection
from . import shield_protection_group
from . import shield_protection_health_check_association
from . import signer_signing_job
from . import signer_signing_profile
from . import signer_signing_profile_permission
from . import simpledb_domain
from . import snapshot_create_volume_permission
from . import sns_platform_application
from . import sns_sms_preferences
from . import sns_topic
from . import sns_topic_policy
from . import sns_topic_subscription
from . import spot_datafeed_subscription
from . import spot_fleet_request
from . import spot_instance_request
from . import sqs_queue
from . import sqs_queue_policy
from . import sqs_queue_redrive_allow_policy
from . import sqs_queue_redrive_policy
from . import ssm_activation
from . import ssm_association
from . import ssm_default_patch_baseline
from . import ssm_document
from . import ssm_maintenance_window
from . import ssm_maintenance_window_target
from . import ssm_maintenance_window_task
from . import ssm_parameter
from . import ssm_patch_baseline
from . import ssm_patch_group
from . import ssm_resource_data_sync
from . import ssm_service_setting
from . import ssoadmin_account_assignment
from . import ssoadmin_customer_managed_policy_attachment
from . import ssoadmin_instance_access_control_attributes
from . import ssoadmin_managed_policy_attachment
from . import ssoadmin_permission_set
from . import ssoadmin_permission_set_inline_policy
from . import ssoadmin_permissions_boundary_attachment
from . import storagegateway_cache
from . import storagegateway_cached_iscsi_volume
from . import storagegateway_file_system_association
from . import storagegateway_gateway
from . import storagegateway_nfs_file_share
from . import storagegateway_smb_file_share
from . import storagegateway_stored_iscsi_volume
from . import storagegateway_tape_pool
from . import storagegateway_upload_buffer
from . import storagegateway_working_storage
from . import subnet
from . import swf_domain
from . import synthetics_canary
from . import timestreamwrite_database
from . import timestreamwrite_table
from . import transcribe_language_model
from . import transcribe_medical_vocabulary
from . import transcribe_vocabulary
from . import transcribe_vocabulary_filter
from . import transfer_access
from . import transfer_server
from . import transfer_ssh_key
from . import transfer_tag
from . import transfer_user
from . import transfer_workflow
from . import volume_attachment
from . import vpc
from . import vpc_dhcp_options
from . import vpc_dhcp_options_association
from . import vpc_endpoint
from . import vpc_endpoint_connection_accepter
from . import vpc_endpoint_connection_notification
from . import vpc_endpoint_policy
from . import vpc_endpoint_route_table_association
from . import vpc_endpoint_security_group_association
from . import vpc_endpoint_service
from . import vpc_endpoint_service_allowed_principal
from . import vpc_endpoint_subnet_association
from . import vpc_ipam
from . import vpc_ipam_organization_admin_account
from . import vpc_ipam_pool
from . import vpc_ipam_pool_cidr
from . import vpc_ipam_pool_cidr_allocation
from . import vpc_ipam_preview_next_cidr
from . import vpc_ipam_scope
from . import vpc_ipv4_cidr_block_association
from . import vpc_ipv6_cidr_block_association
from . import vpc_network_performance_metric_subscription
from . import vpc_peering_connection
from . import vpc_peering_connection_accepter
from . import vpc_peering_connection_options
from . import vpn_connection
from . import vpn_connection_route
from . import vpn_gateway
from . import vpn_gateway_attachment
from . import vpn_gateway_route_propagation
from . import waf_byte_match_set
from . import waf_geo_match_set
from . import waf_ipset
from . import waf_rate_based_rule
from . import waf_regex_match_set
from . import waf_regex_pattern_set
from . import waf_rule
from . import waf_rule_group
from . import waf_size_constraint_set
from . import waf_sql_injection_match_set
from . import waf_web_acl
from . import waf_xss_match_set
from . import wafregional_byte_match_set
from . import wafregional_geo_match_set
from . import wafregional_ipset
from . import wafregional_rate_based_rule
from . import wafregional_regex_match_set
from . import wafregional_regex_pattern_set
from . import wafregional_rule
from . import wafregional_rule_group
from . import wafregional_size_constraint_set
from . import wafregional_sql_injection_match_set
from . import wafregional_web_acl
from . import wafregional_web_acl_association
from . import wafregional_xss_match_set
from . import wafv2_ip_set
from . import wafv2_regex_pattern_set
from . import wafv2_rule_group
from . import wafv2_web_acl
from . import wafv2_web_acl_association
from . import wafv2_web_acl_logging_configuration
from . import worklink_fleet
from . import worklink_website_certificate_authority_association
from . import workspaces_directory
from . import workspaces_ip_group
from . import workspaces_workspace
from . import xray_encryption_config
from . import xray_group
from . import xray_sampling_rule

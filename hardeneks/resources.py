from kubernetes import client, config
import sys


class Resources:
    def __init__(self, region, context, cluster, namespaces, debug):
        self.region = region
        self.context = context
        self.cluster = cluster
        self.namespaces = namespaces
        self.debug = debug
        #self.api_client_obj = config.new_client_from_config(context=self.context)

    def set_resources(self):
    
        #api_client_obj=config.new_client_from_config(context=self.context)
        
        self.cluster_roles = (
            client.RbacAuthorizationV1Api().list_cluster_role().items
        )
        self.cluster_role_bindings = (
            client.RbacAuthorizationV1Api().list_cluster_role_binding().items
        )
        self.resource_quotas = (
            client.CoreV1Api().list_resource_quota_for_all_namespaces().items
        )
        self.network_policies = (
            client.NetworkingV1Api()
            .list_network_policy_for_all_namespaces()
            .items
        )
        self.storage_classes = client.StorageV1Api().list_storage_class().items
        
        self.persistent_volumes = (
            client.CoreV1Api().list_persistent_volume().items
        )
        
        self.namespaceObjList = (
            client.CoreV1Api().list_namespace().items
        )

class NamespacedResources:
    def __init__(self, region, context, cluster, namespace, debug):
        self.namespace = namespace
        self.region = region
        self.cluster = cluster
        self.context = context
        self.debug = debug

    def set_resources(self):
        
        #api_client_obj=config.new_client_from_config(context=self.context)
        
        self.roles = (
            client.RbacAuthorizationV1Api()
            .list_namespaced_role(self.namespace)
            .items
        )
        self.pods = (
            client.CoreV1Api().list_namespaced_pod(self.namespace).items
        )
        self.role_bindings = (
            client.RbacAuthorizationV1Api()
            .list_namespaced_role_binding(self.namespace)
            .items
        )
        self.deployments = (
            client.AppsV1Api().list_namespaced_deployment(self.namespace).items
        )
        self.daemon_sets = (
            client.AppsV1Api().list_namespaced_daemon_set(self.namespace).items
        )
        self.stateful_sets = (
            client.AppsV1Api()
            .list_namespaced_stateful_set(self.namespace)
            .items
        )
        self.services = (
            client.CoreV1Api().list_namespaced_service(self.namespace).items
        )
        self.hpas = (
            client.AutoscalingV1Api()
            .list_namespaced_horizontal_pod_autoscaler(self.namespace)
            .items
        )

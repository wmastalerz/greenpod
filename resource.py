from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
#for i in ret.items:
#    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
for i in ret.items:
    for j in i.spec.containers:
        if j.resources.requests or j.resources.limits:
            sumreq=sumreq+j.rerources.requests
            print(i.spec.node_name, j.name, j.resources)



from kubernetes import client, config
import json
from requests import request

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

sumcpu=0
suffix = {"m": 0.001}
v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    for j in i.spec.containers:
        if j.resources.requests:
            rs=client.ApiClient().sanitize_for_serialization(j.resources)
            rsd=json.dumps(rs)
            res=json.loads(rsd)
            for key, value in res.items():
                if 'cpu' in res['requests']:
                    for mult in suffix:
                        if mult in res['requests']['cpu']:
                            valcpur=float(res['requests']['cpu'].replace(mult,"")) * suffix[mult]
                        else:
                            valcpur=float(res['requests']['cpu'])
                        sumcpu=sumcpu+valcpur
    print(i.spec.node_name, j.name, j.resources, sumcpu)



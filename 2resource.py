from kubernetes import client, config
import json
from requests import request

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

nores_cpu=0.1
sumcpu=0
container_nores=0
suffix = {"m": 0.001}
v1 = client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    for j in i.spec.containers:
        if j.resources.requests:
            rs=client.ApiClient().sanitize_for_serialization(j.resources)
            rsd=json.dumps(rs)
            res=json.loads(rsd)
            for key, value in res['requests'].items():
                if 'cpu' in key:
                    for mult in suffix:
                        if mult in res['requests']['cpu']:
                            valcpur=float(res['requests']['cpu'].replace(mult,"")) * suffix[mult]
                        else:
                            valcpur=float(res['requests']['cpu'])
                        sumcpu=sumcpu+valcpur
        else:
            container_nores=container_nores+1
    print(i.spec.node_name, j.name, j.resources, sumcpu)
sumcpu=sumcpu+container_nores*nores_cpu
print("Pod containers without resources:", container_nores)
print("Pod resources cpu (+0.1 vcpu per unrequested pod):", sumcpu)



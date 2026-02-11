import kopf
import kubernetes
import yaml

# Initialize Kubernetes API clients
kubernetes.config.load_incluster_config()  # use load_kube_config() if running locally
api = kubernetes.client.AppsV1Api()
core_api = kubernetes.client.CoreV1Api()

# Handler for creation of UDPMirror CR
@kopf.on.create('example.com', 'v1', 'udpmirrors')
def create_udpmirror(spec, name, namespace, logger, **kwargs):
    port = spec.get('port', 9999)
    buffer_size = spec.get('buffer-size', 1024)
    
    logger.info(f"Creating UDP Mirror Pod for {name} with port={port}, buffer-size={buffer_size}")
    
    pod_manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": f"{name}-pod",
            "labels": {"app": "udp-mirror"}
        },
        "spec": {
            "containers": [
                {
                    "name": "udp-mirror",
                    "image": "your-dockerhub-username/udp-mirror:latest",
                    "ports": [{"containerPort": port, "protocol": "UDP"}],
                    "env": [
                        {"name": "UDP_PORT", "value": str(port)},
                        {"name": "BUFFER_SIZE", "value": str(buffer_size)}
                    ]
                }
            ]
        }
    }

    # Create the pod
    core_api.create_namespaced_pod(namespace=namespace, body=pod_manifest)
    logger.info(f"Pod {name}-pod created successfully")

# Handler for deletion of UDPMirror CR
@kopf.on.delete('example.com', 'v1', 'udpmirrors')
def delete_udpmirror(spec, name, namespace, logger, **kwargs):
    pod_name = f"{name}-pod"
    try:
        core_api.delete_namespaced_pod(name=pod_name, namespace=namespace)
        logger.info(f"Pod {pod_name} deleted successfully")
    except kubernetes.client.exceptions.ApiException as e:
        if e.status == 404:
            logger.warning(f"Pod {pod_name} not found")
        else:
            raise

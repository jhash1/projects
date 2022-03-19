# from email.mime import image
# from pydoc import cli
# from kubernetes import client, config
# import requests

#load configuration from Kube context
# config.load_kube_config()
# v1 = client.CoreV1Api()

# def pod_collection():
#     '''
#     Collect pod name and pod image from Kubernetes cluster
#     '''
#     pod_namespace_list = v1.list_pod_for_all_namespaces(watch=False)
#     image_list = []
#     for i in pod_namespace_list.items:
#         image_list.append(i.spec.containers[0].image)
#         pod_name = i.metadata.name, 
#         pod_image = i.spec.containers[0].image
#     return image_list
        

# def image_check():
#     '''
#     Check Artifact Hub for K8s images
#     '''


    
#Artifact Hub for images

from pick import pick  # install pick using `pip install pick`

from kubernetes import client, config
from kubernetes.client import configuration

def main():
    contexts, active_context = config.list_kube_config_contexts()
    if not contexts:
        print("Cannot find any context in kube-config file.")
        return
    contexts = [context['name'] for context in contexts]
    active_index = contexts.index(active_context['name'])
    option, _ = pick(contexts, title="Pick the context to load",
                     default_index=active_index)


main()





# v1=client.CoreV1Api()
# pod=client.V1Pod()
# spec=client.V1PodSpec()
# pod.metadata=client.V1ObjectMeta
# container=client.V1Container()





# def main():
#     config.load_kube_config()

#     v1 = client.CoreV1Api()
#     count = 10
#     w = watch.Watch()
#     for event in w.stream(v1.list_namespace, timeout_seconds=10):
#         print("Event: %s %s" % (event['type'], event['object'].metadata.name))
#         count -= 1
#         if not count:
#             w.stop()
#     print("Finished namespace stream.")

#     for event in w.stream(v1.list_pod_for_all_namespaces, timeout_seconds=10):
#         print("Event: %s %s %s %s" % (
#             event['type'],
#             event['object'].kind,
#             event['object'].metadata.name,
#             event['object'].spec.containers[0].image)
#         )
#         count -= 1
#         if not count:
#             w.stop()
#     print("Finished pod stream.")


# if __name__ == '__main__':
#     main()
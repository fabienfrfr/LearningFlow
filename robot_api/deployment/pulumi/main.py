import pulumi
import pulumi_kubernetes as k8s

app_labels = { "app": "robot-control-app" }

deployment = k8s.apps.v1.Deployment(
    "robot-control-app",
    spec={
        "replicas": 3,
        "selector": { "matchLabels": app_labels },
        "template": {
            "metadata": { "labels": app_labels },
            "spec": {
                "containers": [{
                    "name": "robot-control-app",
                    "image": "robot-control-app:latest",
                    "ports": [{ "containerPort": 80 }],
                }]
            }
        }
    }
)

pulumi.export("name", deployment.metadata["name"])


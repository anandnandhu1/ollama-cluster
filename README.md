# ollama-cluster
This file should:
	•	Explain what the project is and why it’s built this way
	•	Give step-by-step instructions to:
	•	Build and push the image
	•	Deploy to EKS
	•	Run monitoring and logging
  •	load test

ARCHITECTURE DIAGRAM

Include the file: architecture.png

 Deployment steps:
  we use docker for build and we push to ECR
Amazon ECR:
 store the Docker images
 we use kubernetes for deploy into the eks
 i write deployment.yaml
         service.yaml
         ingress.yaml

LOADBALANCER AND AUTOSCALING AWS:
 forward the traffic using loadbalancer and scaling up the instances based on cpu metrics of exisiting nodes

HELM CHARTS:
   in helm charts we put updated manifest files so different teams easily use for the helmchats using install helm instead of writing every env they use simple in     this 

ARGOCD:
    we use argocd for continuously deployment

Monitoring & Logging:

Prometheus + Grafana
	•	Prometheus scrapes pod metrics
	•	Grafana visualizes CPU, memory, latency, GPU, etc.
  
  
ELK Stack with Filebeat
	•	Filebeat reads container logs
	•	Sends to Logstash → Elasticsearch
	•	Kibana for searching and viewing logs

 everything i have created seperate file please check 

 

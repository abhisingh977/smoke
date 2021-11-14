conda create -n smoke python=3.8
conda activate smoke
pip install flask==2.0.1 google-cloud-storage==1.42.2 gunicorn==20.0.4, firebase_admin
pip install opencv-python
pip install Pillow



Building the container image - gcloud builds submit --tag gcr.io//complaintsapi .

List the image - gcloud builds list --filter complaints

Checking logs of built image - gcloud builds log

Create Kubernetes Cluster - gcloud container clusters create complaints-gke --zone "us-west1-b" --machine-type "n1-standard-1" --num-nodes "1" --service-account srivatsan-gke@srivatsan-project.iam.gserviceaccount.com (Change to your service account)

Create Kubernetes Deployment - kubectl apply -f deployment.yaml

Get details on deployed application - kubectl get deployments

Get info of created pods via deployment - kubectl get pods

Decribe deployed pod - kubectl describe pod

Get pod logs - kubectl logs

Create service for deployment - kubectl apply -f service.yaml

Get service details - kubectl get services

Add nodes to cluster - gcloud container clusters resize complaints-gke --num-nodes 3 --zone us-west1-b

Get details on cluster - gcloud container clusters list

Scale pod replicas - kubectl scale deployment complaints --replicas 2

Auto Scale setting in deployment - kubectl autoscale deployment complaints --max 6 --min 2 --cpu-percent 50

Get details on horizontal pod autoscaler - kubectl get hpa
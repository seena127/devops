#Initiate terraform and login with aws cli and github accounts in visual studio code

#Move to the repository related to terraform

Terraform init

Terraform plan
#check for any available errors and rectify it

Terraform apply
#After apply EKS will be created with required IAM roles and responsibilities we can additional roles for launching pods too

#Add credentials related to docker hub and aws account in git repository

#git repository-> setting-> secrets -> Add 	KUBE_CONFIG_DATA, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DOCKER_PASSWORD

#For kUBE_CONFIG_DATA use the following command to retrieve after terraform apply

aws eks --region us-east-1 update-kubeconfig --name demo --kubeconfig kubeconfig.yaml --alias <your-alias>

#in region include region in which eks has been launched and in place of "demo" include the name of eks cluster

#After this process perform git operation

git add .

git commit -m "K8S operation devops"

git push

#After this perform kubectl commands to check for pod and remote in to pod to check for application launch

kubectl get pod

kubectl describe pod <pod-name>

kubectl exec -it <pod-name> /bin/sh

curl http://0.0.0.0:5000/items

#path will be displayed in home page for it
sqlite3 /path/to/database.db

#To put values the table inside it use

INSERT INTO Item (name, description) VALUES ('New Item', 'Description');

curl http://0.0.0.0:5000/items









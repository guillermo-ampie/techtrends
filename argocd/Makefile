install:
	-kubectl create namespace argocd
	kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

update-argocd-server:
	kubectl apply -f argocd-server-nodeport.yaml

get-initial-admin-password:
	kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d | tee argocd-passwd.txt
	@echo

init: install update-argocd-server get-initial-admin-password

deploy-staging:
	kubectl apply -f  helm-techtrends-staging.yaml

deploy-prod:
	kubectl apply -f  helm-techtrends-prod.yaml

deploy: deploy-prod deploy-staging

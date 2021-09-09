ns:
	kubectl apply -f namespace.yaml

deploy:
	kubectl apply -f deploy.yaml

svc:
	kubectl apply -f service.yaml

all: ns deploy svc

clean:
	-kubectl delete -f service.yaml
	-kubectl delete -f deploy.yaml
	-kubectl delete -f namespace.yaml

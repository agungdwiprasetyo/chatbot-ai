.PHONY : docker deploy

GCP_PROJECT_ID = mantab-tenanan-le
APP_NAME = chatbot-ai
ts = $(shell date +%Y%m%d%H%M%S)
IMAGE_TAG = $(ts)

docker:
	docker build -t $(APP_NAME):latest .

deploy:
	docker build -t $(APP_NAME):$(IMAGE_TAG) .
	docker tag $(APP_NAME):$(IMAGE_TAG) gcr.io/$(GCP_PROJECT_ID)/$(APP_NAME):$(IMAGE_TAG)
	docker push gcr.io/$(GCP_PROJECT_ID)/$(APP_NAME):$(IMAGE_TAG)
	kubectl set image deployment/$(APP_NAME) $(APP_NAME)-sha256=gcr.io/$(GCP_PROJECT_ID)/$(APP_NAME):$(IMAGE_TAG)
.DEFAULT_GOAL:=docker-run

IMAGE_NAME?=sumeetbansal007/jira-production-support
IMAGE_TAG?=ffa6d707
PORT?=8000

.PHONY: docker-build
docker-build:
	docker build -t ${IMAGE_NAME}:${IMAGE_TAG}  .

.PHONY: docker-run
docker-run:
	docker run  -p ${PORT}:${PORT}  --env-file .env ${IMAGE_NAME}:${IMAGE_TAG} 

.PHONY: run
run:
	python3 run.py

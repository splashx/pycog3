BUNDLE_NAME          = testbundle
BUNDLE_VERSION      ?= 0.1.0
IMAGE_TAG            = cog/$(BUNDLE_NAME):$(BUNDLE_VERSION)

.PHONY: docker docker-clean docker-shell docker-fresh test

test: docker
	docker run -it cog/$(BUNDLE_NAME):$(BUNDLE_VERSION) python -m unittest discover -v tests/

docker: Dockerfile .dockerignore
	docker build -q --rm -t $(IMAGE_TAG) .

docker-clean:
	docker rmi -f `docker images -q $(IMAGE_TAG)` || true

docker-shell:
	docker run --rm -it $(IMAGE_TAG) sh

docker-fresh: docker-clean docker

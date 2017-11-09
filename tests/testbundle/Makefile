BUNDLE_NAME          = testbundle
BUNDLE_VERSION      ?= 0.1.0
IMAGE_TAG            = cog/$(BUNDLE_NAME):$(BUNDLE_VERSION)

.PHONY: docker docker-clean docker-shell docker-fresh

docker: Dockerfile .dockerignore
	mkdir -p pycog3/cog
	mkdir -p pycog3/bin
	cp ../../setup.py  pycog3/
	cp ../../requirements.txt  pycog3/
	cp -R ../../cog pycog3/
	cp -R ../../bin pycog3/
	docker build --rm -t $(IMAGE_TAG) .
	rm -rf pycog3/

docker-clean:
	docker rmi -f `docker images -q $(IMAGE_TAG)` || true

docker-shell:
	docker run --rm -it $(IMAGE_TAG) sh

docker-fresh: docker-clean docker

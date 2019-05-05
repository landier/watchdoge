build:
	docker-compose build --parallel

run: build
	docker-compose up

clean:
	docker rmi $$(docker images --filter "label=project=coincoin" --quiet)
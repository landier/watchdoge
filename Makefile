build:
	docker-compose build --parallel

dev: build
	docker-compose up redis

redis-cli:
	docker run -it  --network coincoin_backend redis redis-cli -h coincoin_redis_1

run: build
	docker-compose up

deploy: build
	docker stack deploy -c docker-compose.yml coin

clean:
	docker-compose down
	docker rmi $$(docker images --filter "label=project=coincoin" --quiet)

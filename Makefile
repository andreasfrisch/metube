build-docker-images:
	docker build -t "metube/web" .

compose-up:
	docker-compose -p metube up -d


compose-down:
	docker-compose -p metube stop

remove-docker-containers:
	docker rm $(docker ps -qa)

remove-docker-images:
	docker rmi $(docker images -qa)

docker-clean-all: compose-down docker-remove-containers docker-remove-images
	echo "Done"



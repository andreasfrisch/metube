build-metube-web:
	docker build -t "metube/web" .

compose-up:
	docker-compose -p metube up -d


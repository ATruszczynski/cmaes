NAME=cma_es
id=$(sudo docker create $(NAME))

build:
	sudo docker build -t $(NAME) .
run:
	sudo docker run --rm $(NAME)
export:
	sudo docker cp $id:path - > local-tar-file
	sudo docker rm -v $(id)
d:
	echo $(id)
	sudo docker container inspect $(id)
rbuild:
	make build
	make run
	make export

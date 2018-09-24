default: run 

run: build
		docker run -p 5000:5000 pg-api python app.py

debug: build
		docker run -p 5000:5000 pg-api python app.py --log DEBUG

test: build
		docker run pg-api python test_app.py

build: Dockerfile
		docker build -t pg-api .

.PHONY: default run build

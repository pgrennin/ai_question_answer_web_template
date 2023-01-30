docker stop omniscient-web
docker rm omniscient-web

docker build -t omniscient -f dev.Dockerfile .

docker run -i -t -p 8000:5000 -d --name omniscient-web -v "$(pwd)":/app omniscient

# then go to http://localhost:8000
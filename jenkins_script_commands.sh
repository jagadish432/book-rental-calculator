
# this alone is not sufficient for jenkins, jenkins configuration on the server/local has to be made manually.

#but these below commands are what needed in the jenkins' pipeline configure's execute shell section to build the code.

CONTAINER_NAME=python-flask-book-rental-calculator:latest
COUNT=$(docker ps -a | grep "$CONTAINER_NAME" | wc -l)
if (($COUNT > 0)); then
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
fi

ls -la
docker --version

docker build -t python-flask-book-rental-calculator:latest .
docker run --name flask-book-app --env-file book-rental-calculator/envs/dev -d -p 5020:5020 python-flask-book-rental-calculator:latest

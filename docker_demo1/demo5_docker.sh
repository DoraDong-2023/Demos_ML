# download and open docker software first
# generate requirements.txt
pip freeze > requirements.txt
# build docker
sudo docker build -t demo:v1 .
# run docker
sudo docker run demo:v1
# show absolute path
pwd
# load data
sudo docker run -v /home/user/docker_demo/logs:/logs demo:v1



# other resources
# official document: https://docs.docker.com/
# handbook: https://www.runoob.com/docker/docker-command-manual.html


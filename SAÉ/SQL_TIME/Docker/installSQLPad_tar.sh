#!/bin/bash
export user=$(whoami)
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -q)
docker load --input /home/etudiants/$user/Ubox_Travail/pedago-iut/INFO/Public/ENSEIGNEMENT/BUT1/R1_05/Docker/sqlpad.tar
docker run -p 3000:3000 --name SQLPAD -e 'SQLPAD_ADMIN=admin' -e 'SQLPAD_ADMIN_PASSWORD=admin' -e 'SQLPAD_CONNECTIONS__SQLCNX__name=SQLServerIUT' -e 'SQLPAD_CONNECTIONS__SQLCNX__driver=sqlserver' -e 'SQLPAD_CONNECTIONS__SQLCNX__host=164.81.120.19' -e 'SQLPAD_CONNECTIONS__SQLCNX__database=master' -e 'SQLPAD_CONNECTIONS__SQLCNX__username=BUT1' -e 'SQLPAD_CONNECTIONS__SQLCNX__password=IUT' --detach sqlpad/sqlpad
docker images
docker ps
ip a show docker0
echo !OK!



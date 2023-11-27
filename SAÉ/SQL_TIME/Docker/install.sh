#!/bin/bash
export user=$(whoami)
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -q)
docker load --input /home/etudiants/$user/Ubox_Travail/pedago-iut/INFO/Public/ENSEIGNEMENT/BUT1/R1_05/Docker/mssql2017_custom.tar
docker run -p 1433:1433 -d --name MSSQL mssqlimage
docker images
docker ps
ip a show docker0
echo !OK!



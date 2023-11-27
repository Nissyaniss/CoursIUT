#!/bin/bash
cd
docker cp ./BD.bak MSSQL:/var/opt/mssql/data/
docker exec -it MSSQL ls -l /var/opt/mssql/data/BD.bak
echo !OK!

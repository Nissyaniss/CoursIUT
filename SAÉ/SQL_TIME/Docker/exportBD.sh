#!/bin/bash
cd
docker cp MSSQL:/var/opt/mssql/data/BD.bak ./
ls -l ./BD.bak
echo !OK!

#!/bin/bash

mkdir -p /backapp/$USER	
cd /backapp/$USER

tar -czf "bk_learn$(date "+%m.%d.%y").tar.gz" /home/mata/learn/
tar -czf "bk_doc$(date "+%m.%d.%y").tar.gz" /home/mata/Документы/


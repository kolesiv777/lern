#!/bin/bash
count=0
while [[ $count -le 7 ]]
	do	
		mkdir "/tmp/directory-$(date +"%Y.%m.%d_%H.%M")"
		((count++))
		sleep 420
	done


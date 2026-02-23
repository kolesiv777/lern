#!/bin/bash
if [[ -L "$1" ]];then
        readlink -f "$1"
	mv "$1" /home/$USER/TRASH
elif [[ -f "$1" ]]; then
	if [[ $(stat -c %h "$1") -gt 1  ]];then
		gzip "$1"
                mv "$1.gz" /home/$USER/TRASH
	else
		gzip "$1"
                mv "$1.gz" /home/$USER/TRASH
	fi
elif [[ -d "$1" ]]; then
        tar czf "$1.tar.gz" "$1"
        mv "$1.tar.gz" /home/$USER/TRASH
else
        echo "xz brat"
fi

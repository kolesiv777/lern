#!/bin/bash
case "$1" in
	*.gz) gunzip "$1" ;;
	*.bz2) bunzip2 "$1" ;;
	*.lzma) unlzma "$1" ;;
	*.zip) if which unzip &> /dev/null; then 
			unzip "$1"
		 else
			 echo "не установлен unzip"
		 fi;;
esac

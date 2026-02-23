#!/bin/bash

#первый вариант +2 будет выдавать только четные
num=0
while [ $num -le 10  ]
	do
		echo $num
		num=$(( num + 2 ))
	done	
#второй с if
num=0
while [ $num -le 10  ]
	do
		if (( num % 2 == 0 ))
			then
			echo $num
		fi
		num=$(( num + 1 ))
	done	
	

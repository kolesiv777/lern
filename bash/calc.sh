#!/bin/bash

read -p "1 number " x
read -p "operator " y
read -p "2 number " z

case $y in

"+") echo "$x + $z = " $(expr "$x" + "$z");;
"-") echo "$x - $z = " $(expr "$x" - "$z");;
"*") echo "$x * $z = " $(expr "$x" \* "$z");;
"/") if [[ $z -ne 0 ]];
     then
	echo "$x / $z = $(echo "scale=2; $x / $z" | bc)"
     else
	echo "you dolboeb na 0 nejizia delit"
     fi;;
"**") echo "$x ** $z = $((x ** z))" ;;
*) echo "co blia" ;;
esac


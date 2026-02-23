#!/bin/bash
head -n 1 "$1" > "$1_clean"
tail -n +2 "$1" | sed 's/#.*$//' >> "$1_clean"
echo "$1_clean"

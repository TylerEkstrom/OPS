#!/bin/bash

$folders = "temp1", "temp2", "temp3", "temp4"

foreach ($folder in $folders){
 mkdir -p $folder
 echo test > "$folder/test.txt"
}
#!/bin/bash

$folders = "temp1", "temp2", "temp3", "temp4"

foreach ($folder in $folders){
 mkdir $folder # stretch goal is there somethig you can do here to say if the folder exists dont create it
 echo test > "$folder/test.txt"
}
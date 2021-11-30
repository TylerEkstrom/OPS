# This file creates a txt file with network information about the device
# author: Tyler 
# Last updated 11/30/2021    

#!/usr/bin/env bash
 
echo "`ifconfig`" > output.txt
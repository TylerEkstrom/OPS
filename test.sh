#!/usr/env bash

$OS = "`uname`"

if [[$OS == "Linx"]]; then
 ifconfig
else
  ipconfig
fi

read -p "All done"
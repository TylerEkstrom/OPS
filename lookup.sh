#!/bin/bash

##not done work in progress

function lookups(){
read = $target;
whois $target;
dig $target;
host $target;
nslookup $target;
}
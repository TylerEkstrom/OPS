#!/bin/bash

function lookups(){
read = $target;
whois $target;
dig $target;
host $target;
nslookup $target;
}
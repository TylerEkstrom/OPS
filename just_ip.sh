#! /usr/bin/env powershell

function getIP(){
ipconfig | Select-String "IPv4 Address"
}
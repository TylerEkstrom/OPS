#! /usr/bin/env powershell

function getLogOn() {
$Log_on = Get-winEvent -MaxEvents 100 -Logname security | where-object{$_.ID -eq 4625 -or $_.ID -eq 4624} 
echo $Log_on > Log_on.txt
}
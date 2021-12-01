#! /usr/bin/env powershell

function getCamAccess(){
$camera_access = Get-WinEvent -Maxevents 100 -LogName System | Where-Object {$_.ID -ep 1 -or $_.ID -eq 2 } 
echo $camera_access > cam_access.LogName
}


#!/bin/bash

function backup(){
@ECHO OFF
mkdir C:\Users\Public\Backup
mkdir C:\Users\Public\Backup\Desktop
mkdir C:\Users\Public\Backup\Documents
xcopy /s C:\Users\User\Desktop C:\Users\Public\Backup\Desktop
xcopy /s C:\Users\User\Documents C:\Users\Public\Backup\Documents
}
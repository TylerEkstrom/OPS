#! /usr/bin/env powershell

function killer(){
  get-process
  $whatkill = Read-Host -Prompt 'Choose a sacrifice'
  stop-process $whatkill
  echo "The deed is done."
}
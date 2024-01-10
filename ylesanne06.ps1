# Markus Laanemae
# muutujad ja massiiv

#massiiv Array
$emailid = Get-Content -Path "C:\Users\mlaanemae\Desktop\emailid.txt"
$skriptiAsukoht = $MyInvocation.MyCommand.Path
$dir = Split-Path $skriptiAsukoht
$emailid = Get-Content -path $dir\emailid.txt
$emailid_massiivis = $emailid.Split(",")
"Esimene email on: "+$emailid_massiivis[0] #esimene
"viimane email on: "+$emailid_massiivis[$emailid_massiivis.Length-1] #viimane
"Kokku emaile: "+ $emailid_massiivis.Length #kokku

#muutuja 
$nimi = "Markus"
$email = "laanemae.markus1@gmail.com"
${kuu paev} = Get-Date

$nimi+" "+$email
${kuu paev}
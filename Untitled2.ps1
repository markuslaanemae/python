# 1.11.23 Markus Laanemäe
# nimi – siia alla korja kasutajanimed kujul Mari Maasikas
# kasutajanimi – siia korda kasutajanimi, mis koosneb eesnime esitähest ja perenimest, kujul mmaasikas
# email – mari.maasikas@hkhk.edu.ee
# parool – 5 kohaline parool, mis genereeritakse perenime kolmest tähest ja kahest numbrist


$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
 
# Import-Csv $dir\users.csv | Format-Table

#loob uue csv faili
$csv_header = @("full_name;account;email;pw")
$csv_header | Set-Content $dir\emailaccounts.csv
$users = Import-Csv $dir\users.csv
ForEach($user in $users) {

        $full_name = $user.first_name+" "+$user.Last_name
        $account = ($user.first_name[0]+$user.last_name).ToLower()
        $email = ($user.last_name+"@hkhk.edu.ee").ToLower()
        $pw = $user.last_name.Substring(0,3)+(Get-Random -Minimum 10 -Maximum 99)

        $row = "$full_name;$account;$email;$pw"
        Add-Content $dir\emailaccounts.csv $row





        }
# 1.11.23 Markus Laanemae
# Koosta skript, mis leiab ja kuvab arvutinime
# Täienda skripti, mis leiab arvutis olevad loogilised kettad (kõvakettad) ning väljastab nende koguarvu
# Täienda skripti, mis leiab kõigi ketaste (isegi kui juhuslikult on su arvutis ainult üks ketas) vaba ruumi protsendiliselt
# Täienda koodi nii, et kuvatakse ketaste protsendid ja kui vaba kettamaht on ALLA 50%, siis kuvatakse tekst “Hakkab täis saama”.

# kuvab masina nime
hostname

# leiab kettad ja koguarvu
$logicalDisks = Get-WmiObject -Class Win32_LogicalDisk
$logicalDisks.count

#"ketaste arv: "+$koguarv+" tk"


foreach ($disk in $logicalDisks) {
    $driveLetter = $disk.DeviceID
    $driveletter
    #$diskSizeGB = [math]::Round($disk.Size / 1GB, 2)
    
    
    #Write-Host "Size: $diskSizeGB GB"
    #Write-Host "-------------------"
}

$date = Get-Date
$date1 = $date.AddMinutes(-30)
$events = Get-WinEvent -LogName *PowerShell* | Where-Object { $_.TimeCreated -ge $date1 }
$events | Select-Object TimeCreated, Id, Message
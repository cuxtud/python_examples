#Upgrade Morpheus Agent 
$script =  "${env:commonprogramfiles(x86)}\upgrade_morph_agent.ps1"
'
$insf = "${env:commonprogramfiles(x86)}\install_morph_agent.ps1"
echo "Installer..."
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12	
} 
Catch {
}
$success = $false
$attempts = 0
Do {
    try {
    $ws = (New-Object System.Net.WebClient).OpenRead("<%=morpheus.applianceUrl%>api/server-script/agentInstall?apiKey=<%=server.apiKey%>")
    $f = [System.IO.File]::OpenWrite($insf)
    $br=1
    $bf = [array]::createInstance([byte],1000)
    Do {
        $br = $ws.Read($bf,0,$bf.Length)
        $f.Write($bf,0,$br)
    }
    While ($br -gt 0)
    $ws.Flush()
    $f.Flush()
    $ws.Close()
    $f.Close()
    $success = $true
    break
    } 
    Catch {
        $attempts++
        Start-Sleep -s 10
    }
} While ($attempts -lt 3)
if($success) {
    echo "Download successful"
} else {
    echo "Download failed after 3 attempts"
    ${logoff ? "logoff" : ""}
    exit 1	
}
try {
    C:\windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -File $insf	
}
Catch {
    ${logoff ? "logoff" : ""}
    exit 1
}
' | out-file $script -Force
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-file `"$script`""
$Trigger = New-ScheduledTaskTrigger -Once -At (get-date).AddSeconds(10); $Trigger.EndBoundary = (get-date).AddSeconds(30).ToString('s')
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DeleteExpiredTaskAfter 00:00:30
Register-ScheduledTask -Force -user system -TaskName "Upgrade Morpheus Agent" -Action $Action -Trigger $Trigger -Settings $Settings -RunLevel Highest
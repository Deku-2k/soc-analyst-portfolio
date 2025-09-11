# Windows KQL Queries

## Excessive 4625 Failures (potential brute force)
```kql
SecurityEvent
| where EventID == 4625
| summarize Failures=count() by TargetUserName, bin(TimeGenerated, 5m)
| where Failures > 10
```

## PowerShell EncodedCommand
```kql
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has "-EncodedCommand"
```

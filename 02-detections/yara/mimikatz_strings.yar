rule Mimikatz_String_Artifact
{
    meta:
        author = "Your Name"
        description = "Detects typical Mimikatz strings"
        date = "2025-09-11"
    strings:
        $s1 = "mimikatz" nocase
        $s2 = "sekurlsa::logonpasswords" nocase
    condition:
        1 of ($s*)
}

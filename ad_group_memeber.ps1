#imports
Import-Module Microsoft.Graph.Groups
Import-Module Microsoft.Graph.Authentication


#parent group id (SharePoint - All Facility ADR Folders)
$parentGroupId = "9f80b1cf-7e6f-4a81-9601-26e3db9dd9fe"

# connect to graph
Connect-Graph -Scopes Group.ReadWrite.All

# get token
$token = Get-MgContextAccessToken

# get all groups with consistency level
$groups = Get-MgGroup -Headers @{ConsistencyLevel="eventual"} -All

# filter groups using whherre object
$filteredGroups = $groups | Where-Object { $_.DisplayName -like "fld_*_adr" }

# itterate throough groups and add to parent group
foreach ($group in $filteredGroups) {
    try {
        # Construct the API URL
        $apiUrl = "https://graph.microsoft.com/v1.0/groups/$parentGroupId/members/$($group.Id)/$ref"

        # Make the API request
        Invoke-RestMethod -Uri $apiUrl -Method PUT -Headers @{
            "Authorization" = "Bearer $($token)"
            "Content-Type" = "application/json"
        }

        Write-Host "Added group '$($group.DisplayName)' to parent group (membership)."
    }
    catch {
        Write-Warning "Failed to add group '$($group.DisplayName)' to parent group. Error: $($_.Exception.Message)"
    }
}

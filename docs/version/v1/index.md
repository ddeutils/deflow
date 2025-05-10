# Version 1

A Data Framework Version 1. This concept use workflow to pass running date on all
process that config in its stream.

```text
core
 ╰─ stream
     ╰─ group
         ╰─ process
```

!!! note

    The audit date control by the steam layer and passing thai audit date to all
    its process after prepare with its frequency.


## Concept

```mermaid
flowchart TD
    start[Start] --> getStreamInfo["Get stream information\n(get-stream)"]
    getStreamInfo --> startStream["Start stream\n(start-stream)"]
    startStream --> priorityLoop["For each priority in priority-groups"]

    priorityLoop --> getGroups["Get Groups from Priority\n(get-groups)"]
    getGroups --> groupLoop["For each group in groups"]

    groupLoop --> triggerGroupWorkflow["Trigger group-workflow\nParams: name, stream, audit-date"]
    triggerGroupWorkflow --> endTriggerGroup["End trigger Group"]
    endTriggerGroup --> groupLoopCheck{"More groups?"}

    groupLoopCheck -- Yes --> groupLoop
    groupLoopCheck -- No --> endTriggerPriorityGroup["End trigger Priority Group"]

    endTriggerPriorityGroup --> priorityLoopCheck{"More priorities?"}
    priorityLoopCheck -- Yes --> priorityLoop
    priorityLoopCheck -- No --> clearLog["Clear log"]

    clearLog --> alert["Alert with mail or notify-services"]
    alert --> finish[End]
```

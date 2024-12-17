# IncidentTasks

The IncidentTasks application is a small example sketching the implementation of the user stories described in the following section.

# Requirements

## User Stories (simplified)

### Create Incidents

* As a *registered user* I want to *create an Incident* describing a situation that I need assistance with to raise awareness for it.

#### Acceptance Criteria

* New Incidents can be created by registered users
* Unregistered users can't create new incidents
* Incidents contain a description of the incident situation.

### Creating Tasks

* As *incident response manager* I want to *create tasks* that express the required actions that need to be performed to resolve an incident. 
* As *incident manager* I want to *assign responsible response agents to new tasks* so that planned tasks get executed by the responsible agents.   

#### Acceptance Criteria

* New tasks can be created by users with the privilege *incident response manager*
* Tasks are assigned to an incident
* New tasks have a status of *OPEN*
* Tasks contain a description of the required actions to be taken (which should not be empty)
* Tasks contain an *assigned User* (which can be empty)


### Tracking Incident and Task Status

* As *incident response manager* I want to *manage the status of incidents*, so I can set resolved issues to *RESOLVED*.
* As *assigned response agent* I want to *update the task status* to reflect my progress on the task.
* As *assigned response agent* I want to *communicate that a task is unclear or that I need assistance with a task* to the *incident response manager*.

#### Acceptance Criteria

Incident Status:
* Incident Status can be changed from *OPEN* to *RESOLVED* by the *incident response manager* if no associated task has a status other than *RESOLVED*
* Incident Status can be changed from *RESOLVED* to *OPEN* by the *incident response manager*

Task Status:
* Task status can be changed from *OPEN* or *REQUIRES_CLARIFICATION* to *IN_PROGRESS* by the assigned user
* Task status can be changed from *IN_PROGRESS* to *RESOLVED* by the assigned user
* Task status can be changed from *OPEN* or *IN_PROGRESS* to *REQUIRES_CLARIFICATION* by the assigned user
* Task status can not be reset to *OPEN* by the assgined user
* An *incident response manager* can set the status of a task to any state

# Design 

## Architecture and Data Model
 
[Class Diagram](./classDiagram.md)

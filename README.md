# Boris Bikes

## in Python


Built using Makers Academy's course.



## User Stories

``` As a person,
So that I can use a bike,
I'd like a docking station to release a bike
```
| Objects | Messages |
| --- | --- |
| Person |  |
| DockingStation | release_bike |

<hr />

``` As a person,
So that I can use a good bike,
I'd like to see if a bike is working
```

| Objects | Messages |
| --- | --- |
| Person |  |
| Bike | is_working? |

<hr />

``` As a member of the public
So I can return biked I've hired
I want to dock my bike at the docking station
``` 

| Objects | Messages |
| --- | --- |
| Person |  |
| DockingStation | dock_bike |

<hr />

```As a member of the public
So I can decide whether to use the docking station
I want to see a bike that has been docked
```

| Objects | Messages |
| --- | --- |
| Person |  |
| DockingStation | list_bikes |

<hr />

``` As a member of the public,
So that I am not confused and charged unnecessarily,
I'd like docking stations not to release bikes when there are none available
```

| Objects | Messages |
| --- | --- |
| Person |  |
| DockingStation | docked_bikes >= 0 |

<hr />

``` As a maintainer of the system,
So that I can control the distribution of bikes,
I'd like docking stations not to accept more dikes than their capacity
```

| Objects | Messages |
| --- | --- |
| Person |  |
| DockingStation | capacity = input OR default |

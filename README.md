# py-stars #

[![GitHub Super-Linter](https://github.com/Leogiciel/py-stars/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

## Description ##

Receives a start array and a target array.
Computes the minimum moves to pass from start state to the target one following the rules given :
- You can change last value
- You can change a value at rank n if the value at rank n+1 is ON, and if all other righter values are OFF

*Example :*

**Input**
````
101010
010101
````

**Output**
````
26
````

## Usage ##

### Calling script ###

A simple script "star_script.py" can be called in a console :
````
C:\Users\Leogiciel\Peacock\py-stars> python star_script.py '11001001000
>> 10000110011'
877
````

### main.py ###

This file can be run. It executes unit tests on given functional requirements.

### star_worker.py ###

This module can be used from any python program. 
It receives the argument as a string, encapsulates args parsing, then raise Exceptions or call the class Chain to compute the result.

## Changelog ##

Exceptions raised on invalid datas received.
Typing hints.

## TODO ##

Add some logs.

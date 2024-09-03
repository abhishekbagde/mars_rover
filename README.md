# Toy Robot Simulator

## What does it do?

The robot can:
- Be placed on a 5x5 table
- Move forward
- Turn left or right
- Tell you where it is

## How to use it

1. Run the script: `python mars_rover.py`
2. Type in commands when it asks you

## Commands you can use

- `PLACE X,Y,F`: Put the robot on the table (X and Y are coordinates, F is the direction it's facing)
- `MOVE`: Move one step forward
- `LEFT` or `RIGHT`: Turn 90 degrees
- `REPORT`: Ask the robot where it is
- `EXIT`: Quit the program (in case your robot needs a nap 😴)

## Example

```
PLACE 0,0,NORTH
MOVE
RIGHT
MOVE
REPORT
```
This will tell you the robot is at 1,1,EAST
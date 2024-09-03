from enum import Enum
from typing import Optional, Tuple

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Robot:
    def __init__(self):
        self.x: Optional[int] = None
        self.y: Optional[int] = None
        self.direction: Optional[Direction] = None

    def place(self, x: int, y: int, direction: Direction) -> None:
        # Place the robot on the table.
        if self._is_valid_position(x, y):
            self.x, self.y, self.direction = x, y, direction

    def move(self) -> None:
        # Move the robot one unit forward in the current direction.
        if not self._is_on_table():
            return

        new_x, new_y = self._get_new_position()
        if self._is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y

    def left(self) -> None:
        # Rotate the robot 90 degrees to the left.
        if self.direction is not None:
            self.direction = Direction((self.direction.value - 1) % 4)

    def right(self) -> None:
        # Rotate the robot 90 degrees to the right.
        if self.direction is not None:
            self.direction = Direction((self.direction.value + 1) % 4)

    def report(self) -> str:
        # Report the current position and direction of the robot.
        return f"{self.x},{self.y},{self.direction.name}" if self._is_on_table() else "Robot is not on the table"

    def _is_on_table(self) -> bool:
        # Check if the robot is on the table.
        return self.x is not None and self.y is not None and self.direction is not None

    def _is_valid_position(self, x: int, y: int) -> bool:
        # Check if the given position is valid on the table.
        return 0 <= x < 5 and 0 <= y < 5

    def _get_new_position(self) -> Tuple[int, int]:
        # Calculate the new position after a move.
        moves = {
            Direction.NORTH: (0, 1),
            Direction.EAST: (1, 0),
            Direction.SOUTH: (0, -1),
            Direction.WEST: (-1, 0)
        }
        dx, dy = moves[self.direction]
        return self.x + dx, self.y + dy

def process_command(robot: Robot, command: str) -> None:
    # Process a single command for the robot.
    parts = command.split()
    if not parts:  # Check if the input is empty
        print("No command entered. Please try again.")
        return

    action = parts[0].upper()

    if action == "PLACE" and len(parts) == 2:
        try:
            x, y, direction = parts[1].split(',')
            robot.place(int(x), int(y), Direction[direction.upper()])
        except (ValueError, IndexError, KeyError):
            print("Invalid PLACE command. Format: PLACE X,Y,F")
    elif action == "MOVE":
        robot.move()
    elif action == "LEFT":
        robot.left()
    elif action == "RIGHT":
        robot.right()
    elif action == "REPORT":
        print(robot.report())
    else:
        print(f"Invalid command: {command}")

def main():
    robot = Robot()
    print("Toy Robot Simulator")
    print("Commands: PLACE X,Y,F | MOVE | LEFT | RIGHT | REPORT | EXIT")
    
    while True:
        try:
            command = input("Enter command: ").strip()
            if command.upper() == "EXIT":
                break
            process_command(robot, command)
        except KeyboardInterrupt:
            print("\nExiting the simulator.")
            break

if __name__ == "__main__":
    main()
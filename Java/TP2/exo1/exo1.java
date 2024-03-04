class Position {
	int x;
	int y;
	Position(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

enum Direction {
	NORTH,
	SOUTH,
	EAST,
	WEST
}

class Rover {
	private Position position;
	private Direction direction;
	Rover (Position position, Direction direction) {
		this.position = position;
		this.direction = direction;
	}

	Rover (Integer x, Integer y, Direction direction) {
		this(new Position(x, y), direction);
	}

	Rover () {
		this(new Position(0, 0), Direction.NORTH);
	}
}

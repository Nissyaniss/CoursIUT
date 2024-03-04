package rover;

public class Rover {
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

	public Position getPosition() {
		return position;
	}

	public void setPosition(Position position) {
		this.position = position;
	}

	public Direction getDirection() {
		return direction;
	}

	public void setDirection(Direction direction) {
		this.direction = direction;
	}

	@Override
	public String toString() {
		return "Rover [position=" + position.toString() + ", direction=" + direction + "]";
	}
	
	public String getLocation() {
		return "at position (x=" + this.position.x() + ",y=" + this.position.y() + ") towards the " + this.direction;
	}
	
	public void turnRight() {
		switch (this.direction) {
			case NORTH:
				this.direction = Direction.EAST;
				break;
			case EAST:
				this.direction = Direction.SOUTH;
				break;
			case SOUTH:
				this.direction = Direction.WEST;
				break;
			case WEST:
				this.direction = Direction.NORTH;
				break;
			default:
				throw new IllegalArgumentException("Unexpected value: " + this.direction);
		}
	}
	
	public void turnLeft() {
		switch (this.direction) {
			case NORTH:
				this.direction = Direction.WEST;
				break;
			case WEST:
				this.direction = Direction.SOUTH;
				break;
			case SOUTH:
				this.direction = Direction.EAST;
				break;
			case EAST:
				this.direction = Direction.NORTH;
				break;
			default:
				throw new IllegalArgumentException("Unexpected value: " + this.direction);
		}
	}
	
	public void move() {
		switch (this.direction) {
		case NORTH:
			this.position.setY(this.position.y() + 1);
			break;
		case WEST:
			this.position.setX(this.position.x() - 1);
			break;
		case SOUTH:
			this.position.setY(this.position.y() - 1);
			break;
		case EAST:
			this.position.setX(this.position.x() + 1);
			break;
		default:
			throw new IllegalArgumentException("Unexpected value: " + this.direction);
		}
	}
	
}
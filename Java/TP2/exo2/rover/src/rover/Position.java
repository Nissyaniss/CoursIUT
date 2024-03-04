package rover;

public class Position {
	private Integer x;
	private Integer y;
	
	public Position(Integer x, Integer y) {
		this.y = y;
		this.x = x;
	}
	
	public int x() {
		return x;
	}
	
	public int y() {
		return y;
	}

	public void setX(Integer x) {
		this.x = x;
	}

	public void setY(Integer y) {
		this.y = y;
	}

	@Override
	public String toString() {
		return "Position [x=" + x + ", y=" + y + "]";
	}
}

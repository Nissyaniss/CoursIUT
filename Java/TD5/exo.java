public interface Bounceable {
	public void bounce();
}

class Ball implements Bounceable {
	private Integer size;
}

class HandBall extends Ball {
	@Override
	public void bounce(){
	}
}

class RugbyBall extends Ball {
	@Override
	public void bounce(){
	}
}

class Tyre implements Bounceable {
	@Override
	public void bounce(){
	}
}

class Pitch {
	private Integer length;
	private Integer width;
}

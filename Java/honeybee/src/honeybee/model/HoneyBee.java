package honeybee.model;

public abstract class HoneyBee {
	protected final String name;

	protected HoneyBee(String name) {
		super();
		this.name = name;
	}

	public String doYourJob() {
		return this.name + " I'm a HoneyBee!";
	}

	public String fly() {
		return "I believe, I can fly.";
	}

	public String getName() {
		return name;
	}
}

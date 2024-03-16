package honeybee.model;

public class Worker extends HoneyBee {
	public Worker(String name) {
		super(name);
	}

	@Override
	public String doYourJob() {
		return super.doYourJob() + "I'm a Worker, I work all day!";
	}
}

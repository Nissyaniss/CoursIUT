package zoo.model.animal;

public class Pig extends Animal{
	public Pig(String name) {
		super(name);
	}
	
	@Override
	public String noise() {
		return "Oink oink!";
	}
}

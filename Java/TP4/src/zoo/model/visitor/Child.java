package zoo.model.visitor;

public abstract class Child extends Visitor{
	protected Integer age; 
	protected Child(Integer age) {
		this.age = age;
	}
	
	@Override
	public String whoAmI() {
		return "I'm a child";
	}
}

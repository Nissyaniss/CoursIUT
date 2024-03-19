package zoo.model.visitor;

public class Teenager extends Child{
	public Teenager(Integer age) {
		super(age);
	}
	
	@Override
	public String whoAmI() {
		return "I'm between 12 and 18 years old : I'm a teenager !";
	}
	
	@Override
	public Integer priceOfTicket() {
		return REGULAR_TICKET/2;
	}
}

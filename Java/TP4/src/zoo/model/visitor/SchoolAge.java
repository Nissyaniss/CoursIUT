package zoo.model.visitor;

public class SchoolAge extends Child {
	public SchoolAge(Integer age) {
		super(age);
	}
	
	@Override
	public String whoAmI() {
		return "I'm between 6 and 12 years old : I'm a school-age child !";
	}
	
	@Override
	public Integer priceOfTicket() {
		return REGULAR_TICKET/3;
	}
}

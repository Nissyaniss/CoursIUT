package zoo.model.visitor;

public class Adult extends Visitor{
	@Override
	public String whoAmI() {
		return "I'm an adult.";
	}
	
	@Override
	public Integer priceOfTicket() {
		return REGULAR_TICKET;
	}
}

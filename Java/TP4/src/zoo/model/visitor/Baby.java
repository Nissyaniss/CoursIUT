package zoo.model.visitor;

import zoo.model.Noisy;

public class Baby extends Child implements Noisy{
	public Baby() {
		super(0);
	}
	
	@Override
	public String whoAmI() {
		return  "I'm under 1 years old : I'm a baby !";
	}
	
	@Override
	public Integer priceOfTicket() {
		return 0;
	}
	
	@Override
	public String noise() {
		return "waaaaaaaaaaa";
	}
}

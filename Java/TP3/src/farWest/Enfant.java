package farWest;

public class Enfant extends PersonnageFarWest {
	private Integer age;
	
	public Enfant(String prenom, Integer age) {
		super(prenom, "");
		this.age = age;
	}
	
	public void faireDesBetises() {
		// TODO
	}
	
	@Override
	public String decrire() {
		return super.decrire() + "J'ai " + age + " ans";
	}
}

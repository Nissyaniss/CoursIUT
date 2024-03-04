package farWest;

public class Heros extends PersonnageFarWest{
	private String profession;
	private Cheval cheval;

	public Heros(String prenom, String nom, String profession, Cheval cheval) {
		super(prenom, nom);
		this.profession = profession;
		this.cheval = cheval;
	}
	
	public void monter(Cheval cheval) {
		//TODO
	}
	
	public void attraper(Cheval cheval) {
		//TODO
	}
	
	@Override
	public String decrire() {
		return super.decrire() + "suis " + this.profession + " et mon cheval " + this.cheval.decrire();
	}
}

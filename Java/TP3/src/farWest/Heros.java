package farWest;

public class Heros extends PersonnageFarWest implements EtreCapableDeTirerAvecUneArmeAFeu{
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
	public void tirerAuPistolet() {
		System.out.println("Je tire plus vite au pistolet : ..Pan..Pan..Pan");
	}
	
	@Override
	public String decrire() {
		return super.decrire() + "Je suis " + this.profession + " et mon cheval " + this.cheval.decrire();
	}
}

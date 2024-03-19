package farWest;

public class Bandit extends PersonnageFarWest implements EtreCapableDeTirerAvecUneArmeAFeu {
	private Integer taille;
	private Boolean estEnPrison;

	public Bandit(String prenom, String nom, Integer taille) {
		super(prenom, nom);
		this.taille = taille;
		this.estEnPrison = false;
	}
	
	public void faireUnBraquage() {
		//TODO
	}
	
	public void mettreEnPrison() {
		this.estEnPrison = true;
	}
	
	public void libererDePrison() {
		this.estEnPrison = false;
	}
	
	@Override
	public void tirerAuPistolet() {
		System.out.println("Je tire au pistolet : .......Pan......Pan......Pan");
		
	}
	
	@Override
	public String decrire() {
		return super.decrire() + "Je mesure " + this.taille + " cm et je suis " + (this.estEnPrison ? "en Prison" : "Libre");
	}
}

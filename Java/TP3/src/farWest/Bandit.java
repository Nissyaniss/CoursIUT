package farWest;

public class Bandit extends PersonnageFarWest {
	private Integer taille;
	private Boolean estEnPrison;

	public Bandit(Integer taille, String prenom, String nom) {
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
	public String decrire() {
		return super.decrire() + "mesure " + this.taille + " cm et je suis " + (this.estEnPrison ? "en Prison" : "Libre");
	}
}

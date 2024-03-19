package farWest;

public abstract class PersonnageFarWest{
	protected final String prenom;
	protected final String nom;

	protected PersonnageFarWest(String prenom, String nom) {
		this.prenom = prenom;
		this.nom = nom;
	}
	
	public String decrire() {
		return this.prenom + " " + this.nom + "! ";
	}
	
	public String prenom() {
		return this.prenom;
	}
	
	public String nom() {
		return this.nom;
	}
}

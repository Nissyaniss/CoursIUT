public class PersonnageFarWest {
	protected final String prenom;
	protected final String nom;

	public PersonnageFarWest(String prenom, String nom) {
		this.prenom = prenom;
		this.nom = nom;
	}

	public void tirerAuPistolet() {
	}
}

public class Bandit extends PersonnageFarWest {
	private Integer taille;
	private Boolean estEnPrison;

	public Bandit(String prenom, String nom, Integer taille) {
		super(prenom, nom);
		this.taille = taille;
		this.estEnPrison = false;
	}

	public void faireUnBraquage() {
	}

	public void mettreEnPrison() {
		this.estEnPrison = true;
	}

	public void libererDePrison() {
		this.estEnPrison = false;
	}
}

public class Cheval {
	private final String nom;
	private final String race;

	public Cheval(String nom, String race) {
		this.nom = nom;
		this.race = race;
	}
}

public class Heros extends PersonnageFarWest {
	private String profession;
	private Cheval cheval;

	public Heros(String prenom, String nom, String profession, Cheval cheval) {
		super(prenom, nom);
		this.profession = profession;
		this.cheval = cheval;
	}

	public void monter(Cheval cheval) {
	}

	public void attraper(Bandit bandit) {
	}
}

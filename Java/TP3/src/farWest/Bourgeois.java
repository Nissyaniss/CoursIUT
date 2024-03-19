package farWest;

public class Bourgeois extends PersonnageFarWest implements EtreCapableDeTirerAvecUneArmeAFeu {
	private String profession;
	
	public Bourgeois(String prenom, String nom, String profession) {
		super(prenom, nom);
		this.profession = profession;
	}
	
	public void faireDesAffaires() {
		//TODO
	}
	
	@Override
	public void tirerAuPistolet() {
		System.out.println("Je tire très mal au pistolet : ............Pan+......");
	}
	
	@Override
	public String decrire() {
		return super.decrire() + "Je suis un " + profession;
	}

}

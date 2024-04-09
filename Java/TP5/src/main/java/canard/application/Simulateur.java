package canard.application;

import canard.model.*;

import java.util.ArrayList;
import java.util.List;

public class Simulateur {
	private static final String LIGNE = "-----------------";

	public static void main(String[] args) {

		List<Canard> canards = mettreDesCanardsDansMonSimulateur();

		faireAfficherEtNager(canards);

	}

	private static List<Canard> mettreDesCanardsDansMonSimulateur() {
		List<Canard> canards = new ArrayList<>();
		canards.add(new Colvert("Piero"));
		canards.add(new Leurre("Danny"));
		canards.add(new Mandarin("Oshidori"));
		canards.add(new CanardEnPlastique("Rubber"));
		return canards;
	}

	private static void faireAfficherEtNager(List<Canard> canards) {
		System.out.println(LIGNE);
		System.out.println("Afficher et Nager");
		System.out.println(LIGNE);

		for (Canard canard : canards) {
			System.out.println(canard.getNom() + " : " + canard.afficher());
			System.out.println(canard.nager());
			System.out.println(canard.effectuerVol());
		}
	}
}

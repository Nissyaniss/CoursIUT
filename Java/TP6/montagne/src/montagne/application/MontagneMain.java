package montagne.application;

import montagne.ihm.Console;
import montagne.metier.ChaineDeMontagne;
import montagne.metier.Sommet;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public class MontagneMain {

	public static void main(String[] args) {
		List<Sommet> sommets = new ArrayList();
		sommets.add(new Sommet("Mont Blanc", 4809, ChaineDeMontagne.MONTBLANC));
		sommets.add(new Sommet("Aiguille des Grands Montets", 3295, ChaineDeMontagne.MONTBLANC));
		sommets.add(new Sommet("La Rhune", 905, ChaineDeMontagne.PYRENEES));
		sommets.add(new Sommet("Pic du Midi", 2877, ChaineDeMontagne.PYRENEES));
		sommets.add(new Sommet("Pic d'Aneto", 3404, ChaineDeMontagne.PYRENEES));
		sommets.add(new Sommet("Pic du Canigou", 2785, ChaineDeMontagne.PYRENEES));
		sommets.add(new Sommet("Puy de Sancy", 1579, ChaineDeMontagne.MASSIF_CENTRAL));
		sommets.add(new Sommet("Puy de Dôme", 1465, ChaineDeMontagne.MASSIF_CENTRAL));
		sommets.add(new Sommet("Le Grand Ballon", 1424, ChaineDeMontagne.VOSGES));
		Console.titre("Mes sommets");
		afficherTousLes(sommets);
		Console.titre("Mes sommets triés par altitude décroissante");
		Collections.sort(sommets);
		afficherTousLes(sommets);
		Console.titre("Mes sommets triés par altitude croissante");
		Collections.sort(sommets, new ComparateurAltitude());
		afficherTousLes(sommets);
		Console.titre("Mes sommets triés par altitude décroissante");
		ComparateurAltitude comparateurAltitude = new ComparateurAltitude();
		Collections.sort(sommets, comparateurAltitude.reversed());
		afficherTousLes(sommets);
		Console.titre("Mes sommets triés par nom (ordre alpha)");
		ComparateurNom comparateurNom = new ComparateurNom();
		Collections.sort(sommets, comparateurNom);
		afficherTousLes(sommets);
		Console.titre("Mes sommets triés par chaine de montagne");
		ComparateurChaineDeMontagne comparateurChaineDeMontagne = new ComparateurChaineDeMontagne();
		Collections.sort(sommets, comparateurChaineDeMontagne);
		afficherTousLes(sommets);
		Console.titre("Mes sommets par chaine et altitude décroissante");
		ComparateurChaineAltitude comparateurChaineAltitude = new ComparateurChaineAltitude();
		Collections.sort(sommets, comparateurChaineAltitude);
		afficherTousLes(sommets);
	}

	private static void afficherTousLes(List<Sommet> sommets) {
		Iterator var2 = sommets.iterator();

		while(var2.hasNext()) {
			Sommet sommet = (Sommet)var2.next();
			Console.message(sommet.description());
		}

	}
}

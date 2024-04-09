package montagne.application;

import java.util.Comparator;
import montagne.metier.Sommet;

class ComparateurChaineAltitude implements Comparator<Sommet> {

    @Override
    public int compare(Sommet sommet1, Sommet sommet2) {
        int resultat = sommet1.chaine().nom().compareTo(sommet2.chaine().nom());
        if (resultat == 0) {
            resultat = sommet2.altitude().compareTo(sommet1.altitude());
        }

        return resultat;
    }
}

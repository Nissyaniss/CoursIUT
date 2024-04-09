
package montagne.application;

import java.util.Comparator;
import montagne.metier.Sommet;

class ComparateurChaineDeMontagne implements Comparator<Sommet> {

    @Override
    public int compare(Sommet sommet1, Sommet sommet2) {
        return sommet1.chaine().nom().compareTo(sommet2.chaine().nom());
    }
}

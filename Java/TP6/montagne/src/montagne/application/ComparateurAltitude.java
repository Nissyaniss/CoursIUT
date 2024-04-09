package montagne.application;

import java.util.Comparator;
import montagne.metier.Sommet;

class ComparateurAltitude implements Comparator<Sommet> {

    @Override
    public int compare(Sommet sommet1, Sommet sommet2) {
        return sommet1.altitude().compareTo(sommet2.altitude());
    }
}

```java
public class MontagneMain {
    public static void main(String[] args) {
        ArrayList<Sommet> sommets = new ArrayList<>();
        sommets.add(new Sommet("Mont Blanc", 4809, ChaineDeMontagne.MONTBLANC));
        sommets.add(new Sommet("AIguille des Grands Montets", 3295, ChaineDeMontagne.MONTBLANC));
        sommets.add(new Sommet("La Rhune", 905, ChaineDeMontagne.PYRENNEE));
        ComparateurAltitude comp1 = new ComparateurAltitude();
        Collections.sort(sommets, comp1);

        Console.titre("Mes Sommets triés par altitude croissante")
        for (Sommet s : sommets) {
            Console.message(s.description());
        }
        ComparateurNom comp2 = new ComparateurNom();
        Collections.sort(sommets, comp2);

        Console.titre("Mes Sommets triés par nom alphabétique")
        for (Sommet s : sommets) {
            Console.message(s.description());
        }
        ComparateurChaineDeMontagne comp3 = new ComparateurDeMontagne();
        Collections.sort(sommets, comp3);

        Console.titre("Mes Sommets triés par chaine de montagne")
        for (Sommet s : sommets) {
            Console.message(s.description());
        }
    }
}

public class Sommet implements Comparable<Sommet> {
    ...
    @Override
    public int compareTo(Sommet o) {
        return -this.altitude().compareTo(o.altitude);
    }
    ...
}

public class ComparateurAltitude implements Comparator<Sommet> {
    @Override
    public int compare(Sommet o1, Sommet o2) {
        return o1.altitude().compareTo(o2.altitude());
    }
}

public class ComparateurNom implements Comparator<Sommet> {
    @Override
    public int compare(Sommet o1, Sommet o2) {
        return o1.nom().compareTo(o2.nom())
    }
}

public class ComparateurChaineDeMontagne implements Comparator<Sommet> {
    @Override
    public int compare(Sommet o1, Sommet o2) {
        return o1.chaine().nom().compareTo(o2.chaine().nom())
    }
}
```


package honeybee.application;

import honeybee.gui.Console;
import honeybee.model.Drone;
import honeybee.model.HoneyBee;
import honeybee.model.Queen;
import honeybee.model.Worker;

public class Sandbox {
	public static void main(String[] args) {
		HoneyBee melli = new Queen("Mellifera");
		HoneyBee may = new Worker("Maya");
		HoneyBee will = new Drone("Willy");
		
		Console.title("Appel à getClass de la classe Object");
		Console.message("Classe de l'objet melli : " + melli.getClass());
		Console.message("Classe de l'objet may: " + may.getClass());
		Console.message("Classe de l'objet will : " + will.getClass());
		
		Console.title("Appel a getName de la classe Class via le mot clé classe");
		Console.message("Classe de d'un objet Class Queen.class : " + (Queen.class).getName());
		Console.message("Classe de d'un objet Class Queen.class : " + (Worker.class).getName());
		Console.message("Classe de d'un objet Class Queen.class : " + (Drone.class).getName());
		
		Console.title("Appel à getName de la classe HoneyBee");
		Console.message("Nom de l'abeille de la classe melli : " + melli.getName());
		Console.message("Nom de l'abeille de la classe may : " + may.getName());
		Console.message("Nom de l'abeille de la classe will : " + will.getName());
		
		Console.title("Operateur instanceof");
		if (melli instanceof HoneyBee)
			Console.message("melli est une instance de HoneyBee");
		if (melli instanceof Queen)
			Console.message("melli est une instance de Queen");
		if (melli instanceof Worker)
			Console.message("melli est une instance de Worker");
		if (melli instanceof Drone)
			Console.message("melli est une instance de Drone");
		
		Queen firstQueen = (Queen) melli;
		//Queen nextQueen = (Worker) melli;
		
	}
}

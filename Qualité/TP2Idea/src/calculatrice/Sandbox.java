package calculatrice;

import calculatrice.model.Calculatrice;
import calculatrice.util.DivisionParZeroException;

public class Sandbox {
	
	public static void main(String[] args) {
		Calculatrice calculatrice = new Calculatrice();
	
		int dividende = 42;
		int diviseur = 2;
		int quotient = 0;

		try {
			quotient = calculatrice.diviser(dividende, diviseur);
			System.out.println("Le résultat de la division de " + dividende + " par " + diviseur + " est : " + quotient);
		} catch (DivisionParZeroException e) {
			System.out.println("La division est par 0 est impossible");
			System.out.println("L'exception capturée est : " + e.getMessage());
		}


		try {
			quotient = calculatrice.diviser(dividende, 0);
		} catch (DivisionParZeroException e) {
			System.out.println("La division est par 0 est impossible");
			System.out.println("L'exception capturée est : " + e.getMessage());
		}

	}
	
	
}

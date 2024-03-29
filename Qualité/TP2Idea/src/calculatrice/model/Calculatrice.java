package calculatrice.model;

import calculatrice.util.DivisionParZeroException;

public class Calculatrice {
	
	public int additionner(int terme1, int terme2) {
		return terme1 + terme2;
	}
	
	public int soustraire(int terme1, int terme2) {
		return terme1 - terme2;
	}
	
	public int multiplier(int terme1, int terme2) {
		return terme1 * terme2;
	}
	
	public int diviser(int dividende, int diviseur) throws DivisionParZeroException {
		if (diviseur == 0 || dividende == 0) {
			throw new DivisionParZeroException("Divison impossible car le diviseur est égal à zéro");
		}

		return dividende / diviseur;
	}


}

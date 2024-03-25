package calculatrice;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class CalculatriceTest {
	private Calculatrice test;
	
	@BeforeEach
	void init() {
		test = new Calculatrice();
	}
	
	@Test
	void doitAdditionnerDeuxEntiers() {
		int terme1 = 5;
		int terme2 = 1;
		
		int resultat = test.additionner(terme1, terme2);
		
		assertEquals(6, resultat);
	}
	
	
	@Test
	void doitSoustraireDeuxEntiers() {
		int terme1 = 5;
		int terme2 = 1;
		
		int resultat = test.soustraire(terme1, terme2);
		
		assertEquals(4, resultat);
	}
	
	@Test
	void doitMultiplierDeuxEntiers() {
		int terme1 = 5;
		int terme2 = 1;
		
		int resultat = test.multiplier(terme1, terme2);
		
		assertEquals(5, resultat);
	}
	
	@Test
	void doitDiviserDeuxEntiers() {
		int dividende = 42;
		int diviseur = 5;
		
		int resultat = test.diviser(dividende, diviseur);
		
		assertEquals(8, resultat);
	}
	
    @Test
    void doitLeverUneArithmeticExceptionSiDiviserParZero() {
        Exception exception = assertThrows(ArithmeticException.class, () ->
            test.diviser(1, 0));
        assertEquals("/ by zero", exception.getMessage());
    }

}

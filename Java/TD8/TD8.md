# Exercice 1

1. Oui. Le programme prend un `int` en paramètre et renvoi `fizz` si celui ci est un multiple de 3, `buzz` si il est divisible par 5 et `fizz buzz` si il est divisible par 15.
2. 
a) 
```java
import truc.unitj5

@Test
public class FizzBuzzTest {
	@Test
	void MultipleTroisTest() {
		Fizzbuzz fizzbuzz = new FizzBuzz();
		int number = 3;

		String result = fizzbuzz.jouer(number);

		assertEquals(result, "fizz");
	}
} 
```

Lignes  couverte
```java
public class FizzBuzz {
	public String jouer(int nombre) {
		if (nombre % 15 == 0) {
		}
		if (nombre % 3 == 0) {
			return "fizz";
		}
	}
}
```

b)
```java
...
void MultipleCinqTest() {
	Fizzbuzz fizzbuzz = new FizzBuzz();
	int number = 5;

	String result = fizzbuzz.jouer(number);

	assertEquals(result, "buzz");
}
...
```

Lignes couverte
```java
public class FizzBuzz {
	public String jouer(int nombre) {
		if (nombre % 15 == 0) {
		}
		if (nombre % 3 == 0) {
		}
		if (nombre % 5 == 0) {
			return "fizz";
		}
	}
}
```

c)
```java
void MultipleQuinzeTest() {
	Fizzbuzz fizzbuzz = new FizzBuzz();
	int number = 15;

	String result = fizzbuzz.jouer(number);

	assertEquals(result, "fizz buzz");
}
```

Lignes couverte :
```java
public class FizzBuzz {
	public String jouer(int nombre) {
		if (nombre % 15 == 0) {
			return "fizz buzz";
		}
	}
}```

d)
```java
void NonMultipleCinqTroisQuinze() {
	Fizzbuzz fizzbuzz = new FizzBuzz();
	int number = 16;

	String result = fizzbuzz.jouer(number);

	assertEquals(result, "16");
}
```

Lignes couverte :
```java
public class FizzBuzz {
	public String jouer(int nombre) {
		if (nombre % 15 == 0) {
		}
		if (nombre % 3 == 0) {
		}
		if (nombre % 5 == 0) {
		}
		return Integer.toString(nombre);
	}
}
```

# Exercice 2

[Exercice](Java/TD8/TD8.mdj)

package TP1;

public class Main {

	public static void main(String[] args) {
		Device babbageMachine = new Device("Babbage Analytical Machine", 1837);
		Device turingMachine = new Device("Turing Engine", 1936);
		System.out.println(babbageMachine.toString());
		System.out.println(turingMachine.toString());

		System.out.println(babbageMachine);
		System.out.println(turingMachine);

		ComputerPioneer adaLovelace = new ComputerPioneer("Ada", "Lovelace", babbageMachine);
		ComputerPioneer alanTuring = new ComputerPioneer("Alan", "Turing", turingMachine);
		System.out.println(adaLovelace);
		System.out.println(alanTuring);
		
		System.out.println("Test case 3 ");
		System.out.println("--------------------");
		System.out.println(adaLovelace.worksOn(babbageMachine));
		System.out.println(adaLovelace.worksOn(turingMachine));
		System.out.println(alanTuring.worksOn(babbageMachine));
		System.out.println(alanTuring.worksOn(turingMachine));
		System.out.println("--------------------");
		
		System.out.println("Test case 4");
		System.out.println("--------------------");
		Device babbage = new Device("Babbage Analytical Machine", 1837);
		Device turing= new Device("Turing Engine", 1936);
		System.out.println(adaLovelace.worksOn(babbage));
		System.out.println(adaLovelace.worksOn(turing));
		System.out.println(alanTuring.worksOn(babbage));
		System.out.println(alanTuring.worksOn(turing));
		System.out.println("--------------------");
	}

}

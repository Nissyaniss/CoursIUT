package honeybee.application;

import java.util.Arrays;
import java.util.List;

import honeybee.gui.Console;
import honeybee.model.Drone;
import honeybee.model.HoneyBee;
import honeybee.model.Queen;
import honeybee.model.Worker;

public class HoneyBeeMain {
	public static void main(String[] args) {
		someHoneyBees();
		arrayOfHoneyBees();
		collectionOfHoneyBees();
	}

	private static void someHoneyBees() {
		Console.title(" Some honeybees ");

		HoneyBee queen = new Queen("Mellifera");
		HoneyBee firstWorker = new Worker("Maya");
		HoneyBee secondWorker = new Worker("Marguerite");
		HoneyBee thirdWorker = new Worker("Propolis");
		HoneyBee firstDrone = new Drone("Willy");
		HoneyBee secondDrone = new Drone("Didier");

		Console.message(queen.doYourJob());
		Console.message(firstWorker.doYourJob());
		Console.message(secondWorker.doYourJob());
		Console.message(thirdWorker.doYourJob());
		Console.message(firstDrone.doYourJob());
		Console.message(secondDrone.doYourJob());

		Console.message(Console.SEPARATOR_LINE);

		Console.message(queen.fly());
		Console.message(firstWorker.fly());
		Console.message(secondWorker.fly());
		Console.message(thirdWorker.fly());
		Console.message(firstDrone.fly());
		Console.message(secondDrone.fly());
	}

	private static void arrayOfHoneyBees() {
		Console.title(" Array of honeybees ");
		HoneyBee[] honeyBees = { new Queen("Mellifera"), new Worker("Maya"), new Worker("Marguerite"),
				new Worker("Propolis"), new Drone("Willy"), new Drone("Didier") };

		for (HoneyBee honeyBee : honeyBees) {
			Console.message(honeyBee.doYourJob());
		}

		Console.message(Console.SEPARATOR_LINE);

		for (HoneyBee honeyBee : honeyBees) {
			Console.message(honeyBee.fly());
		}
	}

	private static void collectionOfHoneyBees() {
		Integer queenNbr = 0;
		Integer workerNbr = 0;
		Integer droneNbr = 0;
		
		Console.title(" Collection of honeybees ");
		HoneyBee[] honeyBeesArray = { new Queen("Mellifera"), new Worker("Maya"), new Worker("Marguerite"),
				new Worker("Propolis"), new Drone("Willy"), new Drone("Didier") };
		List<HoneyBee> honeyBees = Arrays.asList(honeyBeesArray);

		for (HoneyBee honeyBee : honeyBees) {
			Console.message(honeyBee.doYourJob());
			Console.message(honeyBee.fly());
			Console.message(Console.SEPARATOR_LINE);
		}
		
		Console.message(Console.SEPARATOR_LINE);
		Console.message("My collection has " + honeyBees.size() + " honeyBees");
		Console.message(Console.SEPARATOR_LINE);
		for (HoneyBee honeyBee : honeyBees) {
			if (honeyBee instanceof Queen) {
				queenNbr++;
			}
			else if (honeyBee instanceof Worker) {
				workerNbr++;
			}
			else if (honeyBee instanceof Drone) {
				droneNbr++;
			}
		}
		Console.message("-> " + queenNbr + " queen(s)");
		Console.message("-> " + workerNbr + " worker(s)");
		Console.message("-> " + droneNbr + " drone(s)");
	}
}

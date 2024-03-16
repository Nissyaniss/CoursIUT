package honeybee.gui;

public class Console {
	public static final String SEPARATOR_LINE = "--------------------------------------------";

	public static void message(String text) {
		System.out.println(text);

	}

	public static void title(String string) {
		message(SEPARATOR_LINE);
		message(string);
		message(SEPARATOR_LINE);
	}

}

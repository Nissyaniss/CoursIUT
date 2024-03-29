package calculatrice.util;

@SuppressWarnings("serial")
public class DivisionParZeroException extends Exception{
	public DivisionParZeroException(String message) {
		super(message);
	}
}

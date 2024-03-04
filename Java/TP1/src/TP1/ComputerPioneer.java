package TP1;

public class ComputerPioneer {
	private String firstName;
	private String lastName;
	private Device device;
	
	public ComputerPioneer(String firstName, String lastName, Device device) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.device = device;
	}
	
	@Override
	public String toString() {
		return this.device + ". " + this.firstName + " " + this.lastName + " is a pioneer in Computer Science";
	}
	
	public Boolean worksOn(Device device) {
		if (this.device.equals(device)) {
			return true;
		}
		else {
			return false;
		}
	}
}

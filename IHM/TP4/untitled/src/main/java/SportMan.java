import java.util.Objects;

public class SportMan {
    private final String firstName;
    private final String lastName;
    private final Sport sport;
    public SportMan(String firstName, String lastName, Sport sport) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.sport = sport;
    }
    public String whoAmI() {
        return this.firstName + " " + this.lastName + " - " + this.sport;
    }
    public String getFirstName() {
        return firstName;
    }
    public String getLastName() {
        return lastName;
    }
    public Sport getSport() {
        return sport;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        SportMan sportMan = (SportMan) o;
        return Objects.equals(firstName, sportMan.firstName) && Objects.equals(lastName, sportMan.lastName) && sport == sportMan.sport;
    }

    @Override
    public int hashCode() {
        return Objects.hash(firstName, lastName, sport);
    }
}
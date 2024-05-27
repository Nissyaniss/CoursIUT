
import java.util.Objects;

// inspired by
// https://github.com/assertj/assertj-core/blob/517c9c6fca738cb4d088f125ae5186a3a1e4efac/src/test/java/org/assertj/core/data/TolkienCharacter.java

public class TolkienCharacter {

    public final String name;
    public final Integer age;
    public final Race race;

    public TolkienCharacter(String name, Integer age, Race race) {

        this.name = name;
        this.age = age;
        this.race = race;
    }

    public String getName() {

        return name;
    }

    public Integer getAge() {

        return age;
    }

    public Race getRace() {

        return race;
    }

    @Override
    public String toString() {
        return String.format("TolkienCharacter [name=%s, age=%s, race=%s]", name, age, race);
    }

    @Override
    public int hashCode() {
        return Objects.hash(age, name, race);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        TolkienCharacter other = (TolkienCharacter) obj;
        return Objects.equals(age, other.age) && Objects.equals(name, other.name) && race == other.race;
    }

}
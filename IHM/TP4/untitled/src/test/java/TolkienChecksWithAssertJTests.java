import static org.assertj.core.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class TolkienChecksWithAssertJTests {

    protected static final TolkienCharacter frodo = new TolkienCharacter("Frodo", 33, Race.HOBBIT);
    protected static final TolkienCharacter sam = new TolkienCharacter("Sam", 38, Race.HOBBIT);
    protected static final TolkienCharacter merry = new TolkienCharacter("Merry", 36, Race.HOBBIT);
    protected static final TolkienCharacter pippin = new TolkienCharacter("Pippin", 28, Race.HOBBIT);
    protected static final TolkienCharacter gandalf = new TolkienCharacter("Gandalf", 2020, Race.MAIA);
    protected static final TolkienCharacter gimli = new TolkienCharacter("Gimli", 139, Race.DWARF);
    protected static final TolkienCharacter legolas = new TolkienCharacter("Legolas", 1000, Race.ELF);
    protected static final TolkienCharacter aragorn = new TolkienCharacter("Aragorn", 87, Race.MAN);
    protected static final TolkienCharacter boromir = new TolkienCharacter("Boromir", 87, Race.MAN);
    protected static final TolkienCharacter sauron = new TolkienCharacter("Sauron", 50000, Race.MAIA);
    protected static final TolkienCharacter galadriel = new TolkienCharacter("Legolas", 3000, Race.ELF);
    protected static final TolkienCharacter elrond = new TolkienCharacter("Legolas", 3000, Race.ELF);
    protected static final List<TolkienCharacter> fellowshipOfTheRing = new ArrayList<TolkienCharacter>();

    @BeforeAll
    static void createFellowshipOfTheRing() {
        fellowshipOfTheRing.add(frodo);
        fellowshipOfTheRing.add(sam);
        fellowshipOfTheRing.add(merry);
        fellowshipOfTheRing.add(pippin);
        fellowshipOfTheRing.add(gandalf);
        fellowshipOfTheRing.add(legolas);
        fellowshipOfTheRing.add(gimli);
        fellowshipOfTheRing.add(aragorn);
        fellowshipOfTheRing.add(boromir);
    }

    @Test
    void tolkienCharacterShouldHaveProperties() {
        // ensure that TolkienCharacter has the bean property "name"
        // ensure that TolkienCharacter has the bean property "age" with is greater than 0
        assertThat(fellowshipOfTheRing).extracting("name").isNotNull();
        assertThat(fellowshipOfTheRing).extracting("age", Integer.class).allMatch(x -> x > 0);
    }

    @Test
    void validateTolkienCharacterInstanciation() {
        // age is 33
        // name is "Frodo"
        // name is not "Frodon"
        assertThat(frodo).extracting("age").isEqualTo(33);
        assertThat(frodo).extracting("name").isEqualTo("Frodo");
        assertThat(frodo).extracting("name").isNotEqualTo("Frodon");
    }

    @Test
    void ensureThatFellowshipOfTheRingAreNotOrcs() {
        // ensure that no fellowshipOfTheRings is a orc
        assertThat(fellowshipOfTheRing).extracting("race").isNotEqualTo("Orc");
    }

    @Test
    void ensureFellowshipOfTheRingInstanciation() {
        // fellowshipOfTheRing has a size of 9
        // frodo and sam are in the fellowshipOfTheRing
        // sauron is not in the fellowshipOfTheRing
        // aragorn, frodo, legolas, boromir are the only characters with o in their name
        assertThat(fellowshipOfTheRing).hasSize(9);
        assertThat(fellowshipOfTheRing).contains(frodo, sam);
        assertThat(fellowshipOfTheRing).doesNotContain(sauron);
        assertThat(fellowshipOfTheRing).filteredOn(x -> x.getName().contains("o")).containsExactlyInAnyOrder(aragorn, frodo, legolas, boromir);
    }

    @Test
    void listOfHobbitsInFellowshipOfTheRing() {
        // sam, frodo, pippin, merry are the hobbits of fellowshipOfTheRing
        assertThat(fellowshipOfTheRing).filteredOn(x -> x.getRace().equals(Race.HOBBIT)).containsExactlyInAnyOrder(frodo, sam, pippin, merry);
    }

}
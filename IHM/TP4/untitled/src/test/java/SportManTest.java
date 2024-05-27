import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;


class SportManTest {

    static final SportMan TEDDY_RINNER = new SportMan("Teddy", "Rinner", Sport.Judo);
    static final SportMan MELVYN_RICHARDSON = new SportMan("Melvyn", "Richardson", Sport.Handball);
    static final SportMan JACKSON_RICHARDSON = new SportMan("Jackson", "Richardson", Sport.Handball);
    static final SportMan THIERRY_REY = new SportMan("Thierry", "Rey", Sport.Judo);
    static final SportMan TITI_OMEYER= new SportMan("Thierry", "Omeyer", Sport.Handball);
    static final SportMan DAVID_DOUILLET = new SportMan("David", "Douillet", Sport.Judo);
    static List<SportMan> sportMen;

    // why static ? see https://junit.org/junit5/docs/current/user-guide/#writing-tests-annotations
    // with @BeforeAll : Such methods are inherited (unless they are hidden or overridden) and must be static
    // => SportMan objects & sportMen must also be static to be used in this method ;-)
    @BeforeAll
    static void listOfSportMen(){
        sportMen = new ArrayList<>();
        sportMen.add(DAVID_DOUILLET);
        sportMen.add(TITI_OMEYER);
        sportMen.add(THIERRY_REY);
        sportMen.add(JACKSON_RICHARDSON);
        sportMen.add(MELVYN_RICHARDSON);
        sportMen.add(TEDDY_RINNER);
    }


    @Test
    void whoAmI_with_an_hanball_player()
    {
        SportMan ludo = new SportMan("Ludovic","Fabregas",Sport.Handball);
        String who = ludo.whoAmI();

        assertThat(who).isEqualTo("Ludovic Fabregas - Handball");

        assertThat(ludo).extracting("firstName","lastName")
                .contains("Ludovic","Fabregas");

        assertThat(ludo.getSport())
                .isEqualTo(Sport.Handball);
    }

    @Test
    void test_on_list_of_sportMen()
    {
        assertThat(sportMen).extracting("firstName")
                .containsExactly("David", "Thierry", "Thierry", "Jackson", "Melvyn", "Teddy")
                .contains("David", "Thierry", "Jackson", "Melvyn", "Teddy")
                .doesNotContain("Ludovic");


        assertThat(sportMen)
                .filteredOn (sportman -> sportman.getSport().equals(Sport.Judo))
                .contains(DAVID_DOUILLET,TEDDY_RINNER,THIERRY_REY);

        assertThat(sportMen)
                .filteredOn ("lastName","Richardson")
                .contains(MELVYN_RICHARDSON,JACKSON_RICHARDSON);

        assertThat(sportMen)
                .filteredOn (sportman -> sportman.getLastName().equals("Richardson"))
                .contains(MELVYN_RICHARDSON,JACKSON_RICHARDSON);

    }

}
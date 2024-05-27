import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.assertj.core.api.Assertions.*;

public class HelloAssertJ {
    @Test
    void test_hello_with_assertEquals_Junit5() {
        String hello = "hello AssertJ !";
        assertEquals("hello AssertJ !", hello);
    }

    @Test
    void test_hello_with_assertThat_AssertJ() {
        String hello = "hello AssertJ !";
        assertThat(hello).isEqualTo("hello AssertJ !");
    }

    @Test
    void test_List_String() {
        List<String> list = Arrays.asList("1", "2", "3");
        assertThat(list).contains("1");
        assertThat(list).doesNotContain("5");
        assertThat(list).isNotEmpty();
        assertThat(list).startsWith("1");
        assertThat(list).containsSequence("2", "3");
        assertThat(list).doesNotContainSequence("3", "2");
        assertThat(list).containsExactly("1", "2", "3");
    }

    @Test
    void test_List_String_best_practice()
    {
        List<String> list = Arrays.asList("1", "2", "3");
        assertThat(list).contains("1")
                .doesNotContain("5")
                .isNotEmpty()
                .startsWith("1")
                .containsSequence("2", "3")
                .doesNotContainSequence("3", "2")
                .containsExactly("1", "2", "3");
    }

    @Test
    void test_List_Character()
    {
        Character someCharacter = 'i';
        assertThat(someCharacter)
                .isNotEqualTo('a')
                .inUnicode()
                .isGreaterThanOrEqualTo('b')
                .isLowerCase();
    }
}

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AssertJTest {
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
    }
}

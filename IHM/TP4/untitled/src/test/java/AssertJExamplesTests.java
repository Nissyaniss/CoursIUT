import static org.junit.jupiter.api.Assertions.fail;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.*;

public class AssertJExamplesTests {


    // tests for the list
    @DisplayName("Tests for the List")
    @Nested
    class ListTests {

        private List<Integer> list;

        @BeforeEach
        public void setup() {
            list = Arrays.asList(5, 2, 4);
        }

        @Test
        @DisplayName("List should have an intial size of 3")
        void ensureInitialSize() {
            assertThat(list).size().isEqualTo(3);
        }

        @Test
        @DisplayName("Check content of the array")
        void containsNumbersInAnyOrder() {
            assertThat(list).containsExactly(5, 2, 4);
        }   private Integer[] ints;


        @Test
        void everyItemGreaterThan1() {
            assertThat(list).allMatch(x -> x > 1);
        }
    }

    @DisplayName("Tests for the array")
    @Nested
    class ArrayTests {
        private Integer[] ints;

        @BeforeEach
        public void setup() {
            ints = new Integer[] { 7, 5, 12, 16 };

        }

        @Test
        void arrayHasSizeOf4() {
            assertThat(ints).hasSize(4);
        }

        @Test
        void arrayContainsNumbersInGivenOrder() {
            assertThat(ints).containsSequence(7, 5, 12, 16);
        }
    }

    @DisplayName("Tests for the Task")
    @Nested
    class TaskTests {

        // class to be tested
        public class Task {

            private final long id;
            private String summary;
            private String description;
            private int year;

            public Task(long id, String summary, String description) {
                this.id = id;
                this.summary = summary;
                this.description = description;
            }

            // getters/setters
        }

        // tests for the Task
        @Test
        void objectHasSummaryProperty() {
            Task task = new Task(1, "Learn Hamcrest", "Important");
            assertThat(task).hasFieldOrProperty("summary");
        }

        @Test
        void objectHasCorrectSummaryValue() {
            Task task = new Task(1, "Learn Hamcrest", "Important");
            assertThat(task).hasFieldOrPropertyWithValue("summary", "Learn Hamcrest");
        }

        @Test
        void objectHasSameProperties() {
            Task todo1 = new Task(1, "Learn Hamcrest", "Important");
            Task todo2 = new Task(1, "Learn Hamcrest", "Important");

        }
    }

    @DisplayName("Tests for String")
    @Nested
    class StringTests {
        // tests for string
        @Test
        void ensureThatAnEmptryStringIsEmpty() {
            String input = "";
            assertThat(input).isEmpty();
        }

        @Test
        void ensureThatAStringIsEitherNullOrEmpty() {
            String input = "";
            assertThat(input).isNullOrEmpty();
        }
    }
}
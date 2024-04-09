module org.example.td1 {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.td1 to javafx.fxml;
    exports org.example.td1;
}
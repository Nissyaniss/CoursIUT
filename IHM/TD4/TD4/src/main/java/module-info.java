module org.example.td4 {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;
    requires java.sql;


    opens org.example.td4 to javafx.fxml;
    exports org.example.td4;
}
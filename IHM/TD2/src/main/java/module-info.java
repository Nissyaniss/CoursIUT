module org.example.td2 {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.td2 to javafx.fxml;
    exports org.example.td2;
}
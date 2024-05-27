module org.example.tp2 {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.tp2 to javafx.fxml;
    exports org.example.tp2;
}
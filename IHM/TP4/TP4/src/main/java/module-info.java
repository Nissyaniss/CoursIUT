module org.example.tp4 {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.tp4 to javafx.fxml;
    exports org.example.tp4;

    opens org.example.tp4.controleur to javafx.fxml;
    exports org.example.tp4.controleur;
}
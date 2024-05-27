module org.example.tp2 {
    requires javafx.controls;
    requires javafx.fxml;


    opens unilim.info.ihm.tp2.exo2 to javafx.fxml;
    exports unilim.info.ihm.tp2.exo2;
}
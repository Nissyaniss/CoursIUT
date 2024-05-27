package org.example.tp4.controleur;


import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class LoginFormController {

    private final String COMPTA = "Comptabilité";
    private final String PAYE = "Paye";
    private final String GESTION = "Gestion de projet";

    @FXML
    private Button idBtnValider;

    @FXML
    private ComboBox<String> idCb;

    @FXML
    private Label idLibBas;

    @FXML
    private PasswordField idPwd;

    @FXML
    private TextField idUser;

    @FXML
    public void initialize() {
        this.idLibBas.setText("");
        this.idCb.getItems().addAll(COMPTA, PAYE, GESTION);
        this.idCb.setValue(COMPTA);
    }

    @FXML
    void validerSaisies(ActionEvent event) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        if (this.idUser.getText().isEmpty()) {
            alert.setTitle("Erreur");
            alert.setHeaderText(null);
            alert.setContentText("La saisie d'un utilisateur est obligatoire");
            alert.showAndWait();
            return;
        } else if (this.idPwd.getText().isEmpty()) {
            alert.setTitle("Erreur");
            alert.setHeaderText(null);
            alert.setContentText("La saisie d'un mot de passe est obligatoire");
            alert.showAndWait();
            return;
        }

        LocalDateTime dateTime = LocalDateTime.now();
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter hourFormatter = DateTimeFormatter.ofPattern("HH:mm:ss");
        this.idLibBas.setText("Login de <" + this.idUser.getText() + "> pour application <" + this.idCb.getValue() + "> le " + dateTime.format(dateTimeFormatter) + " à " + dateTime.format(hourFormatter));
    }
}

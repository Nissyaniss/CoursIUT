package r202_tp1.tp1bis.exo2;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class FormInscriptionFX extends Application {

    @Override
    public void start(Stage stage) {
        VBox root = new VBox();
        Insets topMargin = new Insets(15,0,0,0);
        Insets topLeftMargin = new Insets(15,0,0,15);
        Insets topRightMafin = new Insets(15,15,0,0);

        Label lblNewsletter = new Label("Souscrivez à notre newsletter !");
        lblNewsletter.setUnderline(true);
        lblNewsletter.setAlignment(Pos.CENTER);
        lblNewsletter.setMaxWidth(Double.MAX_VALUE);

        Label lblWelcome = new Label("Bienvenue à notre newsletter, inscrivez-vous pour avoir des nouvelles.");
        VBox.setMargin(lblWelcome, topMargin);
        lblWelcome.setAlignment(Pos.CENTER);
        lblWelcome.setMaxWidth(Double.MAX_VALUE);

        Label lblGender = new Label("Civilité");
        VBox.setMargin(lblGender, topLeftMargin);

        ComboBox<String> cbxGender = new ComboBox<>();
        cbxGender.getItems().addAll("M.", "Mme.", "Mlle");
        cbxGender.setValue("M.");
        VBox.setMargin(cbxGender, topLeftMargin);

        GridPane gridForm = new GridPane();
        VBox.setMargin(gridForm, topLeftMargin);

        Label lblLastName = new Label("Nom");
        gridForm.add(lblLastName, 0,0);

        TextField txfLastName = new TextField();
        GridPane.setMargin(txfLastName, topRightMafin);
        gridForm.add(txfLastName, 0,1);

        Label lblFirstName = new Label("Prénom");
        gridForm.add(lblFirstName, 1,0);

        TextField txfFirstName = new TextField();
        GridPane.setMargin(txfFirstName, topMargin);
        gridForm.add(txfFirstName, 1,1);

        Label lblEmail = new Label("Adresse email");
        GridPane.setMargin(lblEmail, topMargin);
        gridForm.add(lblEmail, 0,2);

        TextField txfEmail = new TextField();
        GridPane.setMargin(txfEmail, topRightMafin);
        gridForm.add(txfEmail, 0,3);

        Label lblEmailConf = new Label("Confirmez votre email");
        GridPane.setMargin(lblEmailConf, topMargin);
        gridForm.add(lblEmailConf, 1,2);

        TextField txfConfEmail = new TextField();
        GridPane.setMargin(txfConfEmail, topMargin);
        gridForm.add(txfConfEmail, 1,3);

        HBox hboxBtnSubscribe = new HBox();

        Button btnSubscribe = new Button("Souscrire");
        hboxBtnSubscribe.setAlignment(Pos.CENTER);
        hboxBtnSubscribe.setMaxWidth(Double.MAX_VALUE);
        hboxBtnSubscribe.getChildren().add(btnSubscribe);

        root.getChildren().addAll(lblNewsletter, lblWelcome, lblGender, cbxGender, gridForm, hboxBtnSubscribe);

        Scene scene = new Scene(root, 600, 450);
        stage.setScene(scene);
        stage.setTitle("Application Newletter");
        stage.show();

    }

    public static void main(String[] args) {
        launch(args);
    }
}
package org.example.td1;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

import java.text.SimpleDateFormat;
import java.util.Date;

public class LoginAppFX extends Application {
    private Label title;

    private Label errorMessage;

    private Label usernameLabel;
    private TextField username;

    private Label passwordLabel;
    private PasswordField password;

    private Label appLabel;
    private ComboBox<String> app;

    private Button validate;
    private Label footer;

    public static void main(String[] args) {
        LoginAppFX.launch();
    }

    @Override
    public void start(Stage stage) {
        this.title = new Label("Veuillez saisir vos informations de login");
        this.title.setUnderline(true);
        this.title.setAlignment(Pos.CENTER);
        this.title.setMaxWidth(Double.MAX_VALUE);

        this.errorMessage = new Label("");
        this.errorMessage.setMinWidth(250.0);
        this.errorMessage.setPrefSize(250, 250);
        this.errorMessage.setTextFill(Color.color(0.5, 0, 0));
        this.errorMessage.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.usernameLabel = new Label("Utilisateur:");
        this.username = new TextField();

        this.passwordLabel = new Label("Mot de passe:");
        this.password = new PasswordField();

        this.appLabel = new Label("Application");
        this.app = new ComboBox<>();

        String[] apps = {"Comptabilité", "Paye", "Gestion"};
        this.app.getItems().addAll(apps);
        this.app.setValue(apps[0]);

        this.validate = new Button("Valider");
        this.validate.setPadding(new Insets(40, 20, 40, 20));
        this.validate.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                if (password.getText().equals("") && username.getText().equals("")){
                    errorMessage.setText("La saisie d'un mot de passe et d'un username est obligatoire");
                    footer.setText("Aucun login saisi");
                } else if (password.getText().equals("")) {
                    errorMessage.setText("La saisie d'un mot de passe est obligatoire");
                    footer.setText("Aucun login saisi");
                } else if (username.getText().equals("")) {
                    errorMessage.setText("La saisie d'un username est obligatoire");
                    footer.setText("Aucun login saisi");
                } else {
                    Date dateDuJour = new Date();
                    SimpleDateFormat simpleDateFormat = new SimpleDateFormat("dd/MM/yyyy' à 'HH:mm:ss");

                    errorMessage.setText("");
                    footer.setText("login de " + username.getText() + " pour application " + app.getValue() + " le " + simpleDateFormat.format(dateDuJour));
                }

            }
        });


        this.footer = new Label("");
        this.footer.setAlignment(Pos.CENTER);
        this.footer.setMaxWidth(Double.MAX_VALUE);

        // -----------------------------------------------------

        BorderPane root = new BorderPane();

        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Application login");
        stage.setScene(scene);

        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setMaxSize(Double.MAX_VALUE, Double.MAX_VALUE);
        grid.setHgap(10);
        grid.setVgap(5);

        grid.add(this.usernameLabel, 0, 0);
        grid.add(this.username, 1, 0);
        grid.add(this.passwordLabel, 0, 1);
        grid.add(this.password, 1, 1);
        grid.add(this.appLabel, 0, 2);
        grid.add(this.app, 1, 2);
        root.setTop(this.title);
        root.setLeft(this.errorMessage);
        BorderPane.setAlignment(this.errorMessage, Pos.CENTER);
        BorderPane.setMargin(this.errorMessage, new Insets(15, 15, 15, 15));
        root.setCenter(grid);
        root.setRight(this.validate);
        BorderPane.setAlignment(this.validate, Pos.CENTER);
        BorderPane.setMargin(this.validate, new Insets(15, 15, 15, 15));
        root.setBottom(this.footer);

        stage.show();
    }
}
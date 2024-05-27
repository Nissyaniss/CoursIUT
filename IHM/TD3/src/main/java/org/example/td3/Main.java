package org.example.td3;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Orientation;
import javafx.geometry.Pos;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Text;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.net.MalformedURLException;
import java.util.Optional;

public class Main extends Application implements EventHandler<MouseEvent> {

    private Label lblTitre;
    private Label lblNom;
    private Label lblPrenom;
    private Label lblEmail;
    private Label lblPhoto;
    private Label lblPath;
    private Button btnCreer;
    private Button btnPhoto;
    private TextField tfdSaisieNom;
    private TextField tfdSaisiePrenom;
    private TextField tfdSaisieEmail;
    private Stage stage;
    private Text txtCivilite;
    private Text txtEmail;
    private File photo;
    private ImageView imageView;
    private Group zoneDessin;

    public GridPane creerFormulaire() {
        GridPane form = new GridPane();
        form.setAlignment(Pos.CENTER);

        form.add(lblNom, 0,0);
        form.add(tfdSaisieNom, 1, 0);
        form.add(lblPrenom, 0,1);
        form.add(tfdSaisiePrenom, 1, 1);
        form.add(lblEmail, 0,2);
        form.add(tfdSaisieEmail, 1, 2);
        form.add(lblPhoto, 0,3);
        form.add(lblPath, 1, 3);

        return form;
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        this.stage = stage;
        this.lblTitre = new Label("Saisir ma carte de visite");
        this.lblNom = new Label("Nom :");
        this.lblPrenom = new Label("Prenom :");
        this.lblEmail = new Label("Email :");
        this.lblPhoto = new Label("Photo :");
        this.lblPath = new Label("...");

        this.tfdSaisieNom = new TextField();
        this.tfdSaisieEmail = new TextField();
        this.tfdSaisiePrenom = new TextField();

        this.btnCreer = new Button("Creer carte");
        this.btnPhoto = new Button("Photo");

        this.btnCreer.setOnMouseClicked(this);
        this.btnPhoto.setOnMouseClicked(this);

        this.zoneDessin = dessiner();
        VBox.setMargin(zoneDessin, new Insets(5,0,0,0));

        GridPane form = creerFormulaire();
        form.setVgap(5);
        form.setHgap(5);

        FlowPane containeurButtons = new FlowPane(Orientation.HORIZONTAL);
        containeurButtons.setAlignment(Pos.CENTER);
        containeurButtons.setHgap(5);

        containeurButtons.getChildren().addAll(btnCreer, btnPhoto);

        VBox root = new VBox();

        root.getChildren().addAll(lblTitre, form, containeurButtons, zoneDessin);
        root.setAlignment(Pos.CENTER);
        VBox.setMargin(form, new Insets(5,0,5,0));

        Scene scene = new Scene(root, 600,400);

        primaryStage.setScene(scene);
        primaryStage.setTitle("Application carte de visite en Javafx");
        primaryStage.setResizable(false);
        primaryStage.show();
    }

    private Group dessiner() {
        Group dessin = new Group();

        Rectangle rect = new Rectangle(0,0,600,200);
        rect.setFill(Color.PINK);
        this.imageView = new ImageView();

        this.txtCivilite = new Text("Mr/Mrs");
        this.txtCivilite.setX(5);
        this.txtCivilite.setY(20);

        this.txtEmail = new Text("Email : xxxx");
        this.txtEmail.setX(5);
        this.txtEmail.setY(195);

        this.photo = new File("/home/nissya/Cours/Pastedimage20240405183036.png");
        try {
            Image img = new Image(this.photo.toURI().toURL().toString(), 160,160, true, false);
            this.imageView.setImage(img);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }

        dessin.getChildren().addAll(rect, txtCivilite, txtEmail, imageView);
        dessin.setVisible(false);

        return dessin;
    }

    public static void main(String[] args) {
        Application.launch(args);
    }

    @Override
    public void handle(MouseEvent event) {
        Button btn = (Button) event.getSource();

        if (btn == btnCreer) {
            if (tfdSaisiePrenom.getText().isEmpty() || tfdSaisieNom.getText().isEmpty() || tfdSaisieEmail.getText().isEmpty() || this.photo == null) {
                Alert dialog = new Alert(Alert.AlertType.ERROR);
                dialog.setTitle("Erreur de saisie");
                dialog.setHeaderText(null);
                dialog.setContentText("Votre saisie est vide, voulez-vous :");

                ButtonType btnType1 = new ButtonType("Quitter");
                ButtonType btnType2 = new ButtonType("Charger un exemple par défault");
                ButtonType btnType3 = new ButtonType("Revenir a la saisie");

                dialog.getButtonTypes().setAll(btnType1, btnType2, btnType3);
                Optional<ButtonType> choix = dialog.showAndWait();
                if (choix.get() == btnType1) {
                    Platform.exit();
                } else if (choix.get() == btnType2) {
                    tfdSaisieNom.setText("NomDefault");
                    tfdSaisiePrenom.setText("PrenomDefault");
                    tfdSaisieEmail.setText("example@test.com");
                }
            }

            zoneDessin.setVisible(true);
        } else if (btn == btnPhoto) {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Choisisser votre photo");
            FileChooser.ExtensionFilter extensionFilter = new FileChooser.ExtensionFilter("Images files", "*.jpg", "*.png", "*.jpg");

            fileChooser.getExtensionFilters().add(extensionFilter);

            photo = fileChooser.showOpenDialog(this.stage);
            if (photo != null) {
                lblPath.setText(photo.getAbsolutePath());
                try {
                    Image img = new Image(this.photo.toURI().toURL().toString(), 160,160, true, false);
                    this.imageView.setImage(img);
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

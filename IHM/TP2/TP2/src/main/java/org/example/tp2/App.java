package org.example.tp2;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.stage.Stage;

import java.io.IOException;

public class App extends Application implements EventHandler<MouseEvent> {

    private final TextField txfName = new TextField();
    private final TextField txfType = new TextField();
    private final TextField txfPrice = new TextField();
    private final TextField txfQuantity = new TextField();
    private Label lblImagePath;

    private final Label lblNameError = new Label("Veuillez saisir le nom.");
    private final Label lblTypeError = new Label("Veuillez saisir le type.");
    private final Label lblPriceError = new Label("Veuillez saisir le prix.");
    private final Label lblQuantityError = new Label("Veuillez saisir la quantité.");
    private final Label lblImageError  = new Label("Veuillez mettre une image.");

    @Override
    public void start(Stage stage) throws IOException {
        HBox root = new HBox();

        Label lblFormTitle = new Label("Sauvegarde de condiments");
        lblFormTitle.setMaxWidth(Double.MAX_VALUE);
        lblFormTitle.setAlignment(Pos.CENTER);

        Label lblName = new Label("Nom*:");
        lblNameError.setTextFill(Color.RED);
        lblNameError.setVisible(false);

        Label lblType = new Label("Type*:");
        lblTypeError.setTextFill(Color.RED);
        lblTypeError.setVisible(false);

        Label lblPrice = new Label("Prix*:");
        lblPriceError.setTextFill(Color.RED);
        lblPriceError.setVisible(false);

        Label lblQuantity = new Label("Quantité*:");
        lblQuantityError.setTextFill(Color.RED);
        lblQuantityError.setVisible(false);

        Label lblImage = new Label("Image*:");
        lblImagePath = new Label("...");

        ChoixPhotoController choixPhotoController = new ChoixPhotoController(lblImagePath, stage);

        Button btnPhoto = new Button("Photo");
        btnPhoto.setMaxWidth(Double.MAX_VALUE);

        Button btnSave = new Button("Sauvegarder");
        btnSave.setMaxWidth(Double.MAX_VALUE);
        btnSave.setOnMouseClicked(this);

        VBox form = new VBox();
        HBox.setMargin(form, new Insets(10, 0, 15, 15));
        HBox.setHgrow(form, Priority.SOMETIMES);

        form.getChildren().addAll(
                lblFormTitle,
                lblName,
                txfName,
                lblNameError,
                lblType,
                txfType,
                lblTypeError,
                lblPrice,
                txfPrice,
                lblPriceError,
                lblQuantity,
                txfQuantity,
                lblQuantityError,
                lblImage,
                lblImagePath,
                lblImageError,
                btnPhoto,
                btnSave
        );

        VBox list = new VBox();

        Label lblCondimentTitle = new Label("Liste des condiments");
        lblCondimentTitle.setMaxWidth(Double.MAX_VALUE);
        lblCondimentTitle.setAlignment(Pos.CENTER);

        list.getChildren().addAll(lblCondimentTitle);
        HBox.setHgrow(list, Priority.SOMETIMES);

        root.getChildren().addAll(form, list);

        Scene scene = new Scene(root, 700, 500);
        stage.setScene(scene);
        stage.setTitle("Outils d'achats de condiments");
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

    @Override
    public void handle(MouseEvent event) {
        this.lblNameError.setVisible(txfName.getText().isEmpty());
        this.lblTypeError.setVisible(!("Légumes".equalsIgnoreCase(txfType.getText()) || "Fruit".equalsIgnoreCase(txfType.getText())));
        this.lblPriceError.setVisible(txfPrice.getText().isEmpty());
        this.lblQuantityError.setVisible(txfQuantity.getText().isEmpty());

        if (txfName.isVisible() && txfType.isVisible() && txfPrice.isVisible() && txfQuantity.isVisible()) {
            AchatCondiment purchase = new AchatCondiment(txfName.getText(), "Légumes".equalsIgnoreCase(txfType.getText()) ? Color.GREEN : Color.RED, new ImageView(lblImagePath.getText()), txfPrice.getText(), txfQuantity.getText());
            VBox labels = new VBox();
            labels.getChildren().addAll(
                    new Label("Nom :" + purchase.getNom()),
                    new Label("Prix : " + purchase.getPrix()),
                    new Label("Quantité : " + purchase.getQuantite())
            );

            HBox root = new HBox();

            root.getChildren().addAll(labels, purchase.getImage());

        }

    }
}
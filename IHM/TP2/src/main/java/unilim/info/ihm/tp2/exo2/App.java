package unilim.info.ihm.tp2.exo2;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

import java.io.IOException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeFormatterBuilder;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class App extends Application implements EventHandler<MouseEvent> {
    private Label lblSouscrire;
    private Label lblBienvenue;

    private Label lblCivilite;
    private ComboBox<String> cbxCivilite;

    private Label lblNom;
    private TextField txfNom;

    private Label lblPrenom;
    private TextField txfPrenom;

    private Label lblEmail;
    private TextField txfEmail;

    private Label lblConfirmeEmail;
    private TextField txfComfirmeEmail;

    private CheckBox ckbConditions;

    private Button btnSouscrire;

    private Label lblInscrit;

    private Label lblNomErreur;
    private Label lblPrenomErreur;
    private Label lblEmailErreur;
    private Label lblConfirmeEmailErreur;
    private Label lblConfirmeEmailErreurValide;
    private Label lblConfirmeEmailErreurDifferent;
    private Label lblConditionsErreur;

    private static final String MISTER = "M.";
    private static final String MISS = "Mme.";
    private static final String MADAM = "Mlle.";

    @Override
    public void start(Stage stage) throws IOException {
        this.lblSouscrire = new Label("Souscrivez à notre  newsletter !");
        this.lblSouscrire.setUnderline(true);
        this.lblSouscrire.setAlignment(Pos.CENTER);
        this.lblSouscrire.setMaxWidth(Double.MAX_VALUE);

        this.lblBienvenue = new Label("Bienvenue à notre newsletter, inscrivez-vous pour avoir des nouvelles.");
        this.lblBienvenue.setAlignment(Pos.CENTER);
        this.lblBienvenue.setMaxWidth(Double.MAX_VALUE);

        GridPane form = new GridPane();
        form.setVgap(15);

        Insets leftMargin = new Insets(0,0,0,15);

        this.lblCivilite = new Label("Civilité");
        this.cbxCivilite = new ComboBox<>();
        this.cbxCivilite.getItems().addAll(MISTER, MADAM, MISS);
        this.cbxCivilite.setValue(MISTER);
        form.add(this.lblCivilite, 0, 0);
        form.add(this.cbxCivilite, 0, 1);
        GridPane.setMargin(this.lblCivilite, leftMargin);
        GridPane.setMargin(this.cbxCivilite, leftMargin);

        this.lblNom = new Label("Nom");
        this.txfNom = new TextField();
        form.add(this.lblNom, 0, 2);
        form.add(this.txfNom, 0, 3);
        GridPane.setMargin(this.lblNom, leftMargin);
        GridPane.setMargin(this.txfNom, leftMargin);

        this.lblNomErreur = new Label("Le nom est obligatoire");
        this.lblNomErreur.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.lblNomErreur.setTextFill(Color.RED);
        this.lblNomErreur.setVisible(false);
        form.add(this.lblNomErreur, 0, 4);
        GridPane.setMargin(this.lblNomErreur, leftMargin);

        this.lblPrenom = new Label("Prénom");
        this.txfPrenom = new TextField();
        form.add(this.lblPrenom, 1, 2);
        form.add(this.txfPrenom, 1, 3);
        GridPane.setMargin(this.lblPrenom, leftMargin);
        GridPane.setMargin(this.txfPrenom, leftMargin);

        this.lblPrenomErreur = new Label("Le prénom est obligatoire");
        this.lblPrenomErreur.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.lblPrenomErreur.setTextFill(Color.RED);
        this.lblPrenomErreur.setVisible(false);
        form.add(this.lblPrenomErreur, 1, 4);
        GridPane.setMargin(this.lblPrenomErreur, leftMargin);

        this.lblEmail = new Label("Email");
        this.txfEmail = new TextField();
        form.add(this.lblEmail, 0, 5);
        form.add(this.txfEmail, 0, 6);
        GridPane.setMargin(this.lblEmail, leftMargin);
        GridPane.setMargin(this.txfEmail, leftMargin);

        this.lblEmailErreur = new Label("Le mail est obligatoire");
        this.lblEmailErreur.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.lblEmailErreur.setTextFill(Color.RED);
        this.lblEmailErreur.setVisible(false);
        form.add(this.lblEmailErreur, 0, 7);
        GridPane.setMargin(this.lblEmailErreur, leftMargin);

        this.lblConfirmeEmail = new Label("Confirmez votre email");
        this.txfComfirmeEmail = new TextField();
        form.add(this.lblConfirmeEmail, 1, 5);
        form.add(this.txfComfirmeEmail, 1, 6);
        GridPane.setMargin(this.lblConfirmeEmail, leftMargin);
        GridPane.setMargin(this.txfComfirmeEmail, leftMargin);

        this.lblConfirmeEmailErreur = new Label("La vérification du mail est obligatoire");
        this.lblConfirmeEmailErreur.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.lblConfirmeEmailErreur.setTextFill(Color.RED);
        this.lblConfirmeEmailErreur.setVisible(false);
        form.add(this.lblConfirmeEmailErreur, 1, 7);
        GridPane.setMargin(this.lblConfirmeEmailErreur, leftMargin);

        this.lblConfirmeEmailErreurValide = new Label("La mail n'est pas valide");
        this.lblConfirmeEmailErreurValide.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.lblConfirmeEmailErreurValide.setTextFill(Color.RED);
        this.lblConfirmeEmailErreurValide.setVisible(false);
        form.add(this.lblConfirmeEmailErreurValide, 0, 7);
        GridPane.setMargin(this.lblConfirmeEmailErreurValide, leftMargin);

        this.lblConfirmeEmailErreurDifferent = new Label("La vérification du mail est obligatoire");
        this.lblConfirmeEmailErreurDifferent.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.lblConfirmeEmailErreurDifferent.setTextFill(Color.RED);
        this.lblConfirmeEmailErreurDifferent.setVisible(false);
        form.add(this.lblConfirmeEmailErreurDifferent, 1, 7);
        GridPane.setMargin(this.lblConfirmeEmailErreurDifferent, leftMargin);

        this.ckbConditions = new CheckBox("J'accepte les conditions générales d'utilisation de la newsletter.");

        this.lblConditionsErreur = new Label("Il faut accepter la CGU");
        this.lblConditionsErreur.setFont(Font.font(null, FontWeight.BOLD, -1));
        this.lblConditionsErreur.setTextFill(Color.RED);
        this.lblConditionsErreur.setVisible(false);

        HBox hboxBtn = new HBox();
        hboxBtn.setMaxWidth(Double.MAX_VALUE);
        hboxBtn.setAlignment(Pos.CENTER);

        this.btnSouscrire = new Button("Souscrire");
        this.btnSouscrire.setOnMouseClicked(this);

        hboxBtn.getChildren().add(btnSouscrire);

        this.lblInscrit = new Label("Utilisater non inscrit");
        this.lblInscrit.setAlignment(Pos.CENTER);
        this.lblInscrit.setMaxWidth(Double.MAX_VALUE);

        VBox root = new VBox();
        root.setSpacing(15);
        VBox.setMargin(this.ckbConditions, leftMargin);
        VBox.setMargin(this.lblConditionsErreur, leftMargin);

        root.getChildren().addAll(lblSouscrire, lblBienvenue, form, ckbConditions, lblConditionsErreur, hboxBtn, lblInscrit);

        Scene scene = new Scene(root, 600, 400);
        stage.setTitle("Application Newsletter");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

    @Override
    public void handle(MouseEvent event) {
        this.lblNomErreur.setVisible(this.txfNom.getText().isEmpty());
        this.lblPrenomErreur.setVisible(this.txfPrenom.getText().isEmpty());
        this.lblEmailErreur.setVisible(this.txfEmail.getText().isEmpty());
        this.lblConfirmeEmailErreur.setVisible(this.txfComfirmeEmail.getText().isEmpty());
        this.lblConditionsErreur.setVisible(!this.ckbConditions.isSelected());

        Pattern pattern = Pattern.compile(".+@.+\\..+");

        if (!this.txfComfirmeEmail.getText().equals(this.txfEmail.getText())) {
            this.lblConfirmeEmailErreurDifferent.setVisible(true);
        } else if (!pattern.matcher(this.txfEmail.getText()).find()) {
            this.lblConfirmeEmailErreurDifferent.setVisible(false);
            this.lblConfirmeEmailErreurValide.setVisible(true);
        } else {
            this.lblConfirmeEmailErreurDifferent.setVisible(false);
            this.lblConfirmeEmailErreurValide.setVisible(false);
            if (!this.txfNom.getText().isEmpty() && !this.txfPrenom.getText().isEmpty() && !this.txfEmail.getText().isEmpty() && !this.txfComfirmeEmail.getText().isEmpty() && this.ckbConditions.isSelected()) {
                LocalDateTime date = LocalDateTime.now();
                DateTimeFormatter format = DateTimeFormatter.ofPattern("dd/MM/yyyy à hh:mm:ss");
                this.lblInscrit.setText(this.cbxCivilite.getValue() + " " + this.txfPrenom.getText() + " " + this.txfNom.getText() + " s'est inscrit(e) le " + date.format(format));
            }
        }


    }
}
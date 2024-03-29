package org.example.r202_td1;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class DeuxiemeExo extends Application {
	private Label lblUtilisateur;
	private TextField tfdUtilisateur;
	private Label lblMotDePasse;
	private PasswordField pfdMotDePasse;
	private Label lblApplication;
	private Label lblInfosBas;
	private Label lblTitre;
	private Button btnValider;
	private ComboBox<String> cbxMenu;

	@Override
	public void start(Stage stage) throws Exception {
		BorderPane root = new BorderPane();

		lblUtilisateur = new Label("Username : ");
		lblMotDePasse = new Label("Mot de passe : ");
		lblApplication = new Label("Application : ");
		lblTitre = new Label("Veuiller saisir vos informations de login");
		lblTitre.setAlignment(Pos.CENTER);
		lblTitre.setUnderline(true);
		lblTitre.setMaxWidth(Double.MAX_VALUE);
		lblInfosBas = new Label("Login de <xxxx> pour application <xxxx> le xx/xx/xxxx à hh:mm:ss");
		lblInfosBas.setAlignment(Pos.CENTER);
		lblInfosBas.setMaxWidth(Double.MAX_VALUE);
		pfdMotDePasse = new PasswordField();
		tfdUtilisateur = new TextField();

		btnValider = new Button("Valider");
		cbxMenu = new ComboBox<String>();
		cbxMenu.getItems().addAll("Comptabilité", "Paye", "Gestion de prodution");
		cbxMenu.setValue();
		tfdUtilisateur = new TextField("Utilisateur");
		tfdUtilisateur= new PasswordField();

		GridPane grid = new GridPane();
		grid.add(lblUtilisateur, 0,0);
		grid.add(lblMotDePasse, 0,1);
		grid.add(lblApplication, 0,2);
		grid.add(tfdUtilisateur, 1,0);
		grid.add(pfdMotDePasse, 1,1);
		grid.add(cbxMenu, 1,2);

		grid.setAlignment(Pos.CENTER);
		grid.setMaxHeight(Double.MAX_VALUE);

		Scene scene = new Scene(root, 320, 240);

		root.setTop(lblTitre);

		root.setBottom(lblInfosBas);

		root.setRight(btnValider);

		root.setCenter(grid);

		BorderPane.setAlignment(this.btnValider ,Pos.CENTER);
		stage.setScene(scene);
		stage.setTitle("Application Login");
		stage.show();
	}

	public static void main(String[] args) {
		Application.launch();
	}
}

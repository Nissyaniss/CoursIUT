package org.example.r202_td1;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

import java.io.IOException;

public class PremierExo extends Application {
	@Override
	public void start(Stage stage) throws IOException {
		StackPane root = new StackPane();

		Button btn = new Button();
		btn.setText("Valider");

		root.getChildren().add(btn);

		Scene scene = new Scene(root, 320, 240);
		stage.setTitle("Première fenêtre");
		stage.setScene(scene);
		stage.show();
	}

	public static void main(String[] args) {
		for (int i = 0; i < args.length; i++) {
			System.out.println("arguments i = " + args[i]);
		}

		Application.launch();
	}
}
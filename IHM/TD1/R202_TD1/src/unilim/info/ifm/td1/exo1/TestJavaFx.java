package unilim.info.ifm.td1.exo1;

import javafx.application.Application;
import javafx.stage.Stage;

public class TestJavaFx extends Application {

	@Override
	public void start(Stage primaryStage) throws Exception {
		StackPane root = new StackPane;

		Button btn = new Button(); //PAS AWT JAVAFX
		btn.setText("Valider");

		root.getChildren().add(btn);

		Scene scene = new Scene(root, 400, 170);

		primaryStage.setScene(scene);
		primaryStage.setTitle("Première fenêtre");
		primaryStage.show();
	}

	public static void main(String[] args) {
		for (int i = 0; i < args.length; i++) {
			System.out.println("argument i = " + args[i]);
		}

		Application.lauch(args);
	}
}

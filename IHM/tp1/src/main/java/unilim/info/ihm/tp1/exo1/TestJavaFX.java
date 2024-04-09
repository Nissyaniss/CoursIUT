package unilim.info.ihm.tp1.exo1;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import java.io.IOException;

public class TestJavaFX extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        StackPane root = new StackPane();
        Button btn = new Button("Valider");
        root.getChildren().add(btn);


        Scene scene = new Scene(root, 600, 250);
        stage.setScene(scene);
        stage.setTitle("Première Interface");
        stage.show();

    }

    public static void main(String[] args) {
        launch(args);
    }
}
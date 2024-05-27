package org.example.tp5;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.image.ImageView;
import javafx.stage.Stage;

import java.io.IOException;

public class HereWeGoApp extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Group root = new Group();

        ImageView background = new ImageView("/niveau.jpg");

        ImageView mario = new ImageView("/droite.png");
        mario.setFitHeight(30);
        mario.setFitWidth(20);
        mario.setPreserveRatio(true);
        mario.setX(14);
        mario.setY(530);

        MoveMarioController controller = new MoveMarioController(mario);

        root.getChildren().addAll(background, mario);

        Scene scene = new Scene(root, 1200, 622);

        scene.setOnKeyPressed(controller);

        stage.resizableProperty().setValue(Boolean.FALSE);
        stage.setTitle("Here we go");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
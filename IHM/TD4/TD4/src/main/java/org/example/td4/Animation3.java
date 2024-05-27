package org.example.td4;

import javafx.animation.*;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.io.IOException;

public class Animation3 extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        StackPane root = new StackPane();

        BackgroundImage bgi = creerImageFond();
        Background background = new Background(bgi);

        ImageView personnage = changerPersonnage();

        MovePixelController movePixelController = new MovePixelController(personnage);

        root.getChildren().add(personnage);
        root.setBackground(background);

        Scene scene = new Scene(root, 800, 600);

        scene.setOnKeyPressed(movePixelController);

        stage.setResizable(false);
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

    private BackgroundImage creerImageFond() {
        return new BackgroundImage(
                new Image(getClass().getResource("/foot.jpg").toExternalForm()),
                BackgroundRepeat.NO_REPEAT,
                BackgroundRepeat.NO_REPEAT,
                BackgroundPosition.CENTER,
                new BackgroundSize(
                        100,
                        100,
                        true,
                        true,
                        true,
                        false
                )
        );
    }

    private ImageView changerPersonnage() {
        return new ImageView(
                new Image(
                        getClass().getResource("/personnage.png").toExternalForm(),
                        80,
                        80,
                        true,
                        false
                )
        );
    }

    private Timeline animerPersonnage(ImageView personnage) {
        KeyValue kv = new KeyValue(personnage.translateXProperty(), personnage.translateXProperty().get() + 300);

        KeyFrame kf = new KeyFrame(Duration.seconds(2), kv);

        Timeline timeline = new Timeline();
        timeline.getKeyFrames().add(kf);
        timeline.setCycleCount(3);
        timeline.setAutoReverse(true);

        return timeline;
    }
}
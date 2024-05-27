package org.example.td4;

import javafx.animation.*;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.io.IOException;

public class Animation2 extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Group root = new Group();

        Rectangle rectangle = new Rectangle(50, 50, 150, 100);
        rectangle.setFill(Color.BLUE);

        Transition anim = animerRectangle(rectangle);
        Transition fade = animerRectangleFade(rectangle);
        //SequentialTransition sequential = new SequentialTransition(anim, fade);
        ParallelTransition parallel = new ParallelTransition(anim, fade);

        FinAnimationHandler ctrl = new FinAnimationHandler();
        parallel.setOnFinished(ctrl);

        parallel.play();
        //sequential.play();
        //anim.play();
        //fade.play();

        root.getChildren().addAll(rectangle);

        Scene scene = new Scene(root, 600, 200);
        scene.setFill(Color.LIGHTGREEN);

        stage.setTitle("Hello!");
        stage.setResizable(false);
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

    private Transition animerRectangle(Rectangle rectangle) {
        TranslateTransition translateTransition = new TranslateTransition(Duration.seconds(2), rectangle);

        translateTransition.setByX(350);
        translateTransition.setCycleCount(3);
        translateTransition.setAutoReverse(true);
        translateTransition.setInterpolator(Interpolator.EASE_BOTH);
        return translateTransition;
    }

    private Transition animerRectangleFade(Rectangle rectangle) {
        FadeTransition fadeTransition = new FadeTransition(Duration.seconds(2), rectangle);

        fadeTransition.setFromValue(1.0);
        fadeTransition.setToValue(0.0);
        return fadeTransition;
    }

    private class FinAnimationHandler implements EventHandler<ActionEvent> {

        @Override
        public void handle(ActionEvent event) {
            Alert alert = new Alert(Alert.AlertType.INFORMATION);

            alert.setTitle("Fin Animation");
            alert.setHeaderText(null);
            alert.setContentText("L'animation est terminée");
            alert.show();
        }
    }
}
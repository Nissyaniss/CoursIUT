package org.example.td4;

import javafx.animation.AnimationTimer;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

import java.io.IOException;

public class Animation extends Application {

    private Label lblNbFrame;
    private Integer nbFrame = 0;

    @Override
    public void start(Stage stage) throws IOException {
        Group root = new Group();

        Rectangle rectangle = new Rectangle(50, 50, 150, 100);
        rectangle.setFill(Color.BLUE);

        AnimationTimer anim = animerRectangle(rectangle);

        anim.start();

        Node libelle = creerLibelleFrame();

        root.getChildren().addAll(libelle, rectangle);

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

    private AnimationTimer animerRectangle(Rectangle rectangle) {
        return new AnimationTimer() {
            @Override
            public void handle(long now) {
                nbFrame++;
                lblNbFrame.setText(String.valueOf(nbFrame));
                if (rectangle.xProperty().get() < 400) {
                    rectangle.xProperty().set(rectangle.xProperty().get() + 1);
                } else {
                    stop();
                }

                if (rectangle.opacityProperty().get() > 0) {
                    rectangle.opacityProperty().set(rectangle.opacityProperty().get() - (1/350));
                } else {
                    stop();
                }

            }
        };
    }

    private Node creerLibelleFrame() {
        lblNbFrame = new Label("0");
        Label titreLabel = new Label("NbFrames = ");
        titreLabel.setFont(Font.font(null, FontWeight.BOLD, 20));
        lblNbFrame.setFont(Font.font(null, FontWeight.BOLD, 20));

        return new HBox(5, titreLabel, lblNbFrame);
    }
}
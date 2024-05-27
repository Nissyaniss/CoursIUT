package org.example.tp5;

import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.animation.TranslateTransition;
import javafx.beans.value.WritableValue;
import javafx.event.EventHandler;
import javafx.scene.image.Image;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.image.ImageView;
import javafx.util.Duration;

public class MoveMarioController implements EventHandler<KeyEvent> {

    private ImageView personnage;
    private Boolean directionLeft = false;

    public MoveMarioController(ImageView personnage) {
        this.personnage = personnage;
    }

    @Override
    public void handle(KeyEvent event) {
        if (event.getCode() == KeyCode.LEFT) {
            if (!directionLeft) {
                personnage.setImage(new Image("/gauche.png"));
                directionLeft = true;
            }
            Timeline timeline = animerPersonnage(personnage.translateXProperty(), personnage.translateXProperty().get() - 20);
            timeline.play();
        } else if (event.getCode() == KeyCode.RIGHT) {
            if (directionLeft) {
                personnage.setImage(new Image("/droite.png"));
                directionLeft = false;
            }
            Timeline timeline = animerPersonnage(personnage.translateXProperty(), personnage.translateXProperty().get() + 20);
            timeline.play();
        } else if (event.getCode() == KeyCode.SPACE) {
            sautTransition();
        }
    }

    private void sautTransition() {
        TranslateTransition transition1 = new TranslateTransition(Duration.millis(1), personnage);
        transition1.setByY(-50);
        if (directionLeft) {
            transition1.setByX(-50);
        } else {
            transition1.setByX(50);
        }
        transition1.setOnFinished(e -> {
                    TranslateTransition transition2 = new TranslateTransition(Duration.millis(1), personnage);
                    transition2.setByY(50);
                    if (directionLeft) {
                        transition2.setByX(-50);
                    } else {
                        transition2.setByX(50);
                    }
                    transition2.play();
                });
        transition1.play();

    }

    private Timeline animerPersonnage(WritableValue<Number> prop, Number valeurCible) {
        KeyValue kv = new KeyValue(prop, valeurCible);

        KeyFrame kf = new KeyFrame(Duration.seconds(0.1), kv);

        Timeline timeline = new Timeline();
        timeline.getKeyFrames().add(kf);

        return timeline;
    }
}

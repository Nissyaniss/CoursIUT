package org.example.td4;

import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.PathTransition;
import javafx.animation.Timeline;
import javafx.beans.value.WritableValue;
import javafx.event.EventHandler;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.shape.ArcTo;
import javafx.scene.shape.MoveTo;
import javafx.scene.shape.Path;
import javafx.util.Duration;

public class MovePixelController implements EventHandler<KeyEvent> {

    private ImageView personnage;

    private Boolean directionLeft = false;

    public MovePixelController(ImageView personnage) {
        this.personnage = personnage;
    }

    @Override
    public void handle(KeyEvent event) {
        if (event.getCode() == KeyCode.LEFT) {
            directionLeft = true;
            Timeline timeline = animerPersonnage(personnage.translateXProperty(), personnage.translateXProperty().get() - 30);
            timeline.play();
        } else if (event.getCode() == KeyCode.RIGHT) {
            directionLeft = false;
            Timeline timeline = animerPersonnage(personnage.translateXProperty(), personnage.translateXProperty().get() + 30);
            timeline.play();
        } else if (event.getCode() == KeyCode.UP) {
            Timeline timeline = animerPersonnage(personnage.translateYProperty(), personnage.translateYProperty().get() - 30);
            timeline.play();
        } else if (event.getCode() == KeyCode.DOWN) {
            Timeline timeline = animerPersonnage(personnage.translateYProperty(), personnage.translateYProperty().get() + 30);
            timeline.play();
        } else if (event.getCode() == KeyCode.SPACE) {
            sautEnArcDeCercle();
        }
    }

    private void sautEnArcDeCercle() {
        Path path = new Path();

        MoveTo elem1 = new MoveTo(personnage.translateXProperty().get(), personnage.translateYProperty().get());

        ArcTo elem2 = new ArcTo(
                10,
                10,
                0,
                personnage.translateXProperty().get() + (60 * (directionLeft ? -1 : 1)) + 40,
                personnage.translateXProperty().get() + personnage.getY() + 40,
                true,
                !directionLeft
        );

        path.getElements().addAll(elem1, elem2);

        PathTransition pathTransition = new PathTransition(Duration.millis(600), path, personnage);

        pathTransition.play();
    }

    private Timeline animerPersonnage(WritableValue<Number> prop, Number valeurCible) {
        KeyValue kv = new KeyValue(prop, valeurCible);

        KeyFrame kf = new KeyFrame(Duration.seconds(2), kv);

        Timeline timeline = new Timeline();
        timeline.getKeyFrames().add(kf);
        timeline.setCycleCount(3);
        timeline.setAutoReverse(true);

        return timeline;
    }
}

package unilim.info.ihm.tp6.exo6.r202_tp6.exo1;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

public class DndTextRectangle extends Application {
    Rectangle rectDrag = new Rectangle(50, 100, 150, 100);
    Rectangle rectDrop = new Rectangle(300, 50, 150, 100);

    @Override
    public void start(Stage stage) throws Exception {
        Group root = new Group();
        Scene scene = new Scene(root);

        rectDrag.setFill(Color.BLUE);
        rectDrop.setFill(Color.GREEN);

        DndTextController.manageSourceDragAndDrop(rectDrag);
        DndTextController.manageTargetDragAndDrop(rectDrop);

        root.getChildren().addAll(rectDrag, rectDrop);

        stage.setTitle("WOW");
        stage.setScene(scene);
        stage.show();
    }
}

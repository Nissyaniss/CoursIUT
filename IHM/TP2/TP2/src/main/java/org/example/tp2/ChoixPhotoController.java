package org.example.tp2;

import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.net.MalformedURLException;

public class ChoixPhotoController implements EventHandler<MouseEvent> {
    private Label lblPhoto;
    private Stage stage;

    public ImageView getImageView() {
        return imageView;
    }

    private ImageView imageView;

    public ChoixPhotoController(Label lblPhoto, Stage mainStage) {
        this.lblPhoto = lblPhoto;
        this.stage = mainStage;
        this.imageView = null;
    }

    @Override
    public void handle(MouseEvent event) {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Open Image");
        FileChooser.ExtensionFilter png = new FileChooser.ExtensionFilter("PNG files (*.png)", "*.png");
        FileChooser.ExtensionFilter jpg = new FileChooser.ExtensionFilter("JPG files (*.jpg)", "*.jpg");
        fileChooser.getExtensionFilters().addAll(png, jpg);
        File photo = fileChooser.showOpenDialog(this.stage);
        if (photo != null) {
            lblPhoto.setText(photo.getAbsolutePath());
            try {
                Image img = new Image(photo.toURI().toURL().toString(), 160,160, true, false);
                this.imageView = new ImageView(img);
            } catch (MalformedURLException e) {
                e.printStackTrace();
            }
        }
    }
}

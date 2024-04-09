package org.example.td2;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;
import java.util.Random;

public class Roll extends Application {
    private Label lblCentral;

    private TextArea txaGauche;
    private TextArea txaDroite;

    private Button btnRoll;

    private Button btnFin;

    private ToggleGroup group;

    private Integer nbTirages = 0;
    private static final String ROLL_THE_DICE = "Roll the DICE";
    private static final String TIRAGES = "Tirages :";

    private static final String LINE_SEPARATOR = System.lineSeparator();

    @Override
    public void start(Stage stage) {

        this.group = new ToggleGroup();
        RadioButton rbt2 = new RadioButton("2");
        RadioButton rbt4 = new RadioButton("4");
        RadioButton rbt6 = new RadioButton("6");
        RadioButton rbt8 = new RadioButton("8");
        RadioButton rbt10 = new RadioButton("10");
        RadioButton rbt12 = new RadioButton("12");
        RadioButton rbt20 = new RadioButton("20");
        RadioButton rbt100 = new RadioButton("100");
        this.group.getToggles().addAll(rbt2, rbt4, rbt6, rbt8, rbt10, rbt12, rbt20, rbt100);

        EcouteurRadioBouton listenerBtn = new EcouteurRadioBouton();
        rbt2.setOnMouseClicked(listenerBtn);
        rbt4.setOnMouseClicked(listenerBtn);
        rbt6.setOnMouseClicked(listenerBtn);
        rbt8.setOnMouseClicked(listenerBtn);
        rbt10.setOnMouseClicked(listenerBtn);
        rbt12.setOnMouseClicked(listenerBtn);
        rbt20.setOnMouseClicked(listenerBtn);
        rbt100.setOnMouseClicked(listenerBtn);

        this.lblCentral = new Label("0");
        this.lblCentral.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderWidths.DEFAULT)));
        this.lblCentral.setMaxSize(Double.MAX_VALUE, Double.MAX_VALUE);
        this.lblCentral.setAlignment(Pos.CENTER);
        this.lblCentral.setFont(Font.font(null, FontWeight.BOLD, 100));

        this.txaGauche = new TextArea(ROLL_THE_DICE);
        this.txaGauche.setPrefSize(100, 220);

        this.txaDroite = new TextArea(TIRAGES);
        this.txaDroite.setPrefSize(100, 220);

        EcouteurBouton ecouteurBouton = new EcouteurBouton();
        this.btnRoll = new Button("Roll");
        this.btnFin = new Button("Fin");
        btnRoll.setOnMouseClicked(ecouteurBouton);
        btnFin.setOnMouseClicked(ecouteurBouton);

        HBox hbHaut = new HBox();
        hbHaut.setAlignment(Pos.CENTER);
        hbHaut.getChildren().addAll(rbt2, rbt4, rbt6, rbt8, rbt10, rbt12, rbt20, rbt100);

        HBox hbBas = new HBox();
        hbBas.setAlignment(Pos.CENTER);
        hbBas.getChildren().addAll(btnRoll, btnFin);

        //-------------------------------------------
        BorderPane root = new BorderPane();

        root.setTop(hbHaut);
        root.setLeft(txaGauche);
        root.setCenter(lblCentral);
        root.setRight(txaDroite);
        root.setBottom(hbBas);

        Scene scene = new Scene(root, 320, 240);
        stage.setTitle("Roll the dice");
        stage.setScene(scene);
        stage.show();
    }

    private class EcouteurRadioBouton implements EventHandler<MouseEvent> {
        @Override
        public void handle(MouseEvent mouseEvent) {
            RadioButton radioButton = (RadioButton) mouseEvent.getSource();
            String nbrFace = radioButton.getText();
            txaGauche.setText(ROLL_THE_DICE + LINE_SEPARATOR + LINE_SEPARATOR + "dés à " + nbrFace + " faces");
        }
    }

    private class EcouteurBouton implements  EventHandler<MouseEvent> {

        private final Random random = new Random();

        @Override
        public void handle(MouseEvent mouseEvent) {
            if (mouseEvent.getSource() == btnRoll) {
                if (group.getSelectedToggle() != null) {
                    nbTirages++;
                    txaDroite.setText(TIRAGES + LINE_SEPARATOR + nbTirages + " jets");
                    RadioButton radioButton = (RadioButton) (group.getSelectedToggle());

                    Integer value = Integer.parseInt(radioButton.getText());


                    lblCentral.setText(String.valueOf(lancerDes(value)));
                    if (nbTirages >= 10) {
                        btnRoll.setDisable(true);
                    }
                }


            } else if (mouseEvent.getSource() == btnFin) {
                Platform.exit();
            }
        }

        private int lancerDes(Integer value) {
            return (random.nextInt() * value + 1);
        }
    }



    public static void main(String[] args) {
        launch();
    }
}
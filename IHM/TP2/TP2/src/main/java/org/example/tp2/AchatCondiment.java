package org.example.tp2;

import javafx.scene.image.ImageView;
import javafx.scene.paint.Color;

public class AchatCondiment {
    private String nom;
    private Color couleur;
    private ImageView image;
    private String prix;
    private String quantite;

    public String getNom() {
        return nom;
    }

    public Color getCouleur() {
        return couleur;
    }

    public ImageView getImage() {
        return image;
    }

    public String getPrix() {
        return prix;
    }

    public String getQuantite() {
        return quantite;
    }

    public AchatCondiment(String nom, Color couleur, ImageView image, String prix, String quantite) {
        this.nom = nom;
        this.couleur = couleur;
        this.image = image;
        this.prix = prix;
        this.quantite = quantite;
    }

}

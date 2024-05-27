module org.example.td3 {
    requires javafx.controls;
    requires javafx.fxml;

    opens org.example.td3 to javafx.fxml;
    exports org.example.td3;
}
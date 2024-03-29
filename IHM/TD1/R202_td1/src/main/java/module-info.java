module org.example.r202_td1 {
	requires javafx.controls;
	requires javafx.fxml;


	opens org.example.r202_td1 to javafx.fxml;
	exports org.example.r202_td1;
}
<?php
include_once 'db.php';



if(isset($_POST['submit']))
{    

     $date = $_POST['date'];
     $ID = date("ymd", strtotime($date));  

     $potage = $_POST['potage'];
     $subtitle_potage = $_POST['subtitle_potage'];
     $plat_1 = $_POST['plat_1'];
     $subtitle_plat_1 = $_POST['subtitle_plat_1'];
     $plat_2= $_POST['plat_2'];
     $subtitle_plat_2= $_POST['subtitle_plat_2'];
     $accompagnement= $_POST['accompagnement'];
     $subtitle_accompagnement= $_POST['subtitle_accompagnement'];
     $légumes= $_POST['légumes'];
     $subtitle_légumes= $_POST['subtitle_légumes'];
     $dessert= $_POST['dessert'];
     $subtitle_dessert= $_POST['subtitle_dessert'];

     $sql = "INSERT INTO menu (ID, date, potage, subtitle_potage, plat_1, subtitle_plat_1, plat_2, subtitle_plat_2, accompagnement, subtitle_accompagnement, légumes, subtitle_légumes, dessert, subtitle_dessert)
     VALUES ('$ID', '$date', '$potage', '$subtitle_potage', '$plat_1', '$subtitle_plat_1', '$plat_2', '$subtitle_plat_2', '$accompagnement', '$subtitle_accompagnement', '$légumes', '$subtitle_légumes', '$dessert', '$subtitle_dessert')";
     mysqli_query($conn, $sql);
     mysqli_close($conn);
}
header("Location: http://localhost:8888/wordpress/database/page3.php");

?>

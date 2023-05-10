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

     $sql = "UPDATE menu SET ID = '$ID', date = '$date', potage = '$potage', subtitle_potage = '$subtitle_potage', plat_1 = '$plat_1', subtitle_plat_1 = '$subtitle_plat_1', plat_2 = '$plat_2', subtitle_plat_2 = '$subtitle_plat_2', accompagnement = '$accompagnement', subtitle_accompagnement = '$subtitle_accompagnement', légumes = '$légumes', subtitle_légumes = '$subtitle_légumes', dessert = '$dessert', subtitle_dessert = '$subtitle_dessert' where ID = $ID";
     mysqli_query($conn, $sql);
     mysqli_close($conn);
}
header("Location: http://localhost:8888/wordpress/database/edit3.php");

?>

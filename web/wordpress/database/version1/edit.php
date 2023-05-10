<!DOCTYPE html>
<html>
    <head>
        <title>select sql</title>
        <link rel="stylesheet" href="menu_style.css" type="text/css">
    </head>


    <?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "menu";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT ID, date, potage, subtitle_potage, plat_1, subtitle_plat_1, plat_2, subtitle_plat_2, accompagnement, subtitle_accompagnement, légumes, subtitle_légumes, dessert, subtitle_dessert FROM menu";

$ID = null;
$arr = array();
$arr1 = [];
$result = $conn->query($sql);

$arr_date = array();
$arr_date = [];

$arr_potage = [];

$arr_subtitle_potage = [];

$arr_plat_1 = [];

$arr_subtitle_plat_1 = [];

$arr_plat_2 = [];

$arr_subtitle_plat_2 = [];

$arr_accompagnement = [];

$arr_subtitle_accompagnement = [];

$arr_légumes = [];

$arr_subtitle_légumes = [];

$arr_dessert = [];

$arr_subtitle_dessert = [];

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {

    array_push($arr_date, $row["date"]);
    array_push($arr1, $row["ID"]);

    array_push($arr_potage, $row["potage"]);
    array_push($arr_subtitle_potage, $row["subtitle_potage"]);

    array_push($arr_plat_1, $row["plat_1"]);
    array_push($arr_subtitle_plat_1, $row["subtitle_plat_1"]);

    array_push($arr_plat_2, $row["plat_2"]);
    array_push($arr_subtitle_plat_2, $row["subtitle_plat_2"]);

    array_push($arr_accompagnement, $row["accompagnement"]);
    array_push($arr_subtitle_accompagnement, $row["subtitle_accompagnement"]);

    array_push($arr_légumes, $row["légumes"]);
    array_push($arr_subtitle_légumes, $row["subtitle_légumes"]);

    array_push($arr_dessert, $row["dessert"]);
    array_push($arr_subtitle_dessert, $row["subtitle_dessert"]);

}
}
array_push($arr, $arr1);
array_push($arr_date, $arr_date);


foreach ($arr as $item){
    if(is_array($item)){
        $num = 0;
        $box = '<div class="box">
        <h3>select the menu you want to edit</h3>';
        $close_box = '</div>';
        $select='<select onchange="function1(value)">';
        echo $box;
        echo $select;
        
        foreach ($item as $list){
            echo "<option value='".$num."'>".$list.'</option>';
            $num = $num + 1;
        }
        echo '</select>';
        echo $close_box;
    }
    else {
    }
}
$conn->close();

?>
    <body>
<div id="lundi" class="box">
    <h1 id="del">Menu:</h1>

</div>
<script>
    const num = 0;
    function function1(arg) {
try {
        let div = document.getElementById("del");
        div.parentNode.removeChild(div);
        console.log("success");
        
}
catch {
    console.error("error");
}
try {
        let div1 = document.getElementById("del1");
        div1.parentNode.removeChild(div1);
        console.log("success");
}
catch {
    console.error("error");
}

        let arr_date = <?php echo json_encode($arr_date);?>;
        let date = arr_date[arg];

        let arr_potage = <?php echo json_encode($arr_potage);?>;
        let potage = arr_potage[arg];

        let arr_subtitle_potage = <?php echo json_encode($arr_subtitle_potage);?>;
        let subtitle_potage = arr_subtitle_potage[arg];

        let arr_plat_1 = <?php echo json_encode($arr_plat_1);?>;
        let plat_1 = arr_plat_1[arg];

        let arr_subtitle_plat_1 = <?php echo json_encode($arr_subtitle_plat_1);?>;
        let subtitle_plat_1 = arr_subtitle_plat_1[arg];

        let arr_plat_2 = <?php echo json_encode($arr_plat_2);?>;
        let plat_2 = arr_plat_2[arg];

        let arr_subtitle_plat_2 = <?php echo json_encode($arr_subtitle_plat_2);?>;
        let subtitle_plat_2 = arr_subtitle_plat_2[arg];

        let arr_accompagnement = <?php echo json_encode($arr_accompagnement);?>;
        let accompagnement = arr_accompagnement[arg];

        let arr_subtitle_accompagnement = <?php echo json_encode($arr_subtitle_accompagnement);?>;
        let subtitle_accompagnement = arr_subtitle_accompagnement[arg];

        let arr_légumes = <?php echo json_encode($arr_légumes);?>;
        let légumes = arr_légumes[arg];

        let arr_subtitle_légumes = <?php echo json_encode($arr_subtitle_légumes);?>;
        let subtitle_légumes = arr_subtitle_légumes[arg];

        let arr_dessert = <?php echo json_encode($arr_dessert);?>;
        let dessert = arr_dessert[arg];

        let arr_subtitle_dessert = <?php echo json_encode($arr_subtitle_dessert);?>;
        let subtitle_dessert = arr_subtitle_dessert[arg];

        const parentelement = document.getElementById("lundi");
        let html = `<h1 id="del">${date}</h1>
<div id="del1" class="row">
        <div id="lundi_column0" class="column">
            <div>
                <h1>Edit Lundi</h1>
            <form action="update.php" method="post">
                    <label for="date">date</label><br>
                    <input type="date" name="date" id="date" value="${date}">
                    <br>
                    <br>
                    <label for="potage">potage</label><br>
                    <input type="text" id="potage" name="potage" placeholder="plat" value="${potage}">
                    <input type="text" id="subtitle_potage" name="subtitle_potage" placeholder="subtitle" value="${subtitle_potage}">
                <br>
                <br>
                    <label for="plat_1">plat_1</label><br>
                    <input type="text" id="plat_1" name="plat_1" placeholder="plat" value="${plat_1}">
                    <input type="text" id="subtitle_plat_1" name="subtitle_plat_1" placeholder="subtitle" value="${subtitle_plat_1}">
                <br>
                <br>
                    <label for="plat_2">plat_2</label><br>
                    <input type="text" id="plat_2" name="plat_2" placeholder="plat" value="${plat_2}">
                    <input type="text" id="subtitle_plat_2" name="subtitle_plat_2" placeholder="subtitle" value="${subtitle_plat_2}">
                <br>
                <br>
                    <label for="accompagnement">accompagnement</label><br>
                    <input type="text" id="accompagnement" name="accompagnement" placeholder="plat" value="${accompagnement}">
                    <input type="text" id="subtitle_accompagnement" name="subtitle_accompagnement" placeholder="subtitle" value="${subtitle_accompagnement}">
                <br>
                <br>
                    <label for="légumes">légumes</label><br>
                    <input type="text" id="légumes" name="légumes" placeholder="plat" value="${légumes}">
                    <input type="text" id="subtitle_légumes" name="subtitle_légumes" placeholder="subtitle" value="${subtitle_légumes}">
                <br>
                <br>
                    <label for="dessert">dessert</label><br>
                    <input type="text" id="dessert" name="dessert" placeholder="plat" value="${dessert}">
                    <input type="text" id="subtitle_dessert" name="subtitle_dessert" placeholder="subtitle" value="${subtitle_dessert}">
                <br>
                <br>
                    <input type="submit" class="btn btn-primary" name="submit" value="Submit" >
                </form>
                <br>
            <br>
        `;
        parentelement.insertAdjacentHTML("beforeend", html);
    }
    </script>
</body>
</html>
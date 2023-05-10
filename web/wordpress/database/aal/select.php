<!DOCTYPE html>
<html>
    <title>select sql</title>


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

$sql = "SELECT ID, date FROM menu";

$ID = null;
$arr = array();
$arr1 = [];
$result = $conn->query($sql);

$arr_menu = array();
$arr1_menu = [];


if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    array_push($arr1_menu, $row["date"]);
    array_push($arr1, $row["ID"]);

}
}
array_push($arr, $arr1);
array_push($arr1_menu, $arr_menu);
global $arr1_menu, $arr_menu;
foreach ($arr as $item){
    if(is_array($item)){
        $num = 0;
        $select='<select onchange="function1(value)">';
        echo $select;
        foreach ($item as $list){
            echo "<option value='".$num."'>".$list.'</option>';
            $num = $num + 1;
        }
        echo '</select>';
    }
    else {
        echo "aaaa";
    }
}
$conn->close();

?>

    <body>
        <select name="" id="" onchange="function1(value)">
            <option value="ja">val1</option>
            <option value="function1()"onchange="function1()">val1</option>
    </select>
<script>
    function function1(arg) {
        let arr = <?php echo json_encode($arr1_menu);?>;
        console.log(arr[arg]);
    }
    </script>
</body>

</html>
<!DOCTYPE html>
<html>
<body>
<h1>ppp<h1>
<form action="form.php" method="post">
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" />
    </div>
    <button type="submit">Submit</button>
</form>
<script>
  var at = document.getElementById("email").value.indexOf("@");
var age = document.getElementById("age").value;
var fname = document.getElementById("fname").value;
submitOK = "true";

if (fname.length > 10) {
  alert("The name may have no more than 10 characters");
  submitOK = "false";
}

if (isNaN(age) || age < 1 || age > 100) {
  alert("The age must be a number between 1 and 100");
  submitOK = "false";
}

if (at == -1) {
  alert("Not a valid e-mail!");
  submitOK = "false";
}

if (submitOK == "false") {
  return false;
}
</script>
<?php
  $db_host = 'localhost';
  $db_user = 'root';
  $db_password = 'root';
  $db_db = 'database_test';
 
  $mysqli = @new mysqli(
    $db_host,
    $db_user,
    $db_password,
    $db_db
  );
	
  if ($mysqli->connect_error) {
    echo 'Errno: '.$mysqli->connect_errno;
    echo '<br>';
    echo 'Error: '.$mysqli->connect_error;
    exit();
  }

  echo "Connected successfully";
 
  $sql = "INSERT INTO test (n1,n2,n3,n4) VALUES ('1', '1', '1','1')";
  if (mysqli_query($mysqli, $sql)) {
        echo "New record created successfully";
  } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($mysqli);
  }
  $mysqli->close();
?>

</body>
</html>
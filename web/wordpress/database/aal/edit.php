<!DOCTYPE html>
<html>
    <head>
        <title>edit sql tmpl</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
        <style type="text/css">
        label {
color: #eee;
font-weight: serif;
/* display: block; */
}

.submit {
  background-color: #08d;
  border-radius: 12px;
  border: 0;
  padding: 12px;
  box-sizing: border-box;
  color: #eee;
  cursor: pointer;
  font-size: 18px;
  height: 50px;
  /* margin-top: 38px; */
  // outline: 0;
}

::placeholder {
    vertical-align: baseline;
}

input[type='text']{
 font-size: 30px;
 color: rgba(255, 255, 255, 0.4);
 line-height: 30px;
}
input[type="text"], textarea {


background-color: #303245;
border-radius: 5px;
border: 0;
box-sizing: border-box;
color: #eee;
font-size: 18px;
height: 50px;
outline: 0;
padding: 10px 20px 0;
width: 90%;

}

h1 {
font-weight: serif;
color: #eee;
    
}

input[type="date"], textarea {
background-color: #303245;
border-radius: 5px;
border: 0;
box-sizing: border-box;
color: #eee;
font-size: 18px;
height: 100%;
outline: 0;
padding: 4px 20px 0;


}
.box {

width: 100%;
background-color: #15172b; ;
width: 90%;
padding: 10px;
height: 100%;
margin: 0px;
border-radius:10px;
box-shadow: 10px 10px 5px 0px rgba(70, 59, 59, 0.75);

}

.row {
display: flex;
margin: auto;
width: 100%;
border: 0px solid black;
padding: 1px;
height: 100%;
}
            
.column {
flex: 100%;
}

        </style>

    </head>
    <body>

<h1>a1</h1>
<?php
       include_once 'db.php';

       if ($conn->connect_error) {
           die("Connection failed: " . $conn->connect_error);
         }

         $sql = "SELECT potage, subtitle_potage, plat_1, subtitle_plat_1, plat_2, subtitle_plat_2, accompagnement, subtitle_accompagnement, légumes, subtitle_légumes, dessert, subtitle_dessert FROM menu";
         $result = $conn->query($sql);
         $row = $result->fetch_assoc();
         echo $row["potage"];
         echo $row["plat_1"];
         $potage = $row["potage"];

         if ($result->num_rows > 0) {
           // output data of each row
           while($row = $result->fetch_assoc()) {
               $potage = $row["potage"];
               $subtitle_potage = $row["subtitle_potage"];

               echo $potage;
               $plat_1 = $row["plat_1"];
               $subtitle_plat_1 = $row["subtitle_plat_1"];

               $plat_2 = $row["plat_2"];
               $subtitle_plat_2 = $row["subtitle_plat_2"];

               $accompagnement = $row["accompagnement"];
               $subtitle_accompagnement = $row["subtitle_accompagnement"];

               $légumes = $row["légumes"];
               $subtitle_légumes = $row["subtitle_légumes"];

               $dessert = $row["dessert"];
               $subtitle_dessert = $row["subtitle_dessert"];

           }}

       mysqli_close($conn);

    ?>
    <p><?php echo $row["potage"];?></p>
    <div id="lundi" class="row">
        <div id="lundi_column0" class="column">
            <div class="box">
            <form action="replace.php" method="post">
                    <label for="potage">potage</label><br>
                    <input type="text" id="potage" name="potage" placeholder="plat" value=<?php echo $potage;?>>
                    <input type="text" id="subtitle_potage" name="subtitle_potage" placeholder="subtitle" value="<?=$row["subtitle_potage"]?>">
                <br>
                <br>
                    <label for="plat_1">plat_1</label><br>
                    <input type="text" id="plat_1" name="plat_1" placeholder="plat" value="<?=$plat_1?>">
                    <input type="text" id="subtitle_plat_1" name="subtitle_plat_1" placeholder="subtitle" value="<?=$subtitle_plat_1?>">
                <br>
                <br>
                    <label for="plat_2">plat_2</label><br>
                    <input type="text" id="plat_2" name="plat_2" placeholder="plat" value="<?=$plat_2?>">
                    <input type="text" id="subtitle_plat_2" name="subtitle_plat_2" placeholder="subtitle" value="<?=$subtitle_plat_2?>">
                <br>
                <br>
                    <label for="accompagnement">accompagnement</label><br>
                    <input type="text" id="accompagnement" name="accompagnement" placeholder="plat" value="<?=$accompagnement?>">
                    <input type="text" id="subtitle_accompagnement" name="subtitle_accompagnement" placeholder="subtitle" value="<?=$subtitle_accompagnement?>">
                <br>
                <br>
                    <label for="légumes">légumes</label><br>
                    <input type="text" id="légumes" name="légumes" placeholder="plat" value="<?=$légumes?>">
                    <input type="text" id="subtitle_légumes" name="subtitle_légumes" placeholder="subtitle" value="<?=$subtitle_légumes?>">
                <br>
                <br>
                    <label for="dessert">dessert</label><br>
                    <input type="text" id="dessert" name="dessert" placeholder="plat" value="<?=$dessert?>">
                    <input type="text" id="subtitle_dessert" name="subtitle_dessert" placeholder="subtitle" value="<?=$subtitle_dessert?>">
                <br>
                <br>
                    <input type="submit" class="btn btn-primary" name="submit" value="Submit" >
                </form>
                <br>
            <br>

                <!-- <button id="remove_lundi0" onClick="remove_lundi('lundi_column0')">remove</button> -->

            </div>
        </div>
</div>
 
    </body>
</html>
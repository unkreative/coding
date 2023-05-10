<!DOCTYPE html>
<html>
    <head>
        <title>edit</title>
    </head>
    <body>
        <h1>hello world 2</h1>
        <?php 
        include_once 'db.php';

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
          }

          $sql = "SELECT potage, plat_1, plat_2, accompagnement, légumes, dessert FROM menu";
          $result = $conn->query($sql);
          echo "hello";
          if ($result->num_rows > 0) {
            // output data of each row
            while($row = $result->fetch_assoc()) {
                echo $row["potage"]. $row["plat_1"] . $row["plat_2"]. $row["accompagnement"]. $row["légumes"]. $row["desssert"] . "<br>";
                $potage = $row["potage"];
            }
          } else {
            echo "0 results";
          }

        mysqli_close($conn);

        ?>
        <h1>yield</h1>
        <form action="insert.php" methhod="post">
            <label for="potage">potage:</label>
            <input type="text" name="potage" id="potage"> 
        </form>
        <div id="insert">
            <h1>hello</h1>

        <button onClick="insert_sql()">insert sql</button>
        <script>
            function insert_sql () {
            let sql1 = '<?=$potage?>'
            console.log(sql1)
            // make the new lundi tab
            const parentelement = document.getElementById('insert');
            let html = `<h1>${sql1}<h1>`
            parentelement.insertAdjacentHTML("beforeend", html);

            }
            </script>
            <input type="text" name="test1" id="test1" value='<?=$potage?>'>
        
        </div>

        <body>
    <section>
        <h1>GeeksForGeeks</h1>
        <!-- TABLE CONSTRUCTION -->
        <table>
            <tr>
                <th>GFG UserHandle</th>
                <th>Practice Problems</th>
                <th>Coding Score</th>
                <th>GFG Articles</th>
            </tr>
            <!-- PHP CODE TO FETCH DATA FROM ROWS -->
            <?php
                // LOOP TILL END OF DATA
                while($rows=$result->fetch_assoc())
                {
            ?>
            <tr>
                <!-- FETCHING DATA FROM EACH
                    ROW OF EVERY COLUMN -->
                <td><?php echo $rows['potage'];?></td>
                <td><?php echo $rows['plat_1'];?></td>
                <td><?php echo $rows['plat_2'];?></td>
                <td><?php echo $rows['accompagnement'];?></td>
                <td><?php echo $rows['légumes'];?></td>
                <td><?php echo $rows['dessert'];?></td>
            </tr>
            <?php
                }
            ?>
        </table>
    </section>
</body>
 
</body>
</html>
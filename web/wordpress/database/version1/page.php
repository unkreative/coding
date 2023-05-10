<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>menu</title>
        <link rel="stylesheet" href="menu_style.css" type="text/css">
       
    </head>
    <body>
    
       <div id="lundi">
            <div id="lundi_column0">
                <div class="box">
                    <h1>lundi</h1>
                    <form action="insert.php" method="post">
                        
                            <label for="date">date</label><br>
                            <input type="date" name="date" id="date">
                            <br>
                            <br>

                            <label for="potage">potage</label><br>
                            <input type="text" id="potage" name="potage" placeholder="plat">
                            <input type="text" id="subtitle_potage" name="subtitle_potage" placeholder="subtitle">
                        <br>
                        <br>
                            <label for="plat_1">plat_1</label><br>
                            <input type="text" id="plat_1" name="plat_1" placeholder="plat">
                            <input type="text" id="subtitle_plat_1" name="subtitle_plat_1" placeholder="subtitle">
                        <br>
                        <br>
                            <label for="plat_2">plat_2</label><br>
                            <input type="text" id="plat_2" name="plat_2" placeholder="plat">
                            <input type="text" id="subtitle_plat_2" name="subtitle_plat_2" placeholder="subtitle">
                        <br>
                        <br>
                            <label for="accompagnement">accompagnement</label><br>
                            <input type="text" id="accompagnement" name="accompagnement" placeholder="plat">
                            <input type="text" id="subtitle_accompagnement" name="subtitle_accompagnement" placeholder="subtitle">
                            <br>
                            <br>
                                <label for="légumes">légumes</label><br>
                                <input type="text" id="légumes" name="légumes" placeholder="plat">
                                <input type="text" id="subtitle_légumes" name="subtitle_légumes" placeholder="subtitle">
                            <br>
                            <br>
                                <label for="dessert">dessert</label><br>
                                <input type="text" id="dessert" name="dessert" placeholder="plat">
                                <input type="text" id="subtitle_dessert" name="subtitle_dessert" placeholder="subtitle">
                            <br>
                            <br>
                                <input type="submit" class="submit" name="submit" value="Submit" >
                            </form>
                            <br>
                        <br>

                            <button id="remove_lundi0" onClick="remove_lundi('lundi_column0')">remove</button>

                </div>
            </div>
        </div>
       
       <script>
        var num_lundi;
        num_lundi = 1
        function remove_lundi(div_id) {
            // delete thing
            let div = document.getElementById(div_id);
            div.parentNode.removeChild(div);
            // make new button

            const h2 = document.getElementById("lundi");
            let html = "<div class='column' id='new_btn_lundi'><button onClick=add_lundi()>new Lundi</button></div>";
            h2.insertAdjacentHTML("beforeend", html);

        }
        function add_lundi() {
            // remove new button
            let div = document.getElementById('new_btn_lundi');
            div.parentNode.removeChild(div);
            // make the new lundi tab
            const parentelement = document.getElementById("lundi");
            let html = `
            <div id="lundi_column${num_lundi}">
                <div class="box">
                    <h1>lundi</h1>
                    <form action="insert.php" method="post">
                        
                            <label for="date">date</label><br>
                            <input type="date" name="date" id="date">
                            <br>
                            <br>

                            <label for="potage">potage</label><br>
                            <input type="text" id="potage" name="potage" placeholder="plat">
                            <input type="text" id="subtitle_potage" name="subtitle_potage" placeholder="subtitle">
                        <br>
                        <br>
                            <label for="plat_1">plat_1</label><br>
                            <input type="text" id="plat_1" name="plat_1" placeholder="plat">
                            <input type="text" id="subtitle_plat_1" name="subtitle_plat_1" placeholder="subtitle">
                        <br>
                        <br>
                            <label for="plat_2">plat_2</label><br>
                            <input type="text" id="plat_2" name="plat_2" placeholder="plat">
                            <input type="text" id="subtitle_plat_2" name="subtitle_plat_2" placeholder="subtitle">
                        <br>
                        <br>
                            <label for="accompagnement">accompagnement</label><br>
                            <input type="text" id="accompagnement" name="accompagnement" placeholder="plat">
                            <input type="text" id="subtitle_accompagnement" name="subtitle_accompagnement" placeholder="subtitle">
                            <br>
                            <br>
                                <label for="légumes">légumes</label><br>
                                <input type="text" id="légumes" name="légumes" placeholder="plat">
                                <input type="text" id="subtitle_légumes" name="subtitle_légumes" placeholder="subtitle">
                            <br>
                            <br>
                                <label for="dessert">dessert</label><br>
                                <input type="text" id="dessert" name="dessert" placeholder="plat">
                                <input type="text" id="subtitle_dessert" name="subtitle_dessert" placeholder="subtitle">
                            <br>
                            <br>
                                <input type="submit" class="submit" name="submit" value="Submit" >
                            </form>
                            <br>
                        <br>

                            <button id="remove_lundi${num_lundi}" onClick="remove_lundi('lundi_column${num_lundi}')">remove</button>

                </div>
            </div>

`;
            parentelement.insertAdjacentHTML("beforeend", html);
            num_lundi = num_lundi + 1


        }
       </script>

    </body>
</html>
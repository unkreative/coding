<!DOCTYPE html>
<html lang="en" >
<head>
    <meta charset="UTF-8">
    <title>menu</title>
    
    <style type="text/css">
        /*   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css"> */
.row {
  display: flex;
  margin: auto;
  width: 100%;
  border: 1px solid black;
  padding: 10px;
  height: 75%;
}
.box {
background-color: #cfc ;
width: 300px;
padding: 50px;
height: 75%;
margin: 20px;
border-radius: 18px 18px 18px 18px;
-moz-border-radius: 18px 18px 18px 18px;
-webkit-border-radius: 18px 18px 18px 18px;
border: 0px solid #000000;
webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
-moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
}
.column {
  flex: 70%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
.test {
    background-color: #cfc ;
    width: 300px;
    padding: 50px;
    height: 75px;
    margin: 20px;
    border-radius: 18px 18px 18px 18px;
    -moz-border-radius: 18px 18px 18px 18px;
    -webkit-border-radius: 18px 18px 18px 18px;
    border: 0px solid #000000;
    webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
}
.remove_test {
    text-align:center
}
    </style>
</head>
<body>

    <div class="row">
        <div class="column">

            <div id="test1" class="test">
                <h1>hello1</h1>
            </div>
        </div>

        <div class="column">
            <div id="test2" class="test">
                <h1>hello2</h1>
            </div>
            <div class="remove_test">
                <button onClick = "GFG_Fun(test2)">remove</button>
                <button onClick = "for_new()">new</button>
            </div>
        </div>
    </div>
    <script>
         //   var div = document.getElementById('test2');
              
            function GFG_Fun() {
                var div = document.getElementById("test3");
                div.parentNode.removeChild(div);
            }
    </script>
    <div id="new">
        <p id="p1">Tutorix</p>
        <p id="p2">Tutorialspoint</p>
    </div>

    <script>
            function for_new() {
                const h2 = document.getElementById("test2");
                let html = "<div id='test3'><p class='box'>My new paragraph.</p><button onClick=GFG_Fun(test3)>jaaa<button></div>";
                h2.insertAdjacentHTML("afterend", html);
            }
    </script>
</body>
</html>
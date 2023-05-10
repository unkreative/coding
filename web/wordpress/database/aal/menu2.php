<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>menu</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
        <style type="text/css">

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
            
            .row {
                display: flex;
                margin: auto;
                width: 100%;
                border: 1px solid black;
                padding: 10px;
                height: 75%;
            }
            
            .column {
                flex: 70%;
            }

        </style>
    </head>
    <body>
        
    <div id="lundi" class="row">
            <div id="lundicolumn" class="column">
                <div class="box">
                    <p>Lundi</p>
                    <button onClick="remove_lundi('lundicolumn')">remove1</button>
                </div>
            </div>
        </div>
        <script>
            var num = 1;

            function remove_lundi(div_name) {
                var div = document.getElementById(div_name);
                div.parentNode.removeChild(div);

                const h2 = document.getElementById("lundi");
                let html = "<div class='column' id='new_btn'><button onClick=add_lundi()>new</button></div>";
                h2.insertAdjacentHTML("beforebegin", html);
            }
            function add_lundi(){
                var div = document.getElementById('new_btn');
                div.parentNode.removeChild(div);
                const h2 = document.getElementById("lundi");
  //              let html = "<div class='column' id='lundicolumn'><p class='box'>My new paragraph.</p><button onClick=remove_lundi()>remove lundi</button></div>";
                let html = "<div id='lundicolumn' class='column'><div class='box'><p>Lundi</p><button onClick='remove_lundi('lundicolumn')'>remove1</button></div>"
                let html2 = html.replace("'lundicolumn'", `"lundicolumn${num}"`);
                console.log(html2)

                num = num + 1;
                h2.insertAdjacentHTML("afterbegin", html2);

            }
        </script>

    </body>
</html>
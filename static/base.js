//document.getElementById("font").style.fontFamily = "Comic Sans MS",cursive,sans-serif;


var revealAns = function(){
    document.getElementById("pic").addEventListener("contextmenu", getAns);
}

var getAns = function(){
    var x = document.getElementById("ans");
    x.innerHTML = "yeah";
    x.style.fontSize = "30px";
}

revealAns()

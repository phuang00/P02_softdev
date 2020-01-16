//document.getElementById("font").style.fontFamily = "Comic Sans MS",cursive,sans-serif;


var revealAns = function(){
    document.getElementById("pic").addEventListener("contextmenu", getAns);
}

var getAns = function(){
    var x = document.getElementById("ans");
    x.innerHTML = "yeah";
    x.style.fontSize = "30px";
}

var addTeams = function(){
            var number = document.getElementById("teams").value;
            console.log(number);
            var container = document.getElementById("numteams");
            while (container.hasChildNodes()) {
                container.removeChild(container.lastChild);
            }
            var row = container.appendChild(document.createElement("div"));
            for (i = 0; i < number; i++){
                var label = container.appendChild(document.createElement("label"));
                label.innerHTML = "Team " + (i + 1);
                label.for = "team" + (i + 1);
                label.classList.add("col-auto");
                label.classList.add("col-form-label");
                var input = document.createElement("input");
                input.type = "text";
                input.name = "team" + (i + 1);
                container.appendChild(input);
                container.appendChild(document.createElement("br"));
                container.appendChild(document.createElement("br"));
            }
            var btn = container.appendChild(document.createElement("input"));
            btn.classList.add("btn");
            btn.classList.add("btn-outline-success");
            btn.type = "submit";
        }

var disable = function(id){
  var btn = document.getElementById(id);
  btn.disabled = true;
}

revealAns()

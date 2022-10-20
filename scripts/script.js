function Function() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
function myFunction(id) {
        document.getElementById(id).classList.toggle("show");
}
function close(x) {
  if (x.matches) { 
  	var dropdowns = document.getElementsByClassName("dropdown-content");
            var i;
            for (i = 0; i < dropdowns.length; i++) {
                    var openDropdown = dropdowns[i];
                            openDropdown.classList.remove('show');
            }
  } 
}
var x = window.matchMedia("(max-width: 600px)")
close(x)
x.addListener(close)
window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
                var dropdowns = document.getElementsByClassName("dropdown-content");
                var i;
                for (i = 0; i < dropdowns.length; i++) {
                        var openDropdown = dropdowns[i];
                        if (openDropdown.classList.contains('show')) {
                                openDropdown.classList.remove('show');
                        }
                }
        }
}
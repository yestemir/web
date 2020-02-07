var list = document.getElementsByTagName("li");
var i;
for(i = 0; i<list.length; i++){
	var span = document.createElement("span");
	var x = document.createTextNode("\u00D7");
	span.className = "close";
	span.appendChild(x);
	list[i].appendChild(span);
}

var close = document.getElementsByClassName("close");
var i;
for(i = 0; i<close.length; i++){
	close[i].onclick = function () {
		var div = this.parentElement;
		div.style.display = "none";
	}
}

var list = document.querySelector('ul');
list.addEventListener('click', function(ev){
	if(ev.target.tagName === 'LI'){
		ev.target.classList.toggle('checked');
	}
}, false);

function newElement(){
	var li = document.createElement("li");
	var inputValue = document.getElementById("input").value;
	var t = document.createTextNode(inputValue);
	li.appendChild(t);
	if (inputValue === '') {
  		alert("write something");
  	} else {
    	document.getElementById("myul").appendChild(li);
  	}
  	document.getElementById("input").value = "";
 	var span = document.createElement("span");
	var x = document.createTextNode("\u00D7");
	span.className = "close";
	span.appendChild(x);
  	li.appendChild(span);
  	for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
    }
  }
}
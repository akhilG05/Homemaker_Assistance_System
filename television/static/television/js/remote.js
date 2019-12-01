function buttonClickedremote(btn,remoteSlug) {
		var screenClass = document.getElementById("remote-typed");
		screenClass.innerHTML = btn;
		sendBtn(btn,remoteSlug)
}

function sendBtn(button,remoteSlug){
	  var jsondata = {
	    'button':button,
	    'remoteSlug':remoteSlug
	  }
	  $.ajax({
	    type: 'POST',
	    url: "http://localhost:8000/television/send-ir-code/",
	    data: jsondata,
	    dataType: "json",
	    });
}

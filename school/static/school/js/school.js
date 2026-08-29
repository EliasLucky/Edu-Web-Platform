function addUser() {
	var widget = document.getElementById("widget-add-user");
	widget.classList.toggle("hide");
	var darken = document.getElementById("darken");
	darken.classList.toggle("hide");
}

function showPassword(element) {
	var div = element.parentElement;
	var password = div.querySelector(".user-password");
	if (!password.innerHTML.indexOf("*")) {
		password.innerHTML = password.getAttribute("data-content");
	}
	else {
		password.innerHTML = "****";
	}
}

function viewUser(element) {
	var id = element.getAttribute("data-userid");
	
	var widget = document.getElementById(id)
	widget.classList.toggle("hide");
	var darken = document.getElementById("darken");
	darken.classList.toggle("hide");
}
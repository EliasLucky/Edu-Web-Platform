var expanded = false;

function showSidebar() {
	var sidebar = document.getElementById("sidebar");
	if (expanded == true) {
		sidebar.classList.remove("sidebar-slide-in");
		sidebar.classList.add("sidebar-slide-out");
	}
	else {
		sidebar.classList.remove("sidebar-slide-out");
		sidebar.classList.add("sidebar-slide-in");
	}
	expanded = !expanded;
}
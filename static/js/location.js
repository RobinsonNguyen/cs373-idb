locations = [
	{
		uri: 1,
		name: "Kanto",
		routes: ["Route 1", "Route 2"]
	},
	{
		uri: 2,
		name: "Jhoto",
		routes: ["Route 29", "Route 30"]
	}
]

routes = [
	{
		uri: 1,
		region: "Kanto",
		name: "Route 1",
		pokemon: ["Pidgey", "Rattata"]
	},
	{
		uri: 2,
		region: "Kanto",
		name: "Route 2",
		pokemon: ["Pidgey", "Zapdos"]
	}
]

function populateRoutes(uri, caller) {
	var locationButtons = document.getElementsByClassName("locationButton");
	for(var l = 0; l < locationButtons.length; l++)
		locationButtons[l].style.background = "white";

	caller.style.background = "#aaaaaa";

	var routeTable = document.getElementById("routeTable");
	console.log(routeTable.rows.length);

	for(var i = routeTable.rows.length-1; i > 0; i--) {
		routeTable.deleteRow(i);
	}

	for(var loc in locations) {
		if(locations[loc].uri == uri) {
			for(var route in locations[loc].routes) {
				var row = routeTable.insertRow();
				var name = row.insertCell(0);
					name.innerHTML = "<a href=\"#\">" + locations[loc].routes[route] + "</a>";
				var avgLvl = row.insertCell(1);
					avgLvl.innerHTML = 0;
					avgLvl.style = "text-align: center;";
				var numTrainers = row.insertCell(2);
					numTrainers.innerHTML = 0;
					numTrainers.style = "text-align: center;";
			}
		}
	}
}
locations = [
	{
		uri: 1,
		name: "Kanto",
		routes: ["Route 15"]
	},
	{
		uri: 2,
		name: "Johto",
		routes: ["Route 30", "Route 31"]
	}
]

routes = [
	{
		region: "Kanto",
		name: "Route 15",
		pokemon: ["Pidgey", "Rattata"],
		level: 15,
		trainers: 5,
		money: 300,
		pkmnAmnt: 6

	},
	{
		region: "Johto",
		name: "Route 32",
		pokemon: ["Pidgey", "Rattata"],
		level: 28,
		trainers: 3,
		money: 500,
		pkmnAmnt: 3
	},
	{
		region: "Johto",
		name: "Route 30",
		pokemon: ["Pidgey", "Zapdos"],
		level: 35,
		trainers: 6,
		money: 1200,
		pkmnAmnt: 7
	},
	{
		region: "Johto",
		name: "Route 31",
		pokemon: ["Pidgey", "Zapdos"],
		level: 20,
		trainers: 1,
		money: 300,
		pkmnAmnt: 9
	}
]

function populateRoutes(uri, caller) {
	var locationButtons = document.getElementsByClassName("locationButton");
	for(var l = 0; l < locationButtons.length; l++)
		locationButtons[l].style.background = "white";

	caller.style.background = "#aaaaaa";

	var routeTable = document.getElementById("routeTable");
	

	for(var i = routeTable.rows.length-1; i > 0; i--) {
		routeTable.deleteRow(i);
	}

	for(var loc in locations) {
		if(locations[loc].uri == uri) {
			for(var route in locations[loc].routes) {
				console.log(locations[loc].routes[route]);
				for(var r in routes) {
					if(routes[r].region == locations[loc].name && routes[r].name == locations[loc].routes[route]) {
						var row = routeTable.insertRow();
						var name = row.insertCell(0);
							name.innerHTML = "<a href=\"?region=" + routes[r].region + "&name=" + routes[r].name + "\">" + locations[loc].routes[route] + "</a>";
						var avgLvl = row.insertCell(1);
							avgLvl.innerHTML = routes[r].level;
							avgLvl.style = "text-align: center;";
						var numTrainers = row.insertCell(2);
							numTrainers.innerHTML = routes[r].trainers;
							numTrainers.style = "text-align: center;";
						var money = row.insertCell(3);
							money.innerHTML = routes[r].money;
							money.style = "text-align: center;";
						var pkmn = row.insertCell(4);
							pkmn.innerHTML = routes[r].pkmnAmt;
							pkmn.style = "text-align: center;";
					}
				}
			}
		}
	}
}
$(document).ready(function(){

	gameToRegion = { 'Red / Blue':'Kanto', 'Gold / Silver': 'Johto','HeartGold / SoulSilver': 'Johto', 'Ruby / Sapphire': 'Hoenn', 'FireRed / LeafGreen': 'Kanto', 'Diamond / Pearl': 'Sinnoh', 'Black / White': 'Unova', 'X / Y': 'Kalos', 'Red': 'Kanto', 'Blue': 'Kanto', 'Blue (Japan)': 'Kanto', 'Yellow': 'Kanto', 'Gold': 'Johto', 'Silver': 'Johto', 'Crystal': 'Johto', 'Ruby': 'Hoenn', 'Sapphire': 'Hoenn', 'Emerald': 'Hoenn', 'FireRed': 'Kanto', 'LeafGreen': 'Kanto', 'Diamond': 'Sinnoh', 'Pearl': 'Sinnoh', 'Platinum': 'Sinnoh', 'HeartGold':'Johto', 'SoulSilver': 'Johto', 'Black': 'Unova', 'White': 'Unova', 'Black 2': 'Unova', 'White 2': 'Unova', 'X': 'Kalos', 'Y': 'Kalos', 'Omega Ruby': 'Hoenn', 'Alpha Sapphire': 'Hoenn'};
	
	$('#pokemon-models').on('click-row.bs.table', function(row, e) {
		location.href = '/pokemon/' + e[1].trim();
	});

	$('#pokemon-moves').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

	$('#pokemon-routes').on('click-row.bs.table', function(row, e) {
		location.href = '/locations/' + e[0].trim();
	});

}); 
$(document).ready(function(){
	
	$('#route-models').on('click-row.bs.table', function(row, e) {
		location.href = '/location/' + e[0].trim();
	});

}); 

function lowestGen() {
	clearGen();
}

function clearGen() {
	var genI = document.getElementsByClassName("genIPokemon");
	for(i = 0; i < genI.length; i++)
		genI[i].style.display = "none";

	var genII = document.getElementsByClassName("genIIPokemon");
	for(i = 0; i < genII.length; i++)
		genII[i].style.display = "none";

	var genIII = document.getElementsByClassName("genIIIPokemon");
	for(i = 0; i < genIII.length; i++)
		genIII[i].style.display = "none";

	var genIV = document.getElementsByClassName("genIVPokemon");
	for(i = 0; i < genIV.length; i++)
		genIV[i].style.display = "none";

	var genV = document.getElementsByClassName("genVPokemon");
	for(i = 0; i < genV.length; i++)
		genV[i].style.display = "none";

	var genVI = document.getElementsByClassName("genVIPokemon");
	for(i = 0; i < genVI.length; i++)
		genVI[i].style.display = "none";

}

function genI() {
	clearGen();
	var genI = document.getElementsByClassName("genIPokemon");
	for(i = 0; i < genI.length; i++)
		genI[i].style.display = "table-row";
}

function genII() {
	clearGen();
	var genII = document.getElementsByClassName("genIIPokemon");
	for(i = 0; i < genII.length; i++)
		genII[i].style.display = "table-row";
}

function genIII() {
	clearGen();
	var genIII = document.getElementsByClassName("genIIIPokemon");
	for(i = 0; i < genIII.length; i++)
		genIII[i].style.display = "table-row";
}

function genIV() {
	clearGen();
	var genIV = document.getElementsByClassName("genIVPokemon");
	for(i = 0; i < genIV.length; i++)
		genIV[i].style.display = "table-row";
}

function genV() {
	clearGen();
	var genIV = document.getElementsByClassName("genVPokemon");
	for(i = 0; i < genV.length; i++)
		genV[i].style.display = "table-row";
}

function genIV() {
	clearGen();
	var genVI = document.getElementsByClassName("genVIPokemon");
	for(i = 0; i < genVI.length; i++)
		genIV[i].style.display = "table-row";
}
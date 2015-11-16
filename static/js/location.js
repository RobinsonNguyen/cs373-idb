$(document).ready(function(){
	
	$('#route-models').on('click-row.bs.table', function(row, e) {
		location.href = '/location/' + e[0].trim();
	});

}); 

function genI() {
	var genI = document.getElementsByClassName("genIPokemon");
	for(i = 0; i < genI.length; i++)
		genI[i].style.display = "block";

	var genII = document.getElementsByClassName("genIIPokemon");
	for(i = 0; i < genII.length; i++)
		genII[i].style.display = "none";
}

function genII() {
	var genI = document.getElementsByClassName("genIPokemon");
	for(i = 0; i < genI.length; i++)
		genI[i].style.display = "none";

	var genII = document.getElementsByClassName("genIIPokemon");
	for(i = 0; i < genII.length; i++)
		genII[i].style.display = "block";
}
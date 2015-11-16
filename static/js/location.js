$(document).ready(function(){
	
	$('#route-models').on('click-row.bs.table', function(row, e) {
		location.href = '/location/' + e[0].trim();
	});

}); 

function genI() {
	var genI = document.getElementById("genIPokemon");
	genI.style.display = "block";

	var genII = document.getElementById("genIIPokemon");
	genII.style.display = "none";
}

function genII() {
	var genI = document.getElementById("genIPokemon");
	genI.style.display = "none";

	var genII = document.getElementById("genIIPokemon");
	genII.style.display = "block";
}
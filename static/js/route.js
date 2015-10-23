$(document).ready(function(){
	
	$('#pokemon-models').on('click-row.bs.table', function(row, e) {
		location.href = '/pokemon/' + e[1].trim();
	});

	$('#item-models').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

}); 
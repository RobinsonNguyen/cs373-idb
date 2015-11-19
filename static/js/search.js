$(document).ready(function(){

	$('#pokemon-models').on('click-row.bs.table', function(row, e) {
		location.href = '/pokemon/' + e[0].trim();
	});

	$('#moves-models').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

	$('#routes-models').on('click-row.bs.table', function(row, e) {
		location.href = '/locations/' + e[0].trim();
	});

}); 
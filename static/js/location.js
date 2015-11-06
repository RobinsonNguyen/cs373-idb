$(document).ready(function(){
	
	$('#route-models').on('click-row.bs.table', function(row, e) {
		location.href = '/locaiton/' + e[0].trim();
	});

}); 
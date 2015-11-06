$(document).ready(function(){
	
	$('#route-models').on('click-row.bs.table', function(row, e) {
		location.href = '/locaiton/?region=' + e[1].trim() + '&name=' + e[0].trim();
	});

}); 
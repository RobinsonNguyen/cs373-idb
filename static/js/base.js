$(document).ready(function() {

	$( "#search" ).keypress(function(e) {
		console.log(e);
		if(e.which == 13) {
			term = $(this).val();
			location = '/search/' + encodeURIComponent(term);
	    }
	});

}); 

$(document).ready(function(){
	
	$('#route-models').on('click-row.bs.table', function(row, e) {
		location.href = '/location/' + e[0].trim();
	});

}); 

$(document).ready(function(){
	
	$('#route-pokemon-models').on('click-row.bs.table', function(row, e) {
		location.href = '/pokemon/' + e[1].trim();
	});

}); 
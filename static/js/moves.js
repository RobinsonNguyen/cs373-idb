$(document).ready(function(){
	
	$('#move-models').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

	$('.stats-header').click(function(e){
	    $(e.target).siblings('.stats-data').slideToggle('slow');
	});

}); 
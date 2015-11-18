$(document).ready(function(){
	
	$('#move-models').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

	$('.stats-header').click(function(e){
	    $(this).children('p').slideToggle('slow');
	});

}); 
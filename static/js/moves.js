$(document).ready(function(){
	
	$('#move-models').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

	$('.stats').click(function(){
	    $(this).find('.data').slideToggle('slow');
	});

}); 
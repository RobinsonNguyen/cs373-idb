$(document).ready(function(){
	
	$('#move-models').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

	$('.test1').click(function(e){
	    $(e.target).find('.test2').slideToggle('slow');
	});

}); 
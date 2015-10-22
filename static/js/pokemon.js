$(document).ready(function(){
	
	$('#pokemon-models').on('click-row.bs.table', function(row, e) {
		location.href = '/pokemon/' + e[1].trim();
	});

	$('.move-row').click(function() {
		moveName = $(this).find('.move-name').html().trim();
		location.href = '/move/' + moveName;
	})

}); 
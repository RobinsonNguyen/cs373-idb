$(document).ready(function(){
	
	$('#move-models').on('click-row.bs.table', function(row, e) {
		location.href = '/moves/' + e[0].trim();
	});

	$('.stats').click(function(caller){
	    $(this).children('p').slideToggle('slow');
	});

}); 

function collapse(caller) {
	console.log("test");
	caller.style.height = "500px";
}
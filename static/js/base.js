$(document).ready(function() {

	$( "#search" ).keypress(function(e) {
		console.log(e);
		if(e.which == 13) {
			term = $(this).value;
	        alert(term);
	    }
	});

}); 
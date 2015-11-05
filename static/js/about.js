$(document).ready(function (){
  console.log('ready');

  $('#do-unit-tests').click(function() {

    $.ajax({
      url: 'api/v1.0/tests'
    }).success(function(result) {
      console.log(result);
        $('#unit-test-results').text(result['results']);
    });

    $('.unit-test-output').show();
  });

});
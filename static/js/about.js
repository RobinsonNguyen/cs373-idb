$(document).ready(function (){
  console.log('ready');

  $('#do-unit-tests').click(function() {
    $.ajax({
      url: '/api/v1.0/tests/'
    }).success(function(result) {
      console.log(result['results']);
      $('#unit-test-results').text(result['results']);
      $('#unit-test-results').css('white-space', 'pre-wrap');
    });

    $('.unit-test-output').show();
  });

});
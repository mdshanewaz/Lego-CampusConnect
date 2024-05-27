$(document).ready(function() {
  $('input[name=advSearchOption]:radio').change(function(e) {
    let value = e.target.value.trim()

    $('[class^="form"]').css('display', 'none');
    
    switch (value) {
      case 'date_range':
        $('.form-a').show()
        break;
      case 'order_id':
        $('.form-b').show()
        break;
      case 'serv_title':
        $('.form-c').show()
        break;
      default:
        break;
    }
  });

// 
  $("#date_range_556").click(function(){
      // $("#ggKShh76").css("display","block");
      $("#ggKShh76").show();
  });

})


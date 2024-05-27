$(function(){
   	
   	'use strict';

     // scroll to top
    $("#toTop").scrollToTop();

     // smooth scroll
    $("a").on('click', function(event) {

      if (this.hash !== "") {
        event.preventDefault();

        var hash = this.hash;

        $('html, body').animate({

          scrollTop: $(hash).offset().top

        }, 850, function(){

          window.location.hash = hash;

        });

      }

    });

    // loader
    $('#fakeLoader').fakeLoader({
      
      zIndex: 999,
      spinner: "spinner5",
      bgColor: "#9575cd"

    });

    // NAVBAR COLLAPSE HIDE ON CLICK
    $('.nav a').click(function(){
        $('.navbar-collapse').collapse('hide');
    });
    
});
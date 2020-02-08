$('.gallery ul li a').mouseover(function() {
     var alt = $(this).attr('data-title');
     $('#message').text(alt);
     return false;
 });


const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//Fade out timer for messages
setTimeout(function () {
    $('#message').fadeOut('slow')
}, 3000);

//Show uploaded file path
$(".custom-file-input").on("change", function() {
  var fileName = $(this).val().split("\\").pop();
  $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

//Carousel functionality
$(document).ready(function () {
    $('#mycarousel').carousel({ interval: 2000 });
    $('#carouselButton').click(function () {
        if ($('#carouselButton').children('span').hasClass('fa-pause')) {
            $('#mycarousel').carousel('pause');
            $('#carouselButton').children('span').removeClass('fa-pause');
            $('#carouselButton').children('span').addClass('fa-play');
        }
        else {
            $('#mycarousel').carousel('cycle');
            $('#carouselButton').children('span').removeClass('fa-play');
            $('#carouselButton').children('span').addClass('fa-pause');
        }
    });
});

$(document).ready(function () {
    $('#mycarousel1').carousel({ interval: 2000 });
    $('#carouselButton1').click(function () {
        if ($('#carouselButton1').children('span').hasClass('fa-pause')) {
            $('#mycarousel1').carousel('pause');
            $('#carouselButton1').children('span').removeClass('fa-pause');
            $('#carouselButton1').children('span').addClass('fa-play');
        }
        else {
            $('#mycarousel1').carousel('cycle');
            $('#carouselButton1').children('span').removeClass('fa-play');
            $('#carouselButton1').children('span').addClass('fa-pause');
        }
    });
});

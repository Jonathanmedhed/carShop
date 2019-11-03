const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//Fade out timer for messages
setTimeout(function () {
    $('#message').fadeOut('slow')
}, 3000);

//Show uploaded file path
$(".custom-file-input").on("change", function () {
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

//Show choices depending on type in a form
$('#type').on('change', function () {
    var selected = $(this).val();
    $("#choices option").each(function (item) {
        var element = $(this);
        if (element.data("tag") != selected) {
            element.hide();
        } else {
            element.show();
        }
    });
    $("#choices input").each(function (item) {
        var element = $(this);
        if (element.data("tag") != selected) {
            element.hide();
        } else {
            element.show();
        }
    });
    $("#choices select").each(function (item) {
        var element = $(this);
        if (element.data("tag") != selected) {
            element.hide();
        } else {
            element.show();
        }
    });
});

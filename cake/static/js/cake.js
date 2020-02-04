$(function () {

    $(window).on('load', function () {
        $('.loader').delay(500).fadeOut('slow', function () {
            $(this).attr('style', 'display: none !important');
        });
    });

    $('.cake-img-h60').mouseenter(function (e) {
        $(this).find("img").click();
    });

    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.scroll-to-top').fadeIn();
        } else {
            $('.scroll-to-top').fadeOut();
        }
    });

    $('.scroll-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 300);
        return false;
    });

});
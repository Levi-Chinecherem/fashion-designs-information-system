// static/js/main.js
$(document).ready(function () {
    $('.menu-icon').click(function () {
        $('.nav-links').toggleClass('active');
        $('.menu-icon .bar').toggleClass('animate');
    });
});

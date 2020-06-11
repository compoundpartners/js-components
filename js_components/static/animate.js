$.fn.isInViewport = function () {
    let elementTop = $(this).offset().top;
    let elementBottom = elementTop + $(this).outerHeight();

    let viewportTop = $(window).scrollTop();
    let viewportBottom = viewportTop + $(window).height();

    return elementBottom > viewportTop && elementTop < viewportBottom;
};
animateCSS = function (element, animation, prefix = 'animate__'){
  if (element.isInViewport()) {
    element.addClass(prefix + 'animated');
    element.addClass(prefix + animation);
  }
  $(window).on('scroll', function(e) {
    if (element.isInViewport()) {
      element.addClass(prefix + 'animated');
      element.addClass(prefix + animation);
    }
  });
};

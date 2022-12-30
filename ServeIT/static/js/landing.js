const services = document.querySelectorAll('.service');

// handle the scroll event
window.addEventListener('scroll', function() {
  // check if the user has scrolled to a service
  services.forEach(service => {
    if (window.scrollY >= service.offsetTop && window.scrollY < service.offsetTop + service.offsetHeight) {
      // update the scrollTop property to scroll to the selected service
      document.body.scrollTop = service.offsetTop;
    }
  });
});
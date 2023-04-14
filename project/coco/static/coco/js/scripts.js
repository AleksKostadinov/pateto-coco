window.onscroll = function() {myFunction()};
var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;
var logo = document.querySelector(".logo");

logo.classList.add("hidden");

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
    logo.classList.remove("hidden");
  } else {
    navbar.classList.remove("sticky");
    logo.classList.add("hidden");
  }

  // check if the user has scrolled to the top of the page
  if (window.pageYOffset === 0) {
    navbar.classList.remove("sticky");
    logo.classList.add("hidden");
  }
}

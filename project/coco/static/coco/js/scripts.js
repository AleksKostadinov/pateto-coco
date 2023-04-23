// creating a sticky navbar
window.onscroll = function () {
    myFunction()
};
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

// subscribe to newsletter
const form = document.getElementById('contactForm');
form.addEventListener('submit', (event) => {
    event.preventDefault(); // prevent the form from submitting normally
    const formData = new FormData(form); // create a FormData object from the form
    fetch('/', { // replace '/' with the URL of your form submission endpoint
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Thank you for subscribing!');
            } else {
                alert('Please enter a valid email!');
            }
        })
        .catch(error => {
            console.error(error);
            alert('An error occurred. Please try again later.');
        });
});

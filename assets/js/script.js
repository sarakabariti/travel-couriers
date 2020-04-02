var signupform = document.getElementById("signup-form");
var loginform = document.getElementById("login-form");

function signupfunction(){
    signupform.style.display = "block";
    loginform.style.display = "none";
}

function loginfunction(){
    loginform.style.display = "block";
    signupform.style.display = "none";
}



//Code for Humburger menu
let mainNav = document.getElementById("js-menu");
let navBarToggle = document.getElementById("js-navbar-toggle");

navBarToggle.addEventListener("click", function() {
  mainNav.classList.toggle("active");
});


//Prevent default form submission event
document.getElementById("submit").addEventListener("click", function(event){
    event.preventDefault()
  });
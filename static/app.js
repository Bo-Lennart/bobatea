const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav_menu");

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle("active")
    navMenu.classList.toggle("active")
})

document.querySelectorAll('.nav-link').forEach( n=> n.
    addEventListener('click', () => {
        hamburger.classList.remove("active");
        navMenu.classList.remove("active");
    }))


function deleteReservation() {
    alert("Reservation has been deleted");
}



$(document).ready(function() {
          
    $(function() {
        $( "#id_date" ).datepicker();
    });
})
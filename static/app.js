const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav_menu");

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1;
var yyyy = today.getFullYear();
var todaysDate = new Date().getDate


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

if(dd<10){
    dd='0'+dd
} 
if(mm<10){
    mm='0'+mm
} 

today = yyyy+'-'+mm+'-'+dd;

document.getElementById("id_date").setAttribute("min", today, "max", 'nextWeek');



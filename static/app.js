const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav_menu");

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1;
var yyyy = today.getFullYear();
var todaysDate = new Date().getDate

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle("active")
    navMenu.classList.toggle("active")
})

document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}))


function deleteCancelationAlert() {
    alert("Cancelation request has been deleted");
}

function deleteReservationAlert() {
    alert("Reservation has been deleted");
}

function deleteItemMenuAlert() {
    alert("Menu item has been deleted");
}

function itemEditedAlert() {
    alert("Menu has been updated");
}

function reservationEditedAlert() {
    alert("Reservation has been updated");
}

today = yyyy + '-' + mm + '-' + dd;


if (dd < 10) {
    dd = '0' + dd
}
if (mm < 10) {
    mm = '0' + mm
}

var calendarElement = document.getElementById("id_date")

if (calendarElement !== null) {
    calendarElement.setAttribute("min", today, "max", 'nextWeek');
}
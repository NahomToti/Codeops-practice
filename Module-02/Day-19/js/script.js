let cart = document.createElement("strong");
cart.textContent="cart"
let newdiv = document.createElement("div")
newdiv.appendChild(cart)
document.getElementById("nav-bar").appendChild (newdiv)
newdiv.classList.add("blue")
logo.addEventListener("click", () => {alert("logo was clicked")})
cart.addEventListener("click", () => {alert("cart was clicked")})

let form = document.getElementById("form")

form.addEventListener("submit", function (event) {

    event.preventDefault();

    console.log("FORM SUBMITTED!");

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    console.log("Email:", email);
    console.log("Password:", password);
});
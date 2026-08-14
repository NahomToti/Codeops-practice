setTimeout(()=>{})
    0



    const data=fetch("http://127.0.0.1:5500/Module-02/Day-20/htt");
    console.log(data)
    

    let logo = document.getElementById("logo");
let body = document.body;

let theme = sessionStorage.getItem("theme") || "light";

body.classList.add(theme);

function changetheme() {
    if (body.classList.contains("light")) {
        body.classList.remove("light");
        body.classList.add("dark");
        theme = "dark";
    } else {
        body.classList.remove("dark");
        body.classList.add("light");
        theme = "light";
    }

    sessionStorage.setItem("theme", theme);
}

logo.addEventListener("click", changetheme);

let pattern = /^(?:\+251|0)?[97]\d{8}$/;



console.log(pattern.test("+251902391319"))
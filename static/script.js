const form = document.querySelector("form");

form.addEventListener("submit", function(event) {

    const username = document.querySelector(
        'input[name="username"]'
    ).value;

    const password = document.querySelector(
        'input[name="password"]'
    ).value;

    if (username === "" || password === "") {

        alert("Please enter username and password");

        event.preventDefault();
    }

});
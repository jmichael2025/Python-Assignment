
/*const USERNAME = "admin";
const PASSWORD = "admin";

function autoLogin() {
    const username = "admin";
    const password = "admin";

    if (username === USERNAME && password === PASSWORD) {
        
        localStorage.setItem("isLoggedIn", "true");

       
        window.location.href = "dashboard.html";
    } else {
        document.getElementById("message").innerText = "Login failed. Please try again.";
    }
}

window.onload = function () {
    autoLogin();
};

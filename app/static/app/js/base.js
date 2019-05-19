window.onload = () => {
    let loginButton = document.getElementsByClassName("signup-btn")[0];
    loginButton.onclick = () => {
        document.getElementsByClassName("popup")[0].classList.toggle("visible");
    }
}

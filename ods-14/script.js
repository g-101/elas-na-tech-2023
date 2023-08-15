const navbar = document.querySelector(".navbar");
document.addEventListener("scroll", () =>{
    if (window.scrollY > 100) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
})


const menuButton = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
menuButton.addEventListener("click", () => {
    navLinks.classList.toggle("mobile-menu")
})

function toggleMenu() {
    if (navLinks.classList.contains("mobile-menu")) {
        navLinks.classList.remove("mobile-menu");
    } else {
        navLinks.classList.add("mobile-menu");
    }
}
const menuItems = document.querySelectorAll(".menuItem");
menuItems.forEach( 
    function(menuItem) { 
    menuItem.addEventListener("click", toggleMenu);
    }
)


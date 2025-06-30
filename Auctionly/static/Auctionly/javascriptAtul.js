// -----------------by atul -----------------------------------


let arnav_login = document.querySelector("#main-nav-bar-login");
let modal_body_container = document.querySelector(".modal-body-container");
let search_search_closeBtn = document.querySelector("#search p");
let search_icon_navbar = document.querySelector(".search-icon-navbar");
let main_page_menu_btn = document.querySelector(".main-nav-menu");
let inside_menu = document.querySelector(".inside_menu");
let inside_menu_navbar_close = document.querySelector(".inside_menu_navbar_close");
let login_content_heading1 = document.querySelector(".login_content_heading1");
let login_content_heading2 = document.querySelector(".login_content_heading2");
let signup_box = document.querySelector(".signup_box");
let login_main_box_inner = document.querySelector(".login_main_box");
let login_content = document.querySelector(".login_content");
let createAcc_box = document.querySelector(".createAcc_box");

// fixed pos of menu bar
window.onscroll = function() {scrollNavBar()};

function scrollNavBar() {
    const mainPgNavBar = document.querySelector("#main-nav-bar");
    const mainPgNavBarLogo = document.querySelector(".main-nav-bar-logo")

    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80 ){
        mainPgNavBar.style.backgroundColor = "white";
        mainPgNavBar.style.boxShadow = "0 4px 5px rgba(0, 0, 0, 0.1)";
        mainPgNavBarLogo.style.backgroundColor = "rgb(0, 0, 0, 0.6)";
    } else {
        mainPgNavBar.style.backgroundColor = "transparent";
        mainPgNavBarLogo.style.backgroundColor = "";
        mainPgNavBar.style.boxShadow = "";
    }
}




main_page_menu_btn.addEventListener("click", () => {
    console.log("clicked");
    inside_menu.classList.add("popUPOfInsideMenu");
})

inside_menu_navbar_close.addEventListener("click", () => {
    console.log("clicked");
    inside_menu.classList.remove("popUPOfInsideMenu");
})

search_icon_navbar.addEventListener("click", () => {
    console.log("clicked");
    modal_body_container.classList.add("popUPOfSearch");
})

search_search_closeBtn.addEventListener("click", () => {
    console.log("clicked");
    modal_body_container.classList.remove("popUPOfSearch");
})





// ______________________________________________slides A.K_________________________________________




//  selecting images of slides
let slideImages = document.querySelectorAll(".slide_container .slides img");
let slideNextBtn = document.getElementById("next_btn");
let span = document.querySelectorAll(".slides_content span");
let slides_border = document.querySelectorAll(".slides_border div");

var counter = 0;

slideNextBtn.addEventListener("click",slideNext);

function slideNext() {
    slideImages[counter].style.animation = "outgoing 0.5s ease-in forwards";
    slides_border[counter].style.animation = "outgoing 0.5s ease-in forwards";
    span[counter].style.animation = "outgoing 0.5s ease-in forwards";
    if (counter >= slideImages.length-1){
        counter = 0;
    }
    else{
        counter++ ;
    }
    slideImages[counter].style.animation = "incoming 0.5s ease-in forwards";
    span[counter].style.animation = "incoming 0.5s ease-in forwards";
    slides_border[counter].style.animation = "incoming 0.5s ease-in forwards";
}




function autoPlay() {
    delInterval = setInterval(timer, 4000);
    function timer() {
        slideNext();
    }
}

autoPlay();

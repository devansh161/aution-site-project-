

let arnav_login = document.querySelector("#main-nav-bar-login");
let login_main_box = document.querySelector(".atul_login_box");
let login_main_box_closeBtn = document.querySelector("#login_close");
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


arnav_login.addEventListener("click", () => {
    login_main_box.classList.add("popUPOfLoginBox");
    signup_box.classList.add("popUPOfsignUpBox");
    login_content_heading2.id =  "login_content_heading_formatting";

})

login_content_heading1.addEventListener("click",() => {
    login_content_heading2.id =  "";
    signup_box.classList.remove("popUPOfsignUpBox");
    login_main_box_inner.classList.add("adjust_login_main_box");
    login_content.classList.add("adjust_login_content_createAcc");
    createAcc_box.classList.add("popUPOfcreateAcc");
    login_content_heading1.id = "login_content_heading_formatting";
})

login_content_heading2.addEventListener("click",() => {
    login_content_heading1.id =  "";
    signup_box.classList.add("popUPOfsignUpBox");
    login_main_box_inner.classList.remove("adjust_login_main_box");
    login_content.classList.remove("adjust_login_content_createAcc");
    createAcc_box.classList.remove("popUPOfcreateAcc");
    login_content_heading2.id = "login_content_heading_formatting";
})

login_main_box_closeBtn.addEventListener("click", () => {
    login_content_heading1.id =  "";
    login_content_heading2.id =  "";
    login_main_box_inner.classList.remove("adjust_login_main_box");
    signup_box.classList.remove("popUPOfsignUpBox");
    createAcc_box.classList.remove("popUPOfcreateAcc");
    login_content.classList.remove("adjust_login_content_createAcc");
    login_main_box.classList.remove("popUPOfLoginBox");
})
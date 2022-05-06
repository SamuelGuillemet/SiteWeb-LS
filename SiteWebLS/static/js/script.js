//Breadcrumbs for the page
const start = '<svg width="15" height="30" viewBox="0 0 15 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 10C0 4.47715 4.47715 0 10 0H30V30H10C4.47715 30 0 25.5228 0 20V10Z" fill=currentColor /></svg>';
const right = '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 0V30H1H22C23.6569 30 25 28.6569 25 27C25 25.3431 23.6569 24 22 24H16C14.3431 24 13 22.6569 13 21C13 19.3431 14.3431 18 16 18H27C28.6569 18 30 16.6569 30 15C30 13.3431 28.6569 12 27 12H9C7.34315 12 6 10.6569 6 9C6 7.34315 7.34315 6 9 6H14C15.6569 6 17 4.65685 17 3C17 1.34315 15.6569 0 14 0H1H0Z" fill=currentColor /></svg>';
const left = '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" clip-rule="evenodd" d="M30 0L27.9972 0L27 0L8.00003 0C9.65689 0 11 1.34315 11 3C11 4.65685 9.65689 6 8.00003 6H3C1.34314 6 0 7.34315 0 9C0 10.6569 1.34314 12 3 12H21C22.6569 12 24 13.3431 24 15C24 16.6569 22.6569 18 21 18H10C8.34314 18 7 19.3431 7 21C7 22.6569 8.34314 24 10 24H16C17.6569 24 19 25.3431 19 27C19 28.6569 17.6569 30 16 30H27H28H30V0Z" fill=currentColor /></svg>';

if (document.getElementById("breadcrumbs") != null) {
    var breadcrumbsitems = document.getElementById("breadcrumbs").children[0];
    for (let index = 0; index < breadcrumbsitems.childElementCount; index++) {
        if (index == 0) {
            breadcrumbsitems.children[index].children[0].children[0].innerHTML = start;
            breadcrumbsitems.children[index].children[0].children[2].innerHTML = right;
        } else {
            breadcrumbsitems.children[index].children[0].children[0].innerHTML = left;
        }
        if (index == breadcrumbsitems.childElementCount - 1) {
            breadcrumbsitems.children[index].children[0].children[2].innerHTML = start;
        } else {
            breadcrumbsitems.children[index].children[0].children[2].innerHTML = right;
        }
    }
    var scale = (document.children[0].clientWidth - 32) * 0.94 / breadcrumbsitems.clientWidth;
    if (scale >= 1) {
        scale = 1
    }

    document.getElementById("breadcrumbs").style.setProperty('--scale', scale);

    window.addEventListener('resize', () => {
        var scale = (document.children[0].clientWidth - 32) * 0.94 / breadcrumbsitems.clientWidth;
        if (scale >= 1) {
            scale = 1
        }
        document.getElementById("breadcrumbs").style.setProperty('--scale', scale);
    });
}


//Hamburger menu
const hamburger = document.querySelector("#hamburger-menu");
const navitems = document.querySelector("#nav-items");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navitems.classList.toggle("active");
});

// Active class for the nav items

var menuItems = document.querySelectorAll(".menu-items");
var currentUrl = new URL(window.location.href);

for (let index = 0; index < menuItems[0].childElementCount; index++) {
    if ((new URL(menuItems[0].children[index].children[0].href)).pathname.split('/')[1] == currentUrl.pathname.split('/')[1]) {
        menuItems[0].children[index].classList.add("active");
        menuItems[1].children[index].classList.add("active");
    }
}


//Carousel

var arrowRight = document.getElementById("carousel-arrow-right");
var arrowLeft = document.getElementById("carousel-arrow-left");
var carousel = document.getElementById("carousel");

if (carousel != null) {
    const idMax = carousel.children[0].childElementCount - 1;
    var id = 0;

    for (let index = 0; index <= idMax; index++) {
        carousel.children[0].children[index].children[0].addEventListener("click", () => {
            shouldRun = !shouldRun;
        });
    }

    var shouldRun = true;

    arrowRight.addEventListener("click", arrowRightHandler, true);
    arrowLeft.addEventListener("click", arrowLeftHandler);

    function arrowRightHandler(arrow) {
        if (arrow === undefined) {
            arrow = false;
        }
        if (shouldRun || arrow) {
            shouldRun = true;
            carousel.children[0].children[id].classList.remove("active");
            carousel.children[0].children[NextID(id)].classList.add("active");
            carousel.children[0].children[NextID(id)].classList.remove("next");
            carousel.children[0].children[NextID(NextID(id))].classList.add("next");
            id = NextID(id);
        }
    }

    function arrowLeftHandler() {
        carousel.children[0].children[id].classList.remove("active");
        carousel.children[0].children[PrevID(id)].classList.add("active");
        carousel.children[0].children[NextID(id)].classList.remove("next");
        carousel.children[0].children[id].classList.add("next");
        id = PrevID(id);
    }

    function NextID(id) {
        if (id == idMax) {
            return 0;
        } else {
            return id + 1;
        }
    }

    function PrevID(id) {
        if (id == 0) {
            return idMax;
        } else {
            return id - 1;
        }
    }

    setInterval(arrowRightHandler, 7500);
}

var shelfIcons = document.querySelectorAll(".shelf-icon");

for (let index = 0; index < shelfIcons.length; index++) {
    shelfIcons[index].addEventListener("click", () => {
        location.href = '#' + shelfIcons[index].classList[0];
    });
}

let pages = document.getElementsByClassName('page')
let book = document.getElementsByClassName('book')[0]
function bookMove(drect) {
    if (innerWidth > 768) {
        if (drect === 'right') {
            book.style.transform = 'translate(50%,0)'
        } else if (drect === 'left') {
            book.style.transform = 'translate(0,0)'
        }
    } else {
        if (drect === 'right') {
            book.style.height = '50%';
        } else if (drect === 'left') {
            book.style.height = '100%'
        }
    }
}
for (let i = 0; i < pages.length; i++) {
    pages[i].addEventListener('click', () => handlepagedown(pages[i], i, pages), false);
}

function handlepagedown(page, i, pages, params) {
    if (page.classList.contains('flipped')) {
        page.classList.remove('flipped')
        page.classList.add('active')
        if (i === 0) {
            bookMove('left')
        }
        if (page.nextElementSibling !== null) {
            page.nextElementSibling.classList.remove('active')
        } else {
            bookMove('right')
        }
    } else if (i != pages.length - 1) {
        page.classList.add('flipped')
        page.classList.remove('active')
        if (i === 0) {
            bookMove('right')
        }
        if (page.nextElementSibling !== null) {
            page.nextElementSibling.classList.add('active')
        }
    }
}


var MainContent = document.getElementById("MainContent");
var footer = document.getElementById("footer-page");

MainContent.style.minHeight = "calc(100vh - 64px - " + footer.clientHeight + "px)";
window.addEventListener('resize', () => {
    MainContent.style.minHeight = "calc(100vh - 64px - " + footer.clientHeight + "px)";
});

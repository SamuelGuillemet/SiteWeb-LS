//Breadcrumbs for the page
const start = '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 10C0 4.47715 4.47715 0 10 0H30V30H10C4.47715 30 0 25.5228 0 20V10Z" fill=currentColor /></svg>';
const right = '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 0V30H1H22C23.6569 30 25 28.6569 25 27C25 25.3431 23.6569 24 22 24H16C14.3431 24 13 22.6569 13 21C13 19.3431 14.3431 18 16 18H27C28.6569 18 30 16.6569 30 15C30 13.3431 28.6569 12 27 12H9C7.34315 12 6 10.6569 6 9C6 7.34315 7.34315 6 9 6H14C15.6569 6 17 4.65685 17 3C17 1.34315 15.6569 0 14 0H1H0Z" fill=currentColor /></svg>';
const left = '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path fill-rule="evenodd" clip-rule="evenodd" d="M30 0L27.9972 0L27 0L8.00003 0C9.65689 0 11 1.34315 11 3C11 4.65685 9.65689 6 8.00003 6H3C1.34314 6 0 7.34315 0 9C0 10.6569 1.34314 12 3 12H21C22.6569 12 24 13.3431 24 15C24 16.6569 22.6569 18 21 18H10C8.34314 18 7 19.3431 7 21C7 22.6569 8.34314 24 10 24H16C17.6569 24 19 25.3431 19 27C19 28.6569 17.6569 30 16 30H27H28H30V0Z" fill=currentColor /></svg>';

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

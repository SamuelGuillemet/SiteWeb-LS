var currentUrl = new URL(window.location.href)
let choice = document.querySelectorAll(".choice");
let choicePubli = document.querySelectorAll(".choice-publi");

for (let index = 0; index < choice.length; index++) {
    const para = choice[index].children[0].id;
    choice[index].children[0].checked = currentUrl.searchParams.has(para);
    choice[index].children[0].addEventListener("click", () => {
        if (choice[index].children[0].checked) {
            if (!currentUrl.searchParams.has(para)) {
                currentUrl.searchParams.append(para, 'True');
                console.log('Added : ' + para);
            }
        } else {
            if (currentUrl.searchParams.has(para)) {
                currentUrl.searchParams.delete(para);
                console.log('Delete : ' + para);
            }
        }
        window.location.href = currentUrl;
    });
}


if (choicePubli) {
    for (let index = 0; index < choicePubli.length; index++) {
        const para = choicePubli[index].children[0].name;
        const name = choicePubli[index].children[0].id
        choicePubli[index].children[0].checked = currentUrl.searchParams.get(para) == name;
        choicePubli[index].children[0].addEventListener("click", () => {
            if (choicePubli[index].children[0].checked) {
                currentUrl.searchParams.set(para, name);
                console.log('Added : ' + name);
            } else {
                currentUrl.searchParams.delete(para);
                console.log('Delete : ' + name);
            }
            window.location.href = currentUrl;
        });
    }
}
const resetfilter = document.querySelector(".reset-filter");

if (resetfilter) {
    resetfilter.addEventListener("click", () => {
        window.location.href = currentUrl.pathname;
    });
}



var choiceBtn = document.querySelectorAll(".choice-btn");
var choicePubliBtn = document.querySelectorAll(".choice-publi-btn");

for (let index = 0; index < choiceBtn.length; index++) {
    choiceBtn[index].addEventListener("click", () => {
        const para = choiceBtn[index].name;
        if (currentUrl.pathname.split('/').length > 3 || currentUrl.pathname.split('/')[1] != 'article') {
            currentUrl.pathname = "/article/";
            currentUrl.searchParams.delete('q');
        }
        if (!currentUrl.searchParams.has(para)) {
            currentUrl.searchParams.append(para, 'True');
            window.location.href = currentUrl;
        }
    });
}

for (let index = 0; index < choicePubliBtn.length; index++) {
    choicePubliBtn[index].addEventListener("click", () => {
        const para = choicePubliBtn[index].name;
        if (currentUrl.pathname.split('/').length > 3 || currentUrl.pathname.split('/')[1] != 'article') {
            currentUrl.pathname = "/article/";
            currentUrl.searchParams.delete('q');
        }
        if (!currentUrl.searchParams.has('publication')) {
            currentUrl.searchParams.set('publication', para);
            window.location.href = currentUrl;
        }
    });
}
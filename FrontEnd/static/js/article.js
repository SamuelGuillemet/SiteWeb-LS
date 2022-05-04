var currentUrl = new URL(window.location.href)
var choice = document.querySelectorAll(".choice");
var choicePubli = document.querySelectorAll(".choice-publi");

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
var checked = false;
for (let index = 0; index < choicePubli.length; index++) {
    const para = choicePubli[index].children[0].id;
    const name = choicePubli[index].children[0].name
    choicePubli[index].children[0].checked = currentUrl.searchParams.get(para) == name;
    checked = checked || choicePubli[index].children[0].checked;

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

if (checked) {
    for (let index = 0; index < choicePubli.length; index++) {
        //choicePubli[index].children[0].disabled = (true && !choicePubli[index].children[0].checked);
    }
}

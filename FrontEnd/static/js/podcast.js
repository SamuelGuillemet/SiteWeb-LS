let SliderTrackInput = document.querySelector('.slider-track-input');
let SliderCounterCurrent = document.querySelector('.slider-counter-current');
let SliderCounterMax = document.querySelector('.slider-counter-max');
let SliderTrackActive = document.querySelector('.slider-track-active');
let SliderAudio = document.querySelector('.slider-audio');

var max;

const url = new URL(window.location.href);
const params = url.searchParams;

SliderTrackInput.addEventListener('input', () => audioSlider());
SliderAudio.addEventListener('timeupdate', () => audioPlay());


function valueToTime(params) {
    let minute = Math.floor(params / 60).toString();
    if (minute.length == 1) {
        minute = "0" + minute;
    }
    let second = Math.floor(params % 60).toString();
    if (second.length == 1) {
        second = "0" + second;
    }
    return minute + " : " + second;
}

function audioSlider() {
    SliderTrackInput.setAttribute("value", SliderTrackInput.value);
    SliderAudio.currentTime = SliderTrackInput.value;
    changeValue();
}

function changeValue() {
    SliderCounterCurrent.innerHTML = valueToTime(SliderTrackInput.value);
    SliderTrackActive.style.width = SliderTrackInput.value * 100 / max + "%";
}


function audioPlay() {
    SliderTrackInput.value = SliderAudio.currentTime;
    SliderTrackInput.setAttribute("value", SliderTrackInput.value);
    changeValue();
}


const ButtonPlayAudio = document.querySelector(".button-play-audio");
const ButtonPlayAudioSuggestion = document.getElementById(`${params.get('page') ? params.get('page') : '1'}`);
ButtonPlayAudio.addEventListener('click', () => {
    buttonPlay(ButtonPlayAudio);
    if (url.pathname == '/podcast/') {
        if (!SliderAudio.paused) {
            ButtonPlayAudioSuggestion.firstChild.className = 'fas fa-pause';
        } else {
            ButtonPlayAudioSuggestion.firstChild.className = 'fas fa-play';
        }
    }
});
if (url.pathname == '/podcast/') {
    ButtonPlayAudioSuggestion.addEventListener('click', () => {
        buttonPlay(ButtonPlayAudioSuggestion);
        if (!SliderAudio.paused) {
            ButtonPlayAudio.firstChild.className = 'fas fa-pause';
        } else {
            ButtonPlayAudio.firstChild.className = 'fas fa-play';
        }
    });
}

function buttonPlay(element) {
    if (SliderAudio.paused) {
        SliderAudio.play();
        element.firstChild.className = 'fas fa-pause';
    } else {
        SliderAudio.pause();
        element.firstChild.className = 'fas fa-play';
    }
}

SliderAudio.addEventListener('ended', () => {
    ButtonPlayAudio.firstChild.className = 'fas fa-play';
    ButtonPlayAudioSuggestion.firstChild.className = 'fas fa-play';
    if (!document.querySelector('.button-forward-audio').disabled) {
        window.location.href = '?page=' + document.querySelector('.button-forward-audio').onclick.toString().charAt(document.querySelector('.button-forward-audio').onclick.toString().lastIndexOf('=') + 1) + '#podcasts';
    }
});

let ButtonBackwardAudio = document.querySelector(".button-backward-audio");

ButtonBackwardAudio.addEventListener('click', () => buttonBackward());

function buttonBackward() {
    if (SliderAudio.currentTime > 1) {
        SliderTrackInput.setAttribute("value", "0");
        SliderAudio.currentTime = 0;
        changeValue();
    } else if (ButtonBackwardAudio.ondblclick) {
        window.location.href = '?page=' + ButtonBackwardAudio.ondblclick.toString().charAt(ButtonBackwardAudio.ondblclick.toString().lastIndexOf('=') + 1) + '#podcasts';
    }
}

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    SliderAudio.addEventListener('loadedmetadata', () => {
        max = Math.floor(SliderAudio.duration);
        SliderCounterMax.innerHTML = valueToTime(max);
        SliderTrackInput.setAttribute("max", max);
        audioSlider();
    });
    max = Math.floor(SliderAudio.duration);
    SliderCounterMax.innerHTML = valueToTime(max);
    SliderTrackInput.setAttribute("max", max);
    audioSlider();

    if (params.has('page')) {
        SliderAudio.paused = false;
        buttonPlay(ButtonPlayAudio);
        setTimeout(() => {
            if (SliderAudio.paused == true) {
                ButtonPlayAudio.firstChild.className = 'fas fa-play';
            }
            if (url.pathname == '/podcast/') {
                if (!SliderAudio.paused) {
                    ButtonPlayAudioSuggestion.firstChild.className = 'fas fa-pause';
                } else {
                    ButtonPlayAudioSuggestion.firstChild.className = 'fas fa-play';
                }
            }
        }, 100);
    }
}

let lyrics = document.querySelector('.lyrics');

lyrics.addEventListener('click', () => {
    lyrics.nextElementSibling.classList.toggle('chapitres-active');
    if (lyrics.childNodes[3].className == 'fas fa-angle-down') {
        lyrics.childNodes[3].className = 'fas fa-angle-up';
    } else {
        lyrics.childNodes[3].className = 'fas fa-angle-down';
    }
});



function timeToValue(params) {
    minute = params.split(':')[0];
    second = params.split(':')[1];
    return parseInt(minute) * 60 + parseInt(second);
}


let chapitres = document.querySelectorAll('.chapitre-content');

chapitres.forEach(element => {
    element.addEventListener('click', () => changeTime(timeToValue(element.firstElementChild.innerHTML)));
});

function changeTime(time) {
    SliderTrackInput.setAttribute("value", time);
    SliderAudio.currentTime = time;
    changeValue();
}
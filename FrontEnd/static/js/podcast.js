let SliderTrackInput = document.querySelector('.slider-track-input');
let SliderCounterCurrent = document.querySelector('.slider-counter-current');
let SliderCounterMax = document.querySelector('.slider-counter-max');
let SliderTrackActive = document.querySelector('.slider-track-active');
let SliderAudio = document.querySelector('.slider-audio');


var max = Math.floor(SliderAudio.duration);
SliderCounterMax.innerHTML = valueToTime(max);
SliderTrackInput.setAttribute("max", max);
audioSlider();


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

function audioSlider(params) {
    SliderTrackInput.setAttribute("value", SliderTrackInput.value);
    SliderAudio.currentTime = SliderTrackInput.value;
    changeValue();
}

function changeValue(params) {
    SliderCounterCurrent.innerHTML = valueToTime(SliderTrackInput.value);
    SliderTrackActive.style.width = SliderTrackInput.value * 100 / max + "%";
}


function audioPlay(params) {
    SliderTrackInput.value = SliderAudio.currentTime;
    SliderTrackInput.setAttribute("value", SliderTrackInput.value);
    changeValue();
}


let ButtonPlayAudio = document.querySelector(".button-play-audio");

ButtonPlayAudio.addEventListener('click', () => buttonPlay());

function buttonPlay(params) {
    if (SliderAudio.paused) {
        SliderAudio.play();
        ButtonPlayAudio.firstChild.className = 'fas fa-pause';
    } else {
        SliderAudio.pause();
        ButtonPlayAudio.firstChild.className = 'fas fa-play';
    }
}

let ButtonBackwardAudio = document.querySelector(".button-backward-audio");

ButtonBackwardAudio.addEventListener('click', () => buttonBackward());

function buttonBackward(params) {
    if (SliderAudio.currentTime > 1) {
        SliderTrackInput.setAttribute("value", "0");
        SliderAudio.currentTime = 0;
        changeValue();
    } else {

    }
}
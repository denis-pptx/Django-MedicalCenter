const defaultSecondsLeft = 60 * 60;
let secondsLeft = localStorage.getItem('secondsLeft') || defaultSecondsLeft;
let timer = document.querySelector('.countdown-timer');

function updateTimer() {
    timer.innerHTML = new Date(secondsLeft * 1000).toISOString().slice(11, 19);

    secondsLeft--;
    if (secondsLeft < 0)
        secondsLeft = defaultSecondsLeft;
    
    localStorage.setItem('secondsLeft', secondsLeft);
}

updateTimer();
setInterval(updateTimer, 1000);


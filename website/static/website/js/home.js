let currentBanner = 0;
let interval = document.querySelector('.banner-container').dataset.interval || 5000;
let intervalId;

let bannerContainer = document.querySelector('.banner-container');
let banners = bannerContainer.querySelectorAll('.banner');

function rotateBanner() {
    for (let i = 0; i < banners.length; i++) {
        if (i === currentBanner) {
            banners[i].hidden = false; // Показать 
        } else {
            banners[i].hidden = true; // Скрыть 
        }
    }

    currentBanner++;
    if (currentBanner === banners.length) {
        currentBanner = 0;
    }
}

function startRotation() {
    intervalId = setInterval(rotateBanner, interval);
}

function stopRotation() {
    clearInterval(intervalId);
}


startRotation();
window.addEventListener('focus', startRotation);
window.addEventListener('blur', stopRotation);

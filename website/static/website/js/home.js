var currentBanner = 0;
var interval = document.querySelector('.banner-container').dataset.interval || 5000;

function rotateBanner() {
    var bannerContainer = document.querySelector('.banner-container');
    var banners = bannerContainer.querySelectorAll('.banner');

    for (var i = 0; i < banners.length; i++) {
        if (i === currentBanner) {
            banners[i].hidden = false; // Показать текущий баннер
        } else {
            banners[i].hidden = true; // Скрыть остальные
        }
    }

    currentBanner++;
    if (currentBanner === banners.length) {
        currentBanner = 0;
    }
}

rotateBanner();
setInterval(rotateBanner, interval);

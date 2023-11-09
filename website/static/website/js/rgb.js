const rgbButton = document.getElementById('RGB');
var isGoing = false;
var intervalId;

rgbButton.addEventListener('click', () => {
    if (!isGoing) {
        randomBackground();
        intervalId = setInterval(randomBackground, 1000);
    } else {
        clearInterval(intervalId);
    }
    
    isGoing = !isGoing;
});

function randomBackground() {
    let color = `rgb(${Math.random() * 255},${Math.random() * 255},${Math.random() * 255})`;
    rgbButton.style.transition = 'background-color 2s'

    document.body.style.backgroundImage = 'none';
    document.body.style.backgroundColor = color;
    rgbButton.style.backgroundColor = color;
}
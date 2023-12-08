const leftDoctor = document.getElementById('left-doctor');
const rightDoctor = document.getElementById('right-doctor');
const text = document.getElementById('text');


window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const leftOffset = scrollY / 2; 
    const rightOffset = scrollY / 2; 

    leftDoctor.style.left = `calc(40px - ${leftOffset}px)`;
    rightDoctor.style.right = `calc(10px - ${rightOffset}px)`;


    const translateY = scrollY * 0.8;
    const scale = 1 - scrollY / 2000;
    text.style.transform = `translateY(${translateY}px) scale(${scale})`;
})
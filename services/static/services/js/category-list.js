const cards = document.querySelectorAll('.card');

cards.forEach((card) => {
    card.addEventListener('mousemove', (e) => {
        const cardRect = card.getBoundingClientRect();
        const cardCenterX = cardRect.left + cardRect.width / 2;
        const cardCenterY = cardRect.top + cardRect.height / 2;

        // Смещение курсора относительно центра карточки
        const offsetX = e.clientX - cardCenterX;
        const offsetY = e.clientY - cardCenterY;

        // Ууглы вращения
        const rotateX = -(offsetY / 10);
        const rotateY = offsetX / 10;
  
        card.style.transform = `perspective(2000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener('mouseout', () => {
        card.style.transform = 'rotate(0)';
    });
});

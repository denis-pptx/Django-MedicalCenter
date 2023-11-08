const styleControlsCheckbox = document.getElementById('styleControls');
const controlsContainer = document.querySelector('.controls-container');

styleControlsCheckbox.addEventListener('change', function() {
    if (this.checked) {
        addControls();
    } else {
        removeControls();
    }
});

function addControls() {
    if (!controlsContainer) {
        return;
    }

    // Создание элементов управления
    const fontSizeLabel = document.createElement('label');
    fontSizeLabel.textContent = 'Размер шрифта: ';
    const fontSizeInput = document.createElement('input');
    fontSizeInput.type = 'number';
    fontSizeInput.min = '5';
    fontSizeInput.max = '30';

    const textColorLabel = document.createElement('label');
    textColorLabel.textContent = 'Цвет текста: ';
    const textColorInput = document.createElement('input');
    textColorInput.type = 'color';

    const bgColorLabel = document.createElement('label');
    bgColorLabel.textContent = 'Цвет фона: ';
    const bgColorInput = document.createElement('input');
    bgColorInput.type = 'color';

    // Добавить элементы управления в контейнер
    controlsContainer.append(
        document.createElement('br'),
        fontSizeLabel, 
        fontSizeLabel, 
        fontSizeInput,
        document.createElement('br'),
        document.createElement('br'),
        textColorLabel,
        textColorInput,
        document.createElement('br'),
        document.createElement('br'),
        bgColorLabel,
        bgColorInput);

    // Добавить обработчики
    fontSizeInput.addEventListener('change', function() {
        document.body.style.fontSize = this.value + 'px';
    });

    textColorInput.addEventListener('change', function() {
        document.body.style.color = this.value;
    });

    bgColorInput.addEventListener('change', function() {
        document.body.style.backgroundImage = `none`;
        document.body.style.backgroundColor = this.value;
    });
}

function removeControls() {
    while (controlsContainer.firstChild) {
        controlsContainer.removeChild(controlsContainer.firstChild);
    }
}

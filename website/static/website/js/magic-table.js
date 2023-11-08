const table = document.getElementById('magic-table');
const sizeInput = document.getElementById('size');
const createButton = document.getElementById('create');

createButton.addEventListener('click', function () {
    const size = sizeInput.value;
    if (size < 1 || size > 20) {
        alert('Размер таблицы должен быть от 1 до 20.');
        return;
    }

    // Удалить существующую таблицу
    table.innerHTML = ''

    // Создать новую таблицу
    for (let i = 0; i < size; i++) {
        const row = table.insertRow(i);
        for (let j = 0; j < size; j++) {
            const cell = row.insertCell(j);
            cell.textContent = Math.floor(Math.random() * 1000);
        }
    }
});


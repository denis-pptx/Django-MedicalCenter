let table = document.getElementById('magic-table');
const sizeInput = document.getElementById('size');
const createButton = document.getElementById('create');
const transposeButton = document.getElementById('transpose');

createButton.addEventListener('click', function () {
    let size = sizeInput.value;
    if (size < 1 || size > 20) {
        alert('Размер таблицы должен быть от 1 до 20.');
        return;
    }

    // Удалить существующую таблицу
    table.innerHTML = ''

    // Создать новую таблицу
    for (let i = 0; i < size; i++) {
        let row = table.insertRow(i);
        for (let j = 0; j < size; j++) {
            let cell = row.insertCell(j);
            cell.textContent = Math.floor(Math.random() * 1000);
        }
    }
});

transposeButton.addEventListener('click', function () {
    let rows = table.rows;
    let cols = rows[0].cells;

    if (rows.length == 0) 
        return; // Таблица пустая
    
    // Создать новую таблицу для транспонирования
    let transposedTable = table.cloneNode();
    
    for (let i = 0; i < cols.length; i++) {
        let transposedRow = transposedTable.insertRow(i);
        for (let j = 0; j < rows.length; j++) {
            let transposedCell = transposedRow.insertCell(j);
            transposedCell.textContent = rows[j].cells[i].textContent;
        }
    }

    // Заменить таблицу
    table.replaceWith(transposedTable)
    table = transposedTable;
});

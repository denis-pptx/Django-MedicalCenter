let table = document.getElementById('magic-table');

const sizeInput = document.getElementById('size');
const createButton = document.getElementById('create');

const transposeButton = document.getElementById('transpose');

const addRowButton = document.getElementById('addRow');
const addColumnButton = document.getElementById('addColumn');


function createTable() {
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
}

function transposeTable() {
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
}

function addRow() {
    let newRow = table.insertRow(table.rows.length);
    let cols = table.rows[0].cells;
    for (let i = 0; i < cols.length; i++) {
        let cell = newRow.insertCell(i);
        cell.textContent = Math.floor(Math.random() * 1000);
    }
    transposeButton.disabled = false;
}

createButton.addEventListener('click', createTable);
transposeButton.addEventListener('click', transposeTable);
addRowButton.addEventListener('click', addRow);
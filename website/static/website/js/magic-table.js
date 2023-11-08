const MAX_NUMBER = 1000;
const MIN_SIDE = 1;
const MAX_SIDE = 25;

let table = document.getElementById('magic-table');

const sizeInput = document.getElementById('size');
sizeInput.min = MIN_SIDE;
sizeInput.max = MAX_SIDE;

const createButton = document.getElementById('create');
const transposeButton = document.getElementById('transpose');
const addRowButton = document.getElementById('addRow');
const addColumnButton = document.getElementById('addColumn');


function createTable() {
    let size = sizeInput.value;
    if (size < MIN_SIDE || size > MAX_SIDE) {
        alert(`Размер таблицы должен быть от ${MIN_SIZE} до ${MAX_SIDE}.`);
        return;
    }

    // Удалить существующую таблицу
    table.innerHTML = ''

    // Создать новую таблицу
    for (let i = 0; i < size; i++) {
        let row = table.insertRow(i);
        for (let j = 0; j < size; j++) {
            let cell = row.insertCell(j);
            cell.textContent = Math.floor(Math.random() * MAX_NUMBER);
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
        cell.textContent = Math.floor(Math.random() * MAX_NUMBER);
    }
    transposeButton.disabled = false;
}

function addColumn() {
    let rows = table.rows;
    for (let i = 0; i < rows.length; i++) {
        let cell = rows[i].insertCell(rows[i].cells.length);
        cell.textContent = Math.floor(Math.random() * MAX_NUMBER);
    }
}

function makeTableOperation(func) {
    if (table.rows.length == 0)
        alert('Таблица пустая!');
    else
        func();
}

createButton.addEventListener('click', createTable);

transposeButton.addEventListener('click', () => {
    if (table.rows.length == 0)
        alert('Таблица пустая!');
    else
        transposeTable();
});

addRowButton.addEventListener('click', () => {
    if (table.rows.length == 0)
        alert('Таблица пустая!');
    else if (table.rows.length == MAX_SIDE)
        alert(`Максимальное число строк: ${MAX_SIDE}`);
    else
        addRow();
});
addColumnButton.addEventListener('click', () => {
    if (table.rows.length == 0)
        alert('Таблица пустая!');
    else if (table.rows[0].cells.length == MAX_SIDE)
        alert(`Максимальное число колонок: ${MAX_SIDE}`);
    else
        addColumn();
});
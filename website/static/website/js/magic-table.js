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

            transposedCell.style.backgroundColor = rows[j].cells[i].style.backgroundColor;
            transposedCell.style.color = rows[j].cells[i].style.color;
            if (rows[j].cells[i].hasAttribute('selected'))
                transposedCell.setAttribute('selected', true);
        }
    }

    // Удалить элементы исходной таблицы
    while (table.firstChild)
        table.firstChild.remove();

    // Вставить детей транспонированной таблицы в эту
    for (let child of transposedTable.children) 
        table.appendChild(child);
}

function addRow() {
    let newRow = table.insertRow(table.rows.length);
    let cols = table.rows[0].cells;
    for (let i = 0; i < cols.length; i++) {
        let cell = newRow.insertCell(i);
        cell.textContent = Math.floor(Math.random() * MAX_NUMBER);
    }
}

function addColumn() {
    let rows = table.rows;
    for (let i = 0; i < rows.length; i++) {
        let cell = rows[i].insertCell(rows[i].cells.length);
        cell.textContent = Math.floor(Math.random() * MAX_NUMBER);
    }
}

function hasSelectedNeighbor(cell) {
    let row = cell.parentElement.rowIndex;
    let col = cell.cellIndex;

    const neighbors = [
        { r: -1, c: 0 }, // Сверху
        { r: 1, c: 0 },  // Снизу
        { r: 0, c: -1 }, // Слева
        { r: 0, c: 1 }   // Справа
    ];

    for (const neighbor of neighbors) {
        const neighborRow = row + neighbor.r;
        const neighborCol = col + neighbor.c;

        if (neighborRow >= 0 && neighborRow < table.rows.length &&
            neighborCol >= 0 && neighborCol < table.rows[0].cells.length) {

            const neighborCell = table.rows[neighborRow].cells[neighborCol];
            if (neighborCell.getAttribute('selected') == 'true')
                return true;
        }
    }

    // Нет покрашенных соседей
    return false; 
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




table.addEventListener('click', (event) => {
    let cell = event.target;

    if (cell.tagName == 'TD' && !hasSelectedNeighbor(cell)) {
        let number = parseInt(cell.textContent);
        
        if (number == 0) {
            cell.style.backgroundColor = 'green';
            cell.style.color = 'white';
        }
        else if (number % 2 == 0) {
            cell.style.backgroundColor = 'gray';
            cell.style.color = 'white';
        } else {
            cell.style.backgroundColor = 'red';
            cell.style.color = 'white';
        }

        cell.setAttribute('selected', true);
    }
});

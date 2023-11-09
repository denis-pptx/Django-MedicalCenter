let dateInput = document.getElementById('id_date_of_birth');
dateInput.setAttribute('max', new Date().toISOString().slice(0, 10));
dateInput.setAttribute('min', '1900-01-01');

let info = document.querySelector('.info');
let registerButton = document.getElementById('register');

const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];

dateInput.addEventListener('change', function () {
    setTimeout(function () {
        let birthDate = new Date(dateInput.value);
        let currentDate = new Date();

        let ageInMilliseconds = currentDate - birthDate;
        let years = Math.floor(ageInMilliseconds / (1000 * 60 * 60 * 24 * 365));

        let dayOfWeek = birthDate.getDay();
        let text = `Дата рождения: ${dateInput.value} (${daysOfWeek[dayOfWeek]})<br>Возраст: ${years}`;

        if (years < 18) {
            alert('Малышам сюда нельзя!')
            text += '<br>Позови старших!'
            registerButton.disabled = true;
        }
        else {
            registerButton.disabled = false;
        }

        info.innerHTML = text;


    }, 0);
});

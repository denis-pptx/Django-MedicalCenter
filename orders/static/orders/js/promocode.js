const promoCodeInput = document.getElementById('promo-code-input');
const promoCodeInfo = document.getElementById('promo-code-info');
const applyPromoCodeButton = document.getElementById('apply-promo-code');
const serviceIdInputHidden = document.getElementsByName('service_id')[0];
const promoCodeInputHidden = document.getElementsByName('promo_code')[0];

applyPromoCodeButton.addEventListener('click', function (event) {
    event.preventDefault();
    const promoCodeValue = promoCodeInput.value.trim();

    fetch('http://127.0.0.1:8000/services/check-promo-code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            promo_code: promoCodeValue,
            service_id: serviceIdInputHidden.value
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.valid) {
            promoCodeInfo.textContent = `Промокод "${promoCodeValue}" действителен. Скидка: ${data.discount}%. Новая цена: $${data.new_price}`;
            promoCodeInputHidden.value = promoCodeValue;
        } else {
            promoCodeInfo.textContent = data.message;
            promoCodeInputHidden.removeAttribute('value');
        }
    })
    .catch(error => {
        console.error('Произошла ошибка при проверке промокода:', error);
    });

});

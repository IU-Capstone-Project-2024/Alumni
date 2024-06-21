/* Check filling data */
function validateForm() {
    const form = document.getElementById("card-request-form");

    const fields = ['name', 'surname', 'email', 'telegram', 'visit-date'];
    let isValid = true;

    // Clear previous error messages and styles
    fields.forEach(field => {
        const input = form.elements[field];
        input.classList.remove('error');
        const errorMessage = input.parentNode.querySelector('.error-message');
        if (errorMessage) {
            errorMessage.remove();
        }
    });

    // Check each field
    fields.forEach(field => {
        const input = form.elements[field];
        if (input.value.trim() === '') {
            isValid = false;
            input.classList.add('error');
            const errorMessage = document.createElement('div');
            errorMessage.className = 'error-message';
            errorMessage.innerText = 'Field is required';
            input.parentNode.appendChild(errorMessage);
        }
    });

    // Add event listeners to remove error styles when user starts typing
    fields.forEach(field => {
        const input = form.elements[field];
        input.addEventListener('focus', function () {
            input.classList.remove('error');
            const errorMessage = input.parentNode.querySelector('.error-message');
            if (errorMessage) {
                errorMessage.remove();
            }
        });
    });

    // Check correctness of the email domain
    const emailInput = form.elements['email'];
    if (emailInput.value.trim() !== '') {
        const emailDomain = "@innopolis.university";
        if (!emailInput.value.endsWith(emailDomain)) {
            isValid = false;
            emailInput.classList.add('error');
            const errorMessage = document.createElement('div');
            errorMessage.className = 'error-message';
            errorMessage.innerText = `Please enter your email with the domain ${emailDomain}`;
            emailInput.parentNode.appendChild(errorMessage);
        }
    }

    // Check correctness of the Telegram alias
    const telegramInput = form.elements['telegram'];
    if (telegramInput.value.trim() !== '') {
        if (!telegramInput.value.startsWith('@')) {
            isValid = false;
            telegramInput.classList.add('error');
            const errorMessage = document.createElement('div');
            errorMessage.className = 'error-message';
            errorMessage.innerText = 'Please enter your Telegram username starting with @';
            telegramInput.parentNode.appendChild(errorMessage);
        }
    }

    // Check if visit date is less than today's date
    const visitDateInput = form.elements['visit-date'];
    if (visitDateInput.value.trim() !== '') {
        const visitDate = new Date(visitDateInput.value);
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        if (visitDate < today) {
            isValid = false;
            visitDateInput.classList.add('error');
            const errorMessage = document.createElement('div');
            errorMessage.className = 'error-message';
            errorMessage.innerText = 'Please select today or a future date';
            visitDateInput.parentNode.appendChild(errorMessage);
        }
    }

    if (isValid) {
        sendFormData(form);
        form.reset();
        showSuccessAlert();
    }
}

function showSuccessAlert() {
    const successMessage = 'Your request has been sent successfully!';
    const successAlert = document.createElement('div');
    successAlert.className = 'success-alert';
    successAlert.textContent = successMessage;

    setTimeout(function () {
        document.body.appendChild(successAlert);

        setTimeout(function () {
            document.body.removeChild(successAlert);
        }, 3000);
    }, 0);
}

function sendFormData(form) {
    const data = new FormData(form);
    fetch('handle-form-submission/', {
        method: 'POST',
        body: data
    })
    .catch(error => {
        console.error('Error sending form data:', error);
    });
}

/* Filling out the date field */
document.getElementById('visit-date').addEventListener('focus', function (e) {
    this.type = 'date';
});
document.getElementById('visit-date').addEventListener('blur', function (e) {
    if (this.value === '') {
        this.type = 'text';
    }
});

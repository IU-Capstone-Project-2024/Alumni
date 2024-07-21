function initializeButtonState() {
    var button = document.querySelector('.sign-up-button');
    var currentState = localStorage.getItem('signUpCancelState');

    if (currentState === 'signed-up') {
        button.classList.remove('cancel');
        button.textContent = 'Sign up';
    } else {
        button.classList.add('cancel');
        button.textContent = 'Cancel';
    }
}

function handleSignUpCancel(event) {
    event.preventDefault();
    var button = document.querySelector('.sign-up-button');
    var eventLink = document.querySelector('input[name="activity"]').value;

    if (!button.classList.contains('cancel')) {
        fetch('/events/add-activity/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({ event_link: eventLink })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.classList.add('cancel');
                button.textContent = 'Cancel';
                showSuccessAlert('You signed up successfully! Event link added to your profile');
                localStorage.setItem('signUpCancelState', 'canceled');
            } else {
                console.error('Failed to add event link');
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        fetch('/events/delete-activity/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({ event_link: eventLink })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.classList.remove('cancel');
                button.textContent = 'Sign up';
                showSuccessAlert('Event registration canceled successfully!');
                localStorage.setItem('signUpCancelState', 'signed-up');
            } else {
                console.error('Failed to remove event link');
            }
        })
        .catch(error => console.error('Error:', error));
    }
}

function showSuccessAlert(successMessage) {
    const existingSuccessAlert = document.querySelector('.success-alert');
    if (existingSuccessAlert) {
        document.body.removeChild(existingSuccessAlert);
    }
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

initializeButtonState();
window.addEventListener('load', () => {
    const form = document.getElementById("sign-up-cancel-form");
    form.addEventListener("submit", handleSignUpCancel);
});

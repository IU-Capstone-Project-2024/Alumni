function initializeButtonState() {
    var button = document.querySelector('.check-in-button');
    var currentState = localStorage.getItem('checkInOutState');

    if (currentState === 'checked-in') {
        button.classList.remove('check-out');
        button.textContent = 'Check in';
    } else {
        button.classList.add('check-out');
        button.textContent = 'Check out';
    }
}

function handleCheckInOut(event) {
    event.preventDefault();
    var button = document.querySelector('.check-in-button');
    var eventLink = document.querySelector('input[name="activity"]').value;

    if (!button.classList.contains('check-out')) {
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
                button.classList.add('check-out');
                button.textContent = 'Check out';
                showSuccessAlert('You checked in successfully! Event link added to your profile');
                localStorage.setItem('checkInOutState', 'checked-out');
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
                button.classList.remove('check-out');
                button.textContent = 'Check in';
                showSuccessAlert('You checked out successfully!');
                localStorage.setItem('checkInOutState', 'checked-in');
            } else {
                console.error('Failed to remove event link');
            }
        })
        .catch(error => console.error('Error:', error));
    }
}

function showSuccessAlert(successMessage) {
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
    const form = document.getElementById("check-in-out");
    form.addEventListener("submit", handleCheckInOut);
});


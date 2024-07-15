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

function toggleCheckInOut() {
    var button = document.querySelector('.check-in-button');
    if (!button.classList.contains('check-out')) {
        button.classList.add('check-out');
        button.textContent = 'Check out';
        showSuccessAlert('You checked in successfully! Event link added to your profile');
        localStorage.setItem('checkInOutState', 'checked-out');
    } else {
        button.classList.remove('check-out');
        button.textContent = 'Check in';
        showSuccessAlert('You checked out successfully!');
        localStorage.setItem('checkInOutState', 'checked-in');
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

document.querySelector('.check-in-button').addEventListener('click', toggleCheckInOut);

initializeButtonState();
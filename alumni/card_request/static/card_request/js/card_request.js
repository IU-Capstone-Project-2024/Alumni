/* Year range */
var currentYear = new Date().getFullYear();

document.getElementById('graduation-year').max = currentYear;


/* Filling out the date field */
document.getElementById('receipt-date').addEventListener('focus', function (e) {
    this.type = 'date';
});
document.getElementById('receipt-date').addEventListener('blur', function (e) {
    if (this.value === '') {
        this.type = 'text';
    }
});

/* Check filling data */

document.addEventListener('DOMContentLoaded', function () {
    fetchMedicines();

    document.getElementById('add-form').addEventListener('submit', function (event) {
        event.preventDefault();
        addMedicine();
    });
});

function fetchMedicines() {
    fetch('http://localhost:5000/')
        .then(response => response.json())
        .then(data => {
            const medicineList = document.getElementById('medicine-list');
            medicineList.innerHTML = '';

            data.forEach(medicine => {
                const listItem = document.createElement('li');
                listItem.textContent = `${medicine.name} - ${medicine.dosage}`;
                medicineList.appendChild(listItem);
            });
        });
}

function addMedicine() {
    const name = document.getElementById('name').value;
    const dosage = document.getElementById('dosage').value;

    fetch('http://localhost:5000/add', {
        method:


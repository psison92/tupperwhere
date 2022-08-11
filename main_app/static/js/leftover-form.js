const dateInput = document.getElementById('id_expiration')

const picker = MCDatepicker.create({
  el: '#id_expiration',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", (evt) => {
  picker.open()
})
var myModalRenda = document.getElementById('modalAdicionarRenda')
var myInputRenda = document.getElementById('modalAdicionarRenda')

myModalRenda.addEventListener('shown.bs.modal', function () {
  myInputRenda.focus()
})
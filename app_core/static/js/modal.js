var myModalRenda = document.getElementById('modalAdicionarRenda')
var myInputRenda = document.getElementById('modalAdicionarRenda')

myModalRenda.addEventListener('shown.bs.modal', function () {
  myInputRenda.focus()
})

var myModalAcessarRenda = document.getElementById('modalAcessarRenda')
var myInputAcessarRenda = document.getElementById('modalAcessarRenda')

myModalAcessarRenda.addEventListener('shown.bs.modal', function () {
  myInputAcessarRenda.focus()
})
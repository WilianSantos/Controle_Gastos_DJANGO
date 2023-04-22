var myModalRenda = document.getElementById('modalAdicionarRenda')
var myInputRenda = document.getElementById('modalAdicionarRenda')

myModalRenda.addEventListener('shown.bs.modal', function () {
  myInputRenda.focus()
})

var myModalGasto = document.getElementById('modalAdicionarGasto')
var myInputGasto = document.getElementById('modalAdicionarGasto')

myModalGasto.addEventListener('shown.bs.modal', function () {
  myInputGasto.focus()
})
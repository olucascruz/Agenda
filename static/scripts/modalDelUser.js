let btnDelete = document.getElementById('btn-delete-user');
let btnNao = document.querySelector('.btn-nao')
let modal = document.getElementById('modal-user')

btnDelete.addEventListener('click', ()=>{    
    modal.classList.remove('hidden')
})

btnNao.addEventListener('click', ()=>{
    modal.classList.add('hidden')
})
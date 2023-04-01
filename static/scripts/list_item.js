const delBtn = document.querySelectorAll(".icon_del")
const cancelBtn = document.querySelectorAll(".btn-nao")

let modal; 

delBtn.forEach((el)=>{
    el.addEventListener("click", ()=>{
        console.log(el.id)
        modal = document.getElementById(`modal-${el.id}`);
        modal.classList.remove("hidden")    
    })
})

cancelBtn.forEach((el)=>{
    el.addEventListener("click",()=>{
        modal.classList.add("hidden")
    })
});
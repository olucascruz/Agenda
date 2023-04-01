const form = document.getElementById('form_edit_user')
const id  = document.getElementById('user_id').textContent


const editUser = async (data) => {
    const endpoint = 'edit_user/' 
    await fetch('http://localhost:8000/'+endpoint+id, {
        method: "PATCH",
        body: JSON.stringify(data),
        mode:"cors",
        headers:{
            "Content-type": "application/json",
        }, 
     })
}


form.addEventListener('submit', async (event)=>{
    event.preventDefault();
    

    const name = form['name'].value
    const email = form['email'].value
    const actual_password = form['actual_password'].value

    const data = {
        "user_name": name,
        "user_email":email, 
        "actual_password": actual_password, 
    }
    editUser(data)
    .then(window.history.back())

    
})
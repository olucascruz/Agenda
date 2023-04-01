const axios = require('axios');
const form = document.getElementById('form_edit_event')
const id  = document.getElementById('event_id').textContent
const base_url = document.getElementById('base_url').textContent



const editEvent = async (data) => {
    const endpoint = 'edit_event/' 
    try {
    const response = await axios.patch(base_url + endpoint + id, JSON.stringify(data), {
        headers: {
          'Content-Type': 'application/json',
        },
      });
    return response.data;
    } catch (error) {
    console.error(error);
    }
}


form.addEventListener('submit', async (event)=>{
    event.preventDefault();
    

    const title = form['title'].value
    const description = form['description'].value
    const date = form['date'].value
    
    
    const data = {
        "title": title,
        "description":description, 
        "date": date 
    }

    console.log(data)
    editEvent(data)
    .then(window.history.back())

    
})
<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.0.3/index.global.min.js"></script>

let calendarEl = document.getElementById("calendar");
let events = Json.parse(document.getElementById("calendar").dataset.events);

console.log(events);



let calendar = new FullCalendar.Calendar(calendarEl, {
    locale:'pt-br',
    buttonText: {
    today: 'Hoje',
    month: 'Mês',
    week: 'Semana',
    day: 'Hoje',
    list: 'Lista'
    },
    events:[],
    selectable:true,
    select: (start, end)=>{
        console.log(start)
    },
    eventClick:(info)=>{
        window.location.href = `/edit_event/${info.event.id}`
    }
})
calendar.render()

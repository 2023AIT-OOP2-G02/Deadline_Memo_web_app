const datetime = new Date().toLocaleString({ timeZone: 'Asia/Tokyo'}, { hour12: false });
const date = datetime.split(' ')[0];

const dateElement = document.getElementById('date');
dateElement.innerHTML = date;
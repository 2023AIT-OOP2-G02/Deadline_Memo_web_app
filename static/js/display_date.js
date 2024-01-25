// 日付の表示
const datetime = new Date().toLocaleString({ timeZone: 'Asia/Tokyo' }, { hour12: false });
const date = datetime.split(' ')[0];
//dateの/の直後にスペースを追加
const dateArr = date.split('/');
const dateStr = dateArr[0] + ' / ' + dateArr[1] + ' / ' + dateArr[2];

const dateElement = document.getElementById('date');
dateElement.innerHTML = dateStr;
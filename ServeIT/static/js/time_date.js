const dateElement = document.querySelector(".date");
const greetingElement = document.querySelector(".greeting");
const nth = function(d) {
  if (d > 3 && d < 21) return 'th';
  switch (d % 10) {
    case 1:  return "st";
    case 2:  return "nd";
    case 3:  return "rd";
    default: return "th";
  }
}
const ordinal = nth(date);
/**
 * @param {Date} date
 */


/**
 * @param {Date} date
 */
function formatDate(date) {
  const DAYS = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
  ];
  const MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ];

  return `${DAYS[date.getDay()]}, ${MONTHS[date.getMonth()]} ${date.getDate()}${ordinal(date.getDate())}`;
}
function getGreeting() {
  const now = new Date();
  const hours = now.getHours();
  
  if (hours < 12) {
    return "Good morning, " + userFirstName;
  } else if (hours < 18) {
    return "Good afternoon," + userFirstName;
  } else {
    return "Good evening," + userFirstName;
  }
}

setInterval(() => {
  const now = new Date();


  dateElement.textContent = formatDate(now);
}, 200);

setInterval(() => {
  greetingElement.textContent = getGreeting();
}, 200);



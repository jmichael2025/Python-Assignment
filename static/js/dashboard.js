
  let currentMonth = "{{ current_month }}";

function changeMonth(offset) {
    let date = new Date(currentMonth + "-01");
    date.setMonth(date.getMonth() + offset);

    let newMonth = date.toISOString().slice(0, 7);
    window.location.href = "/dashboard?month=" + newMonth;
}

function goCurrent() {
    window.location.href = "/dashboard";
}  

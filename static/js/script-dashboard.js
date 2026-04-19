
let monthIndex = 0;
const months = ["Previous Month", "Current Month", "Next Month"];

function changeMonth(dir){
  monthIndex = (monthIndex + dir + months.length) % months.length;
  document.getElementById("monthLabel").innerText = months[monthIndex];
}

function addRow(){
  const table = document.getElementById("expenseTable").getElementsByTagName('tbody')[0];
  const row = table.insertRow();
  for(let i=0;i<3;i++){
    const cell = row.insertCell(i);
    cell.contentEditable = true;
    cell.innerText = "Edit";
  }
}
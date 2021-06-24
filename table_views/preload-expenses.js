function getExpenses() {
    fetch("http://127.0.0.1:5000/data/expenses/")
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.expenses.length; i++) {
                console.log(data.expenses[i])
                
                var row = document.createElement("div")
                row.classList.add("row");

                var id = document.createElement("div");
                id.classList.add("col-sm-2");
                id.innerHTML = data.expenses[i].expense_id
                row.appendChild(id)

                var date = document.createElement("div");
                date.classList.add("col-sm-3");
                date.innerHTML = data.expenses[i].date
                row.appendChild(date)
                
                var name = document.createElement("div");
                name.classList.add("col-sm-3");
                name.innerHTML = data.expenses[i].name
                row.appendChild(name)

                var type = document.createElement("div");
                type.classList.add("col-sm-2");
                type.innerHTML = data.expenses[i].type
                row.appendChild(type)

                var cost = document.createElement("div");
                cost.classList.add("col-sm-2");
                cost.innerHTML = "$" + data.expenses[i].cost.toFixed(2)
                row.appendChild(cost)

                var chart = document.getElementById("expenses-rows");
                chart.appendChild(row)
            }
        });
}

getExpenses();

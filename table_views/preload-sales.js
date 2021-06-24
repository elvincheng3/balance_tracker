function getSales() {
    fetch("http://127.0.0.1:5000/data/sales/")
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.sales.length; i++) {
                console.log(data.sales[i])
                
                var row = document.createElement("div")
                row.classList.add("row");

                var id = document.createElement("div");
                id.classList.add("col-sm-1");
                id.innerHTML = data.sales[i].sale_id
                row.appendChild(id)

                var date = document.createElement("div");
                date.classList.add("col-sm-1");
                date.innerHTML = data.sales[i].date
                row.appendChild(date)
                
                var name = document.createElement("div");
                name.classList.add("col-sm-3");
                name.innerHTML = data.sales[i].name
                row.appendChild(name)

                var sku = document.createElement("div");
                sku.classList.add("col-sm-1");
                sku.innerHTML = data.sales[i].sku
                row.appendChild(sku)

                var location = document.createElement("div");
                location.classList.add("col-sm-1");
                location.innerHTML = data.sales[i].location
                row.appendChild(location)

                var gross_price = document.createElement("div");
                gross_price.classList.add("col-sm-1");
                gross_price.innerHTML = "$" + data.sales[i].gross_price.toFixed(2)
                row.appendChild(gross_price)

                var taxes = document.createElement("div");
                taxes.classList.add("col-sm-1");
                taxes.innerHTML = "$" + data.sales[i].taxes.toFixed(2)
                row.appendChild(taxes)

                var shipping_expenses = document.createElement("div");
                shipping_expenses.classList.add("col-sm-1");
                shipping_expenses.innerHTML = "$" + data.sales[i].shipping_expenses.toFixed(2)
                row.appendChild(shipping_expenses)
                
                var fees = document.createElement("div");
                fees.classList.add("col-sm-1");
                fees.innerHTML = "$" + data.sales[i].fees.toFixed(2)
                row.appendChild(fees)

                var net_price = document.createElement("div");
                net_price.classList.add("col-sm-1");
                net_price.innerHTML = "$" + data.sales[i].net_price.toFixed(2)
                row.appendChild(net_price)

                var chart = document.getElementById("sales-rows");
                chart.appendChild(row)
            }
        });
}

getSales();

function getServices() {
    fetch("http://127.0.0.1:5000/data/services/")
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.services.length; i++) {
                console.log(data.services[i])
                
                var row = document.createElement("div")
                row.classList.add("row");

                var id = document.createElement("div");
                id.classList.add("col-sm-1");
                id.innerHTML = data.services[i].service_id
                row.appendChild(id)

                var date = document.createElement("div");
                date.classList.add("col-sm-2");
                date.innerHTML = data.services[i].date
                row.appendChild(date)
                
                var name = document.createElement("div");
                name.classList.add("col-sm-3");
                name.innerHTML = data.services[i].name
                row.appendChild(name)

                var sku = document.createElement("div");
                sku.classList.add("col-sm-1");
                sku.innerHTML = data.services[i].sku
                row.appendChild(sku)

                var client = document.createElement("div");
                client.classList.add("col-sm-1");
                client.innerHTML = data.services[i].client
                row.appendChild(client)

                var unit_cost = document.createElement("div");
                unit_cost.classList.add("col-sm-1");
                unit_cost.innerHTML = "$" + data.services[i].unit_cost.toFixed(2)
                row.appendChild(unit_cost)

                var quantity = document.createElement("div");
                quantity.classList.add("col-sm-1");
                quantity.innerHTML = data.services[i].quantity
                row.appendChild(quantity)

                var total = document.createElement("div");
                total.classList.add("col-sm-2");
                total.innerHTML = "$" + data.services[i].total.toFixed(2)
                row.appendChild(total)

                var chart = document.getElementById("services-rows");
                chart.appendChild(row)
            }
        });
}

getServices();

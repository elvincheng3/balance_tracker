function getPurchases() {
    fetch("http://127.0.0.1:5000/data/purchases/")
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.purchases.length; i++) {
                // var container = document.createElement("div");
                // var node = document.createTextNode("test");
                // container.appendChild(node);
                // var element = document.getElementById("body");
                // console.log("found element")
                // element.appendChild(container)

                console.log(data.purchases[i])
                
                var row = document.createElement("div")
                row.classList.add("row");

                var id = document.createElement("div");
                id.classList.add("col-sm-1");
                id.innerHTML = data.purchases[i].purchase_id
                row.appendChild(id)

                var date = document.createElement("div");
                date.classList.add("col-sm-2");
                date.innerHTML = data.purchases[i].date
                row.appendChild(date)
                
                var name = document.createElement("div");
                name.classList.add("col-sm-3");
                name.innerHTML = data.purchases[i].name
                row.appendChild(name)

                var sku = document.createElement("div");
                sku.classList.add("col-sm-1");
                sku.innerHTML = data.purchases[i].sku
                row.appendChild(sku)

                var site = document.createElement("div");
                site.classList.add("col-sm-1");
                site.innerHTML = data.purchases[i].site
                row.appendChild(site)

                var size = document.createElement("div");
                size.classList.add("col-sm-1");
                size.innerHTML = data.purchases[i].size
                row.appendChild(size)

                var price = document.createElement("div");
                price.classList.add("col-sm-1");
                price.innerHTML = "$" + data.purchases[i].price.toFixed(2)
                row.appendChild(price)

                var status = document.createElement("div");
                status.classList.add("col-sm-2");
                status.innerHTML = data.purchases[i].status
                row.appendChild(status)

                var chart = document.getElementById("purchase-rows");
                chart.appendChild(row)
            }
        });
}

getPurchases();
// $(document).ready(function() {
//     $('.selectpicker').selectpicker();
//  });
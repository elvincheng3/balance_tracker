function getSkulist() {
    fetch("http://127.0.0.1:5000/data/skulist/")
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.skulist.length; i++) {
                console.log(data.skulist[i])
                
                var row = document.createElement("div")
                row.classList.add("row");

                var sku = document.createElement("div");
                sku.classList.add("col-sm-6");
                sku.innerHTML = data.skulist[i].sku
                row.appendChild(sku)

                var model = document.createElement("div");
                model.classList.add("col-sm-6");
                model.innerHTML = data.skulist[i].model
                row.appendChild(model)

                var chart = document.getElementById("skulist-rows");
                chart.appendChild(row)
            }
        });
}

getSkulist();

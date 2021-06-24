fetch("http://127.0.0.1:5000/data/skulist/")
    .then(response => response.json())
    .then(data => {
        for (var i = 0; i < data.skulist.length; i++) {
            var opt = '<option value="' + data.skulist[0'">Volvo</option>'
        }
    }) 
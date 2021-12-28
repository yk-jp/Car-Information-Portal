const config = {
    'baseUrl': 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&model'
}

document.getElementById('carMake').addEventListener('change', (e) => {
    $.ajax({
        type: 'GET',
        url: `${config.baseUrl}&make=${e.target.value}`,
        dataType: 'json',
        success: function(data) {
            const modelsData = data["Trims"];
            let models = [];
            modelsData.forEach((model) => {
                if (!models.includes(model['model_name'])) models.push(model['model_name']);
            })

            const carModelEle = document.getElementById('carModel');
            carModelEle.innerHTML = ` <option selected>CAR MODEL</option>`;

            models.forEach((model) => {
                carModelEle.innerHTML += ` <option value="${model}">${model}</option>`;
            });
        },
        error: function(error) {
            console.log(error);
        }
    });
});
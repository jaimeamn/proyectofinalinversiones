(function() {

    function getMovements() {
        fetch('http://localhost:5000/api/v1/movimientos')
            .then(response => response.json())
            .then(data => renderData("tbody-movimientos", data));
    }


    function renderData(target, data) {

        let elementTarget = document.getElementById(target);

        data.data.forEach(element => {


            let tbodyConten =
                `<tr> 
        <td> ${element.fecha} </td>
        <td> ${element.hora} </td>
        <td> ${element.moneda_from}</td>
        <td> ${element.cantidad_from}</td>
        <td> ${element.moneda_to}</td>
        <td> ${element.cantidad_to}</td>
        </tr>`;

            elementTarget.innerHTML += tbodyConten;

        });

    }

    getMovements();
})()
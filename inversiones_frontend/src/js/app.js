(function(window) {

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

    window.addEventListener('load', function() {
        getMovements();
    });

    // peticion crear movimiento

    function saveMovement() {
        let data = {data:getDataForm()};
        const client = new XMLHttpRequest();
        fetch('http://localhost:5000/api/v1/movimiento', {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers:{
              'Content-Type': 'application/json'
            }})
            .then(response => response.json())
            .then(data => {console.log(data)});
            
    }

// evento en boton ok envio de formulario al backend
    let okButton = document.getElementById("ok");
    okButton.addEventListener("click", saveMovement);

    function getDataForm(){ 
        let fromValue = document.getElementById("from").value;
        let toValue = document.getElementById("to").value;
        let quantityFromValue = document.getElementById("cantidad_from").value;
        let quantityToValue = document.getElementById("cantidad_to").value;
        return{ moneda_from: fromValue,
                 moneda_to: toValue,
                 cantidad_from:quantityFromValue,
                 cantidad_to:quantityToValue

        }
    }

//funcionalidad boton añadir movimiento
    let addButton = document.getElementById("btn-alta");
    addButton.addEventListener("click", showForm);

     function showForm(){ 
         let sectAddMovements = document.getElementById("movimiento-activo");
         sectAddMovements.classList.remove("hide-form");




     }
})(window)
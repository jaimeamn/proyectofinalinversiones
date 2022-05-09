(function(window) {

'use strict';

//funcionalidad listar todos los movimientos
    function getMovements() {
        fetch('http://localhost:5000/api/v1/movimientos')
            .then(response => response.json())
            .then(data => renderMovements("tbody-movimientos", data));
    }

    function renderMovements(target, data) {

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
        let uno = -10;
        if (uno < 0) {
            let val_invertido = document.querySelector('#val-invertido');
            let val_val = document.querySelector('#val-valor');
            val_invertido.style.color = 'red';
            val_val.style.color = 'green';
            // val_invertido.classList.add('color-rojo');
            // val_invertido.className = 'color-rojo';
        }
    }

    

    // peticion crear movimiento

    function saveMovement() {
        let data = {data:getDataForm()};
        //const client = new XMLHttpRequest();
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

    

//funcionalidad boton compra venta de criptos
    let addButton = document.getElementById("btn-alta");
    addButton.addEventListener("click", showForm);

     function showForm(){ 
         let sectAddMovements = document.getElementById("movimiento-activo");
         sectAddMovements.classList.remove("hide-form");

     }

// funcionalidad calcular
     let buttonCalcular = document.getElementById("aceptar");
     buttonCalcular.addEventListener("click", calcular)

      function calcular(){
        let data = getDataForm();
        
        fetch(`http://localhost:5000/api/v1/tipo_cambio?moneda_from=${data.moneda_from}&moneda_to=${data.moneda_to}&cantidad_from=${data.cantidad_from}`)
        .then(response => response.json())
        .then(response => {
            let data = response.data;
            let inputQTo = document.getElementById("cantidad_to");
            let inputPU = document.getElementById("precio_unitario");
            inputQTo.value = Number(data.quantityTo);
            inputPU.value = Number(data.unit_price);            
        });
          
      }

      //helpers
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

      function status(){
          


      }

    //init
    window.addEventListener('load', function() {
        getMovements();
    });

})(window)
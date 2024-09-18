function validate(){

    //Variables

    let contactFullName = document.formSuggest.contactFullName.value
    let emailContact = document.formSuggest.emailContact.value
    let phoneContact = document.formSuggest.phoneContact.value
    let messageUser = document.getElementById('messageUser').value

    //Validation Pattern
    
    let minusculas = /[a-z]/g

    let mayusculas = /[A-Z]/g

    let numeros = /[1-999999999999]/g

    let patternEmail = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i


    if(contactFullName.length < 5){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre completo no puede tener menos de 5 caracteres, por favor intenta nuevamente',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false  
    }

    else if(contactFullName.match(numeros)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre completo no puedo contener numeros, intenta nuevamente',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false          
    }

    else if(emailContact.length < 5){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El correo electronico no puede tener menos de 5 caracteres, por intenta nuevamente',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false          
    }

    else if(!patternEmail.test(emailContact)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El correo ingresado es invalido, por favor intenta nuevamente',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false                  
    }

    else if(phoneContact.length > 10 || phoneContact.length < 10){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El telefono de contacto debe ser de 10 digitos, por favor intenta nuevamente',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false                  
    }

    else if(phoneContact.match(minusculas) || phoneContact.match(mayusculas)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El numero de contacto no puede tener letras, por favor intenta nuevamente',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false                  
    }

    else if(messageUser == ''){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La sugerencia no puede estar vacia, por favor intenta nuevamente y rellena tu sugerencia',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false               
    }
    else{
        return true
    }

}
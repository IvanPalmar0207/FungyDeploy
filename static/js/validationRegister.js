function validateRegister(){
    let firstName = document.form.firstName.value
    let lastName = document.form.lastName.value
    let userName = document.form.userName.value
    let userEmail = document.form.userEmail.value
    let userPassword = document.form.userPassword.value
    let userConfirm = document.form.userConfirm.value

    //Validation Pattern
    
    let minusculas = /[a-z]/g
    let mayusculas = /[A-Z]/g
    let numeros = /[1-999999999999]/g
    let patternEmail = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
    let patternPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/

    
    if(firstName.length < 5){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre no puede tener menos de 5 caracteres, intenta nuevamente.',
            confirmButtonText: "Reenviar",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false  
    }    

    else if(firstName.match(numeros)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre no puede contener numeros, intenta nuevamente.',
            confirmButtonText: "Reenviar",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
   }

   else if(lastName.length < 5){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'El apellido no puede tener menos de 5 caracteres, intenta nuevamente.',
        confirmButtonText: "Reenviar",
        allowEnterKey:true,
        allowOutsideClick:false,
        confirmButtonColor:"red"
        }
    )
        return false
   }

   else if(lastName.match(numeros)){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'El apellido no puede contener numeros, intenta nuevamente.',
        confirmButtonText: "Reenviar",
        allowEnterKey:true,
        allowOutsideClick:false,
        confirmButtonColor:"red"
        }
    )
        return false
   }

   else if(userName.length < 5){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'El nombre de usuario no puede tener menos de 5 caracteres, intenta nuevamente.',
        confirmButtonText: "Reenviar",
        allowEnterKey:true,
        allowOutsideClick:false,
        confirmButtonColor:"red"
        }
    )
        return false
   }

   else if(userEmail.length < 5){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'El correo electronico no puede tener menos de 5 caracteres, intenta nuevamente.',
        confirmButtonText: "Reenviar",
        allowEnterKey:true,
        allowOutsideClick:false,
        confirmButtonColor:"red"
        }
    )
        return false
   }

   else if(!patternEmail.test(userEmail)){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'El correo es incorrecto, intenta nuevamente.',
        confirmButtonText: "Reenviar",
        allowEnterKey:true,
        allowOutsideClick:false,
        confirmButtonColor:"red"
        }
    )
        return false
   }

   else if(userPassword.length > 16 || userPassword.length < 8){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'La contraseña no tener más de 16 caracteres ni menos de 8 caracteres, intenta nuevamente.',
        confirmButtonText: "Reenviar",
        allowEnterKey:true,
        allowOutsideClick:false,
        confirmButtonColor:"red"
        }
    )
        return false
   }

   else if(!patternPassword.test(userPassword)){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Recuerda que la contraseña debe contener almenos una letra minuscula, una letra mayuscula y un numero',
        confirmButtonText: "Reenviar",
        allowEnterKey:true,
        allowOutsideClick:false,
        confirmButtonColor:"red"
        }
    )
        return false
   }

   else if(userPassword !== userConfirm){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Las contraseñas son diferentes, intenta nuevamente.',
        confirmButtonText: "Reenviar",
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
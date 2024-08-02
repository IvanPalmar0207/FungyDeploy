function validate(){
    //Form Fields
    let userName = document.formLogin.username.value
    let password = document.formLogin.password.value

    //Validation password
    var patternPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/


    if(userName.lenght > 60 || userName.lenght < 8){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre de usuario no puede tener mas de 60 caracteres ni menos de 8 caracteres, intenta nuevamente',
            confirmButtonText: "Reenviar",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false  
    }

    else if(password.lenght > 16 || password.lenght < 8){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La contraseña no puede tener más de 16 caracteres ni menos de 8 caracteres, por favor intenta nuevamente',
            confirmButtonText: "Reenviar",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else if(!patternPassword.test(password)){
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
    else{
        return true
    }

}

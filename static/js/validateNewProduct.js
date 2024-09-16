function validateNewProduct(){
    
    let productName = document.form.productName.value
    let priceProduct = document.form.priceProduct.value
    let descriptionProduct = document.form.descriptionProduct.value
    
    //Pattern Validators
    
    let minusculas = /[a-z]/g

    let mayusculas = /[A-Z]/g    

    if(productName.length < 5 || productName.length > 100){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre del producto no puede tener menos de 5 caracteres ni más de 100 caracteres, intenta nuevamente.',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false 
    }
    else if(priceProduct.match(minusculas) || priceProduct.match(mayusculas)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El precio del producto no puede contener letras, intenta nuevamente.',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false 
    }

    else if(priceProduct.length > 40){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El precio del producto no puede contener mas de 40 caracteres, intenta nuevamente.',
            confirmButtonText: "Volver",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false 
    }

    else if(descriptionProduct.length < 5 || descriptionProduct.length > 150){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La descripción del producto no puede contener menos de 5 caracteres ni más de 150 caracteres, intenta nuevamente.',
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
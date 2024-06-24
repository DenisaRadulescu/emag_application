function firstFunction() {
    let title_products = document.getElementById("titleId")

//    console.log(title_products.innerHTML)
    if (title_products.style.color === 'black') {
        title_products.style.color = 'green'
    }
    else {
        title_products.style.color = 'black'
    }



}

function display_add_product_form() {
    let add_product_button = document.getElementById("button2")
    add_product_button.style.display = 'none'
    if (add_product_button.style.display === 'none') {
        document.getElementById("add_product").style.display = 'block'
    }
}



function display_delete_product_form() {
    let delete_product_button = document.getElementById("button3")
    delete_product_button.style.display = 'none'
    if (delete_product_button.style.display === 'none') {
        document.getElementById("delete_product").style.display = 'block'
    }
}

function display_update_price_form() {
    let update_price_button = document.getElementById("button4")
    update_price_button.style.display = 'none'
    if (update_price_button.style.display === 'none') {
        document.getElementById("update_price").style.display = 'block'
    }
}
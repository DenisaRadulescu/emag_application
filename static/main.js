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

function display_most_expensive_product_form() {
    let most_expensive_product_button = document.getElementById("button5");
    most_expensive_product_button.style.display = 'none';
    if (most_expensive_product_button.style.display === 'none') {
        fetch_most_expensive_product();
    }
}

function get_most_expensive_product() {
    fetch('/most_expensive_product')
    .then(response => response.text())
    .then(data => {
        document.getElementById("prod_name").innerText = data;
        document.getElementById("most_expensive_product").style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
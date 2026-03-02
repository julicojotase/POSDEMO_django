let cart = []
let total = 0

function addProduct(id, name, price)
{

price = parseFloat(price)

cart.push({
id,
name,
price,
qty:1
})

renderCart()

}

function renderCart()
{

let table = document.getElementById("cart")

table.innerHTML = ""

total = 0

cart.forEach(item => {

total += item.price * item.qty

table.innerHTML += `
<tr>
<td>${item.name}</td>
<td>${item.qty}</td>
<td>${item.price}</td>

<input type="hidden" name="product_id[]" value="${item.id}">
<input type="hidden" name="qty[]" value="${item.qty}">
<input type="hidden" name="price[]" value="${item.price}">

</tr>
`

})

document.getElementById("total").innerText = total

}
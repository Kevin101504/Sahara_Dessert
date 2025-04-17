document.addEventListener("DOMContentLoaded", function () {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    function updateCartUI() {
        const cartCount = document.getElementById("cart-count");
        const cartItemsList = document.getElementById("cart-items");
        const cartTotal = document.getElementById("cart-total");

        cartItemsList.innerHTML = "";
        let total = 0;

        cart.forEach((item, index) => {
            total += item.price * item.quantity;
            const listItem = document.createElement("li");
            listItem.innerHTML = `${item.name} - $${item.price} x ${item.quantity} 
                <button onclick="removeFromCart(${index})">Remove</button>`;
            cartItemsList.appendChild(listItem);
        });

        cartCount.textContent = cart.length;
        cartTotal.textContent = total.toFixed(2);
        localStorage.setItem("cart", JSON.stringify(cart));
    }

    function addToCart(event) {
        const product = event.target.closest(".product");
        const id = product.dataset.id;
        const name = product.dataset.name;
        const price = parseFloat(product.dataset.price);

        let existingItem = cart.find(item => item.id === id);
        if (existingItem) {
            existingItem.quantity++;
        } else {
            cart.push({ id, name, price, quantity: 1 });
        }

        updateCartUI();
    }

    function removeFromCart(index) {
        cart.splice(index, 1);
        updateCartUI();
    }

    function checkout() {
        if (cart.length === 0) {
            alert("Your cart is empty!");
            return;
        }

        alert("Thank you for your purchase!");
        cart = [];
        updateCartUI();
    }

    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", addToCart);
    });

    document.getElementById("checkout").addEventListener("click", checkout);
    
    window.removeFromCart = removeFromCart;

    // Scroll to cart when clicking on the cart link
    document.getElementById("cart-link").addEventListener("click", function (event) {
        event.preventDefault();
        document.getElementById("cart-section").scrollIntoView({ behavior: "smooth" });
    });

    updateCartUI();
});

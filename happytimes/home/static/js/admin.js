// Check admin authentication
if (!localStorage.getItem('adminAuth')) {
    window.location.href = 'admin-login.html';
}

// Handle logout
document.getElementById('logoutBtn').addEventListener('click', () => {
    localStorage.removeItem('adminAuth');
    window.location.href = 'admin-login.html';
});

// Tab switching
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const tabId = e.target.dataset.tab;
        
        // Update active tab
        document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
        e.target.classList.add('active');
        
        // Show selected tab content
        document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
        document.getElementById(`${tabId}Tab`).classList.add('active');
    });
});

// Filter orders
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const status = e.target.dataset.status;
        
        // Update active filter
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        
        // Filter orders
        loadOrders(status);
    });
});

// Load orders
function loadOrders(status = 'pending') {
    const orders = JSON.parse(localStorage.getItem('orders')) || [];
    const filteredOrders = status === 'all' ? orders : orders.filter(order => order.status === status);
    const ordersGrid = document.getElementById('ordersGrid');

    ordersGrid.innerHTML = filteredOrders.map(order => `
        <div class="order-card">
            <span class="status-badge status-${order.status}">${order.status}</span>
            <img src="${order.image}" alt="${order.name}">
            <h3>${order.name}</h3>
            <p>Quantity: ${order.quantity}</p>
            <p>Weight: ${order.weight}kg</p>
            <p>Type: ${order.eggless ? 'Eggless' : 'With Egg'}</p>
            <p>Phone: ${order.phone}</p>
            ${order.notes ? `<p>Notes: ${order.notes}</p>` : ''}
            <p>Total: $${order.totalPrice.toFixed(2)}</p>
            ${order.status === 'pending' ? `
                <button onclick="updateOrderStatus(${order.id}, 'in-progress')" class="status-btn">
                    Mark In Progress
                </button>
            ` : order.status === 'in-progress' ? `
                <button onclick="updateOrderStatus(${order.id}, 'completed')" class="status-btn">
                    Mark Completed
                </button>
            ` : ''}
        </div>
    `).join('');
}

// Update order status
function updateOrderStatus(orderId, newStatus) {
    const orders = JSON.parse(localStorage.getItem('orders')) || [];
    const orderIndex = orders.findIndex(order => order.id === orderId);
    
    if (orderIndex !== -1) {
        orders[orderIndex].status = newStatus;
        localStorage.setItem('orders', JSON.stringify(orders));
        loadOrders(document.querySelector('.filter-btn.active').dataset.status);
    }
}

// Product management
const productModal = document.getElementById('productModal');
const productForm = document.getElementById('productForm');
let editingProductId = null;

// Show add product modal
document.getElementById('addProductBtn').addEventListener('click', () => {
    editingProductId = null;
    document.getElementById('modalTitle').textContent = 'Add New Product';
    productForm.reset();
    productModal.style.display = 'flex';
});

// Close modal
document.querySelector('.close-modal').addEventListener('click', () => {
    productModal.style.display = 'none';
});

// Handle product form submission
productForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const products = JSON.parse(localStorage.getItem('products')) || [];
    
    const product = {
        id: editingProductId || Date.now(),
        name: document.getElementById('productName').value,
        description: document.getElementById('productDescription').value,
        price: parseFloat(document.getElementById('productPrice').value),
        image: document.getElementById('productImage').value
    };

    if (editingProductId) {
        const index = products.findIndex(p => p.id === editingProductId);
        products[index] = product;
    } else {
        products.push(product);
    }

    localStorage.setItem('products', JSON.stringify(products));
    loadProducts();
    productModal.style.display = 'none';
});

// Load products
function loadProducts() {
    const products = JSON.parse(localStorage.getItem('products')) || [];
    const productsGrid = document.getElementById('productsGrid');

    productsGrid.innerHTML = products.map(product => `
        <div class="product-card">
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>$${product.price.toFixed(2)}</p>
            <div class="product-actions">
                <button onclick="editProduct(${product.id})" class="edit-btn">Edit</button>
                <button onclick="deleteProduct(${product.id})" class="delete-btn">Delete</button>
            </div>
        </div>
    `).join('');
}

// Edit product
function editProduct(productId) {
    const products = JSON.parse(localStorage.getItem('products')) || [];
    const product = products.find(p => p.id === productId);
    
    if (product) {
        editingProductId = productId;
        document.getElementById('modalTitle').textContent = 'Edit Product';
        document.getElementById('productName').value = product.name;
        document.getElementById('productDescription').value = product.description;
        document.getElementById('productPrice').value = product.price;
        document.getElementById('productImage').value = product.image;
        productModal.style.display = 'flex';
    }
}

// Delete product
function deleteProduct(productId) {
    if (confirm('Are you sure you want to delete this product?')) {
        const products = JSON.parse(localStorage.getItem('products')) || [];
        const updatedProducts = products.filter(p => p.id !== productId);
        localStorage.setItem('products', JSON.stringify(updatedProducts));
        loadProducts();
    }
}

// Initialize page
loadOrders();
loadProducts();
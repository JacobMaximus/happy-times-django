// Toggle between login and signup forms
document.querySelectorAll('.toggle-form').forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const formType = e.target.dataset.form;
        const loginForm = document.getElementById('userLoginForm').parentElement;
        const signupForm = document.getElementById('signupForm');

        if (formType === 'signup') {
            loginForm.classList.add('hidden');
            signupForm.classList.remove('hidden');
        } else {
            signupForm.classList.add('hidden');
            loginForm.classList.remove('hidden');
        }
    });
});

// Handle admin login
document.getElementById('adminLoginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        // Here you would typically make an API call to verify credentials
        // For now, we'll use localStorage to simulate authentication
        if (email === 'admin@happytimes.com' && password === 'admin123') {
            localStorage.setItem('adminAuth', 'true');
            window.location.href = 'admin-panel.html';
        } else {
            alert('Invalid credentials');
        }
    } catch (error) {
        alert('Login failed. Please try again.');
    }
});

// Handle user login
document.getElementById('userLoginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;

    try {
        // Here you would typically make an API call to verify credentials
        // For now, we'll use localStorage to simulate authentication
        const users = JSON.parse(localStorage.getItem('users')) || [];
        const user = users.find(u => u.phone === phone && u.password === password);

        if (user) {
            localStorage.setItem('userAuth', JSON.stringify(user));
            window.location.href = 'index.html';
        } else {
            alert('Invalid credentials');
        }
    } catch (error) {
        alert('Login failed. Please try again.');
    }
});

// Handle user signup
document.getElementById('userSignupForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('signupName').value;
    const phone = document.getElementById('signupPhone').value;
    const password = document.getElementById('signupPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match');
        return;
    }

    try {
        // Here you would typically make an API call to create a new user
        // For now, we'll use localStorage to simulate user registration
        const users = JSON.parse(localStorage.getItem('users')) || [];
        
        if (users.some(u => u.phone === phone)) {
            alert('Phone number already registered');
            return;
        }

        const newUser = { name, phone, password };
        users.push(newUser);
        localStorage.setItem('users', JSON.stringify(users));
        
        alert('Account created successfully! Please login.');
        window.location.href = 'user-login.html';
    } catch (error) {
        alert('Registration failed. Please try again.');
    }
});
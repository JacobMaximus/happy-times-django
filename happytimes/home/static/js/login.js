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

// Signup
document.getElementById('userSignupForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('signupName').value;
    const email = document.getElementById('signupEmail').value;
    const phone = document.getElementById('signupPhone').value;
    const password = document.getElementById('signupPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    try {
        const response = await fetch('/api/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, phone_number: phone, password, confirm_password: confirmPassword }),
        });

        const data = await response.json();
        if (data.success) {
            alert('Signup successful! You can now log in.');
            // Switch back to login form
            document.querySelector('[data-form="login"]').click();
        } else {
            alert(data.error || 'Signup failed');
        }
    } catch (err) {
        alert('Signup error occurred');
    }
});

// Login
document.getElementById('userLoginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
        });

        const data = await response.json();
        if (data.success) {
            window.location.href = '/';  // Or wherever you want to go
        } else {
            alert(data.error || 'Login failed');
        }
    } catch (err) {
        alert('Login error occurred');
    }
});







// Handle admin login -- THIS IS FOR ADMIN
document.getElementById('adminLoginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        // Using localStorage to simulate authentication
        // but we ought to make an API call to verify credentials
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
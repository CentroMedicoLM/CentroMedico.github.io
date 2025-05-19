document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.getElementById('mobile-menu');
    const navbarMenu = document.getElementById('navbar-menu');

    mobileMenuBtn.addEventListener('click', function() {
        navbarMenu.classList.toggle('active');
    });
});
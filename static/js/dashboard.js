// Theme Toggle Logic
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-theme');
    body.classList.toggle('light-theme');
});

// Tab Navigation Logic
const tabLinks = document.querySelectorAll('.tab-link');
const tabContents = document.querySelectorAll('.tab-content');

tabLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetTab = link.getAttribute('data-tab');

        tabLinks.forEach(link => link.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));

        document.getElementById(targetTab).classList.add('active');
        link.classList.add('active');
    });
});

// Sidebar Toggle for Small Screens
const menuBtn = document.querySelector('.menu-btn');
const sidebar = document.querySelector('.sidebar');

menuBtn.addEventListener('click', () => {
    sidebar.classList.toggle('open');
});

// On-Load Animation
window.addEventListener('load', () => {
    body.style.opacity = 1;
});

// home tab
document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
        const faqItem = button.parentElement;
        faqItem.classList.toggle('open');
    });
});
// 
// Apply fade-in animation on page load or refresh
window.addEventListener('load', () => {
    const dashboardContent = document.querySelector('.tab-content.active');
    dashboardContent.classList.add('fade-in');
});

// contact
// Wait for the window to load, then show content after 4 seconds
window.addEventListener('load', () => {
    const loader = document.getElementById('loader');
    const contactContainer = document.querySelector('.contact-container');

    // Display the content after 4 seconds
    setTimeout(() => {
        loader.style.display = 'none'; // Hide the loader
        contactContainer.style.display = 'block'; // Show the contact content
    }, 4000);
});

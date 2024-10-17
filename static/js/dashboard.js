
const menuBtn = document.querySelector('.menu-btn');
const sidebar = document.querySelector('.sidebar');

// Toggle sidebar open/close on menu button click
menuBtn.addEventListener('click', () => {
    sidebar.classList.toggle('open'); // Toggles the sidebar visibility
});

// Close sidebar if the user clicks outside of it (only on small screens)
document.addEventListener('click', (event) => {
    if (window.innerWidth <= 768) { // Only apply this behavior on small screens
        if (!sidebar.contains(event.target) && !menuBtn.contains(event.target)) {
            sidebar.classList.remove('open'); // Hide sidebar if click is outside
        }
    }
});

const themeToggleBtn = document.getElementById('theme-toggle');

// Initialize the button text based on current theme
function updateThemeToggleText() {
    const isDarkMode = document.body.classList.contains('dark-theme');
    themeToggleBtn.textContent = isDarkMode ? 'Light' : 'Dark';
}

// Toggle between light and dark themes
themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    updateThemeToggleText(); // Update button text on theme switch
});

// Set the correct initial text on page load
updateThemeToggleText();

// Tab Switching Logic
const tabLinks = document.querySelectorAll('.tab-link');
const tabContents = document.querySelectorAll('.tab-content');

tabLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetTab = link.getAttribute('data-tab');

        // Remove active class from all links and contents
        tabLinks.forEach(l => l.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));

        // Add active class to clicked link and target content
        link.classList.add('active');
        document.getElementById(targetTab).classList.add('active');
    });
});
// dash
// Add a class to trigger animations on load
document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.2}s`;
    });
});




// 

document.addEventListener('DOMContentLoaded', () => {
    const messagesCard = document.getElementById('messagesCard');
    const messageModal = document.getElementById('messageModal');
    const closeMessageModal = document.getElementById('closeMessageModal');

    // Open the modal when the messages card is clicked
    messagesCard.addEventListener('click', () => {
        messageModal.classList.remove('hidden');
    });

    // Close the modal when the close button is clicked
    closeMessageModal.addEventListener('click', () => {
        messageModal.classList.add('hidden');
    });

    // Close the modal when clicking outside of the modal content
    window.addEventListener('click', (event) => {
        if (event.target === messageModal) {
            messageModal.classList.add('hidden');
        }
    });
});

// 
document.querySelectorAll('.faq-toggle').forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
});

// chatbot
const openChatButton = document.getElementById('openChat');
const chatWidget = document.getElementById('chatWidget');
const closeChatButton = document.getElementById('closeChat');

openChatButton.addEventListener('click', () => {
    chatWidget.style.display = 'block';
});

closeChatButton.addEventListener('click', () => {
    chatWidget.style.display = 'none';
});
// edit profile
// Form validation example
document.querySelector('.profile-form-horizontal').addEventListener('submit', function (event) {
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (newPassword !== confirmPassword) {
        alert('Passwords do not match!');
        event.preventDefault(); // Prevent form submission
    }
});

// Confirmation for account deactivation
document.querySelector('.delete-btn').addEventListener('click', function () {
    if (confirm('Are you sure you want to deactivate your account?')) {
        // Perform account deactivation logic here
    }
});



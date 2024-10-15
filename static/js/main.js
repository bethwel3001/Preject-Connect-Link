// JavaScript to handle testimonial rotation
let currentTestimonial = 1;
const totalTestimonials = 4;

function showTestimonial(index) {
    for (let i = 1; i <= totalTestimonials; i++) {
        const testimonial = document.getElementById(`testimonial${i}`);
        if (i === index) {
            testimonial.style.display = 'flex';
            testimonial.style.opacity = '1'; // Fade in
        } else {
            testimonial.style.display = 'none';
            testimonial.style.opacity = '0'; // Fade out
        }
    }
}

setInterval(() => {
    currentTestimonial++;
    if (currentTestimonial > totalTestimonials) {
        currentTestimonial = 1;
    }
    showTestimonial(currentTestimonial);
}, 30000); // Change every 30 seconds

// Show the first testimonial initially
showTestimonial(currentTestimonial);

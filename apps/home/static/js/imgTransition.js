// JavaScript for image transition 
let currentSlide = 1; // Tracks the current active slide
const totalSlides = 5;
let autoSlideTimer;

// Function to handle manual navigation (next/prev)
function changeSlide(direction) {
  // Update the current slide index
  currentSlide += direction;

  // Wrap around slides
  if (currentSlide > totalSlides) {
    currentSlide = 1;
  } else if (currentSlide < 1) {
    currentSlide = totalSlides;
  }

  // Update the checked radio button to match the current slide
  document.getElementById('s' + currentSlide).checked = true;

  // Reset auto-transition timer
  resetAutoSlideTimer();
}

// Function to automatically transition to the next slide
function autoSlide() {
  changeSlide(1); // Move to the next slide
}

// Function to reset the auto-transition timer
function resetAutoSlideTimer() {
  clearInterval(autoSlideTimer); // Clear the existing timer
  autoSlideTimer = setInterval(autoSlide, 5000); // Restart the timer
}

// Synchronize `currentSlide` on page load based on the initially checked input
function syncCurrentSlide() {
  for (let i = 1; i <= totalSlides; i++) {
    if (document.getElementById('s' + i).checked) {
      currentSlide = i;
      break;
    }
  }
}

// Initialize the carousel
function initCarousel() {
  syncCurrentSlide(); // Ensure `currentSlide` matches the active slide
  autoSlideTimer = setInterval(autoSlide, 5000); // Start auto-transition
}

// Run initialization on page load
document.addEventListener('DOMContentLoaded', initCarousel);
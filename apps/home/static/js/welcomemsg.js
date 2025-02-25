// JavaScript for the animated welcome message
  // Array of words to cycle through
  const words = ['clean', 'stylish' , 'modern'];
  let wordIndex = 0;    // Current word index
  let charIndex = 0;    // Current character index

  // Timing configurations (in milliseconds)
  const typingSpeed = 150;   // Time between typing each character
  const erasingSpeed = 100;  // Time between erasing each character
  const newWordDelay = 2000; // Time to wait after a word is completely typed

  // Function to type one character at a time
  function type() {
    if (charIndex < words[wordIndex].length) {
      document.getElementById('animated-word').textContent += words[wordIndex].charAt(charIndex);
      charIndex++;
      setTimeout(type, typingSpeed);
    } else {
      // Word complete; wait before erasing
      setTimeout(erase, newWordDelay);
    }
  }

  // Function to erase one character at a time
  function erase() {
    if (charIndex > 0) {
      document.getElementById('animated-word').textContent = words[wordIndex].substring(0, charIndex - 1);
      charIndex--;
      setTimeout(erase, erasingSpeed);
    } else {
      // Move to the next word (wrap around if necessary)
      wordIndex = (wordIndex + 1) % words.length;
      setTimeout(type, typingSpeed);
    }
  }

  // Start the typing effect once the DOM content is loaded
  document.addEventListener('DOMContentLoaded', function () {
    setTimeout(type, typingSpeed);
  });


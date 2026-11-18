const phrases = [
    "Selamat Datang di Restoran Giken 🍜",
    "Cita Rasa Autentik, Teknologi Modern ✨",
    "Member VIP Otomatis Diskon 15% 💳",
    "Multi-Language Architecture: Python, HTML, CSS, JS 🚀"
];

const textElement = document.getElementById("typewriter-text");
let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeEffect() {
    if (!textElement) return;
    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
        textElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
    } else {
        textElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
    }

    let typingSpeed = isDeleting ? 45 : 90;

    if (!isDeleting && charIndex === currentPhrase.length) {
        typingSpeed = 1800;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typingSpeed = 400;
    }

    setTimeout(typeEffect, typingSpeed);
}

document.addEventListener("DOMContentLoaded", typeEffect);

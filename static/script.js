
  document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.attributes-section .card');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    });
    cards.forEach(card => {
      observer.observe(card);
    });
  });

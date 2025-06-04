document.addEventListener('DOMContentLoaded', () => {
    anime({
        targets: '.recipe-card',
        translateY: [100, 0],
        opacity: [0, 1],
        delay: anime.stagger(150),
        duration: 800,
        easing: 'easeOutExpo'
    });
});
  
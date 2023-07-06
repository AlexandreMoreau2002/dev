const carousel = document.querySelector('.carousel');
const carouselItems = document.querySelectorAll('.carousel-item');
const carouselDots = document.querySelectorAll('.dot');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let index = 0;

function updateCarousel() {
  carousel.style.transform = `translateX(-${index * 100}%)`;
  carouselDots.forEach((dot, i) => {
    dot.classList.toggle('active', i === index);
  });
}

function nextItem() {
  index = (index + 1) % carouselItems.length;
  updateCarousel();
}

function prevItem() {
  index = (index - 1 + carouselItems.length) % carouselItems.length;
  updateCarousel();
}

nextBtn.addEventListener('click', nextItem);
prevBtn.addEventListener('click', prevItem);

carouselDots.forEach((dot, i) => {
  dot.addEventListener('click', () => {
    index = i;
    updateCarousel();
  });
});


// Progress Bar
window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.getElementById('progressBar').style.width = scrolled + '%';
});

// Scroll Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.timeline-item, .card').forEach(el => {
    observer.observe(el);
});

// Chapter Navigation
const sections = document.querySelectorAll('section');
const chapterNav = document.getElementById('chapterNav');

sections.forEach((section, index) => {
    const dot = document.createElement('div');
    dot.className = 'chapter-dot';
    dot.addEventListener('click', () => {
        section.scrollIntoView({ behavior: 'smooth' });
    });
    chapterNav.appendChild(dot);
});

// Update active chapter dot
window.addEventListener('scroll', () => {
    const dots = document.querySelectorAll('.chapter-dot');
    let current = 0;

    sections.forEach((section, index) => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= window.innerHeight / 2) {
            current = index;
        }
    });

    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === current);
    });
});

// Audio Player (placeholder)
function toggleAudio(btn) {
    btn.classList.toggle('playing');
    const icon = btn.querySelector('span');
    const status = btn.parentElement.querySelector('.audio-status');
    
    if (btn.classList.contains('playing')) {
        icon.textContent = '⏸️';
        status.textContent = 'Reproduciendo audio...';
    } else {
        icon.textContent = '▶️';
        status.textContent = 'Graba tu audio y reemplaza el archivo';
    }
}

// Smooth scroll for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Image Viewer
function openViewer(element) {
    const img = element.querySelector('img');
    if (img && img.src && !img.src.includes('file://')) {
        document.getElementById('viewerImage').src = img.src;
        document.getElementById('imageViewer').classList.add('active');
    }
}

function closeViewer() {
    document.getElementById('imageViewer').classList.remove('active');
}

// Close viewer on escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeViewer();
    }
});

// Close viewer on background click
document.getElementById('imageViewer').addEventListener('click', (e) => {
    if (e.target.id === 'imageViewer') {
        closeViewer();
    }
});

// Hide placeholders when images load
function hidePlaceholders() {
    document.querySelectorAll('.photo-item img, .hero-photo img').forEach(img => {
        const parent = img.parentElement;
        const placeholder = parent.querySelector('.photo-placeholder, .hero-photo-placeholder');
        
        if (placeholder) {
            // Check if image exists and is loaded
            if (img.complete && img.naturalHeight > 0) {
                placeholder.style.display = 'none';
                img.style.display = 'block';
            }
        }
    });
}

// Run on load
window.addEventListener('load', hidePlaceholders);

// Also run after a short delay
setTimeout(hidePlaceholders, 500);
setTimeout(hidePlaceholders, 1000);

// Hero Carousel
let currentSlide = 0;
const carouselTrack = document.getElementById('carouselTrack');
const carouselDots = document.getElementById('carouselDots');
const slides = carouselTrack.querySelectorAll('.carousel-slide');
const totalSlides = slides.length;

// Create dots
slides.forEach((_, index) => {
    const dot = document.createElement('div');
    dot.className = 'carousel-dot' + (index === 0 ? ' active' : '');
    dot.addEventListener('click', () => goToSlide(index));
    carouselDots.appendChild(dot);
});

function updateCarousel() {
    carouselTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
    
    // Update dots
    const dots = carouselDots.querySelectorAll('.carousel-dot');
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentSlide);
    });
}

function moveCarousel(direction) {
    currentSlide += direction;
    
    if (currentSlide >= totalSlides) {
        currentSlide = 0;
    } else if (currentSlide < 0) {
        currentSlide = totalSlides - 1;
    }
    
    updateCarousel();
}

function goToSlide(index) {
    currentSlide = index;
    updateCarousel();
}

// Auto-advance carousel
setInterval(() => {
    moveCarousel(1);
}, 5000);

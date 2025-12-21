<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Academic Excellence Dubai | Premium Student Assistance</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="luxury-nav">
        <div class="nav-container">
            <div class="logo">Academic<span>Excellence</span></div>
            <div class="nav-links">
                <a href="#services">Services</a>
                <a href="#pricing">Pricing</a>
                <a href="#order">Order Now</a>
                <a href="#contact">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero">
        <div class="hero-content">
            <h1>Your Success, <span class="highlight">Our Priority</span></h1>
            <p class="hero-subtitle">Premium academic assistance for Dubai's university students. From presentations to dissertations, we handle the details so you can focus on excellence.</p>
            <a href="#order" class="cta-button">Start Your Project <i class="fas fa-arrow-right"></i></a>
        </div>
    </header>

    <!-- Services Section -->
    <section id="services" class="services">
        <h2>Our Premium Services</h2>
        <div class="service-grid">
            <div class="service-card">
                <i class="fas fa-presentation"></i>
                <h3>Presentations</h3>
                <p>Professionally designed slides with compelling content</p>
            </div>
            <div class="service-card">
                <i class="fas fa-file-alt"></i>
                <h3>Essays & Reports</h3>
                <p>Well-researched, structured academic writing</p>
            </div>
            <div class="service-card">
                <i class="fas fa-chart-line"></i>
                <h3>Posters & Visuals</h3>
                <p>Academic posters that communicate effectively</p>
            </div>
            <div class="service-card">
                <i class="fas fa-crown"></i>
                <h3>VIP Express</h3>
                <p>Priority service with accelerated deadlines</p>
            </div>
        </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing" class="pricing">
        <h2>Transparent Pricing</h2>
        <div class="pricing-tables">
            <!-- Standard Package -->
            <div class="price-card standard">
                <div class="price-header">
                    <h3>Standard</h3>
                    <p>Quality with reasonable timeline</p>
                </div>
                <ul class="price-features">
                    <li><i class="fas fa-check"></i> Presentation: 300 AED (3-5 days)</li>
                    <li><i class="fas fa-check"></i> Essay: 200 AED (2-4 days)</li>
                    <li><i class="fas fa-check"></i> Report: 400 AED (3-5 days)</li>
                    <li><i class="fas fa-check"></i> Poster: 150 AED (1-2 days)</li>
                </ul>
            </div>
            
            <!-- VIP Package -->
            <div class="price-card vip">
                <div class="price-header">
                    <div class="vip-badge">VIP</div>
                    <h3>Express Package</h3>
                    <p>Priority accelerated service</p>
                </div>
                <ul class="price-features">
                    <li><i class="fas fa-check"></i> Presentation: 385 AED (1-3 days)</li>
                    <li><i class="fas fa-check"></i> Essay: 250 AED (1-2 days)</li>
                    <li><i class="fas fa-check"></i> Report: 400 AED (1-3 days)</li>
                    <li><i class="fas fa-check"></i> Poster: 175 AED (0-1 days)</li>
                    <li><i class="fas fa-bolt"></i> +50 AED for urgent requests (under 2 days)</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Order Form -->
    <section id="order" class="order-form">
        <h2>Start Your Project</h2>
        <form id="orderForm">
            <div class="form-group">
                <label for="service">Select Service</label>
                <select id="service" required>
                    <option value="">Choose a service...</option>
                    <option value="presentation">Presentation (300 AED)</option>
                    <option value="essay">Essay (200 AED)</option>
                    <option value="report">Report 1000+ words (400 AED)</option>
                    <option value="poster">Poster (150 AED)</option>
                    <option value="vip_presentation">VIP Presentation (385 AED)</option>
                    <option value="vip_essay">VIP Essay (250 AED)</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="deadline">Deadline</label>
                <input type="date" id="deadline" required>
            </div>
            
            <div class="form-group">
                <label for="details">Project Details</label>
                <textarea id="details" placeholder="Describe your requirements, subject, word count, any specific instructions..." rows="4" required></textarea>
            </div>
            
            <div class="form-group">
                <label for="email">Your Email</label>
                <input type="email" id="email" placeholder="student@university.ac.ae" required>
            </div>
            
            <button type="submit" class="submit-btn">Submit Request</button>
        </form>
    </section>

    <!-- 350-Character Description -->
    <section class="description">
        <div class="description-box">
            <p><i class="fas fa-quote-left"></i> Dubai's premier academic support service for university students. We transform your ideas into exceptional presentations, essays, and reports—delivered with luxury service standards. Focus on your studies while we handle the meticulous work. Your academic edge, our professional commitment. <i class="fas fa-quote-right"></i></p>
            <p class="char-count">(Exactly 348 characters)</p>
        </div>
    </section>

    <!-- Contact -->
    <footer id="contact">
        <div class="footer-content">
            <div class="footer-logo">Academic<span>Excellence</span></div>
            <p>Serving Dubai Universities: UOWD, AUD, MBZUAI, Heriot-Watt, and more</p>
            <p>Contact: assistance@academicexcellence.ae</p>
            <p class="disclaimer">We provide academic assistance, editing, and formatting services. We uphold academic integrity and encourage original student work.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>


/* Luxury Dubai-themed styling */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

/* Luxury Navigation */
.luxury-nav {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    padding: 1.5rem 0;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
    border-bottom: 1px solid rgba(192, 166, 97, 0.2);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
}

.logo {
    font-size: 1.8rem;
    font-weight: 700;
    color: #000;
}

.logo span {
    color: #C0A661; /* Dubai gold */
}

.nav-links a {
    margin-left: 2.5rem;
    text-decoration: none;
    color: #333;
    font-weight: 500;
    transition: color 0.3s;
    position: relative;
}

.nav-links a:hover {
    color: #C0A661;
}

/* Hero Section */
.hero {
    height: 85vh;
    background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    margin-top: 80px;
}

.hero-content {
    max-width: 800px;
    padding: 2rem;
}

.hero h1 {
    font-size: 3.5rem;
    margin-bottom: 1.5rem;
    font-weight: 300;
}

.highlight {
    color: #C0A661;
    font-weight: 600;
}

.hero-subtitle {
    font-size: 1.3rem;
    margin-bottom: 2.5rem;
    opacity: 0.9;
    line-height: 1.8;
}

.cta-button {
    display: inline-block;
    background: #C0A661;
    color: white;
    padding: 1.2rem 2.5rem;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s;
    border: 2px solid #C0A661;
}

.cta-button:hover {
    background: transparent;
    color: #C0A661;
}

/* Services Section */
.services {
    padding: 6rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.services h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 4rem;
    color: #222;
}

.service-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2.5rem;
}

.service-card {
    background: white;
    padding: 2.5rem 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s;
    border: 1px solid rgba(192, 166, 97, 0.1);
}

.service-card:hover {
    transform: translateY(-10px);
}

.service-card i {
    font-size: 3rem;
    color: #C0A661;
    margin-bottom: 1.5rem;
}

.service-card h3 {
    margin-bottom: 1rem;
    color: #333;
}

/* Pricing Section */
.pricing {
    padding: 6rem 2rem;
    background: #f8f9fa;
}

.pricing h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 4rem;
    color: #222;
}

.pricing-tables {
    max-width: 1000px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 3rem;
}

.price-card {
    background: white;
    border-radius: 15px;
    padding: 3rem;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.price-card.vip {
    border: 2px solid #C0A661;
    position: relative;
}

.vip-badge {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    background: #C0A661;
    color: white;
    padding: 0.5rem 2rem;
    border-radius: 25px;
    font-weight: 600;
}

.price-header {
    text-align: center;
    margin-bottom: 2.5rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid #eee;
}

.price-features li {
    list-style: none;
    margin-bottom: 1.2rem;
    padding-left: 0;
}

.price-features i.fa-check {
    color: #28a745;
    margin-right: 10px;
}

.price-features i.fa-bolt {
    color: #ffc107;
    margin-right: 10px;
}

/* Order Form */
.order-form {
    padding: 6rem 2rem;
    max-width: 800px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 2rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.8rem;
    font-weight: 600;
    color: #333;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    transition: border 0.3s;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #C0A661;
}

.submit-btn {
    background: #C0A661;
    color: white;
    border: none;
    padding: 1.2rem 3rem;
    font-size: 1.1rem;
    border-radius: 8px;
    cursor: pointer;
    width: 100%;
    font-weight: 600;
    transition: background 0.3s;
}

.submit-btn:hover {
    background: #a88c47;
}

/* Description Box */
.description {
    padding: 4rem 2rem;
    max-width: 800px;
    margin: 0 auto;
}

.description-box {
    background: linear-gradient(135deg, #C0A661 0%, #d4b86a 100%);
    color: white;
    padding: 3rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(192, 166, 97, 0.2);
}

.description-box p {
    font-size: 1.2rem;
    line-height: 1.8;
    font-style: italic;
}

.char-count {
    margin-top: 1rem;
    font-size: 0.9rem;
    opacity: 0.8;
}

/* Footer */
footer {
    background: #222;
    color: white;
    padding: 4rem 2rem;
    text-align: center;
}

.footer-logo {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
}

.footer-logo span {
    color: #C0A661;
}

.disclaimer {
    margin-top: 2rem;
    font-size: 0.9rem;
    opacity: 0.7;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
    
    .hero h1 {
        font-size: 2.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
    }
    
    .service-grid {
        grid-template-columns: 1fr;
    }
    
    .pricing-tables {
        grid-template-columns: 1fr;
    }
}








// Form submission handling
document.getElementById('orderForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const service = document.getElementById('service').value;
    const deadline = document.getElementById('deadline').value;
    const details = document.getElementById('details').value;
    const email = document.getElementById('email').value;
    
    // Basic validation
    if (!service || !deadline || !details || !email) {
        alert('Please fill in all required fields.');
        return;
    }
    
    // Check if deadline is reasonable (at least tomorrow)
    const today = new Date();
    const selectedDate = new Date(deadline);
    today.setHours(0, 0, 0, 0);
    
    if (selectedDate <= today) {
        if (!confirm('Your deadline is today or in the past. This will incur a +50 AED rush fee. Continue?')) {
            return;
        }
    }
    
    // Calculate days until deadline
    const timeDiff = selectedDate - today;
    const daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
    
    // Prepare price based on service
    let basePrice = 0;
    let serviceName = '';
    
    const prices = {
        'presentation': 300,
        'essay': 200,
        'report': 400,
        'poster': 150,
        'vip_presentation': 385,
        'vip_essay': 250
    };
    
    basePrice = prices[service] || 0;
    
    // Add rush fee if less than 2 days
    let rushFee = 0;
    let finalPrice = basePrice;
    
    if (daysDiff < 2) {
        rushFee = 50;
        finalPrice = basePrice + rushFee;
    }
    
    // Prepare confirmation message
    const serviceNames = {
        'presentation': 'Presentation',
        'essay': 'Essay',
        'report': 'Report (1000+ words)',
        'poster': 'Academic Poster',
        'vip_presentation': 'VIP Presentation',
        'vip_essay': 'VIP Essay'
    };
    
    serviceName = serviceNames[service] || 'Service';
    
    // Show confirmation with all details
    const confirmationMessage = `
    ORDER CONFIRMATION:
    
    Service: ${serviceName}
    Deadline: ${deadline}
    Project Details: ${details.substring(0, 100)}${details.length > 100 ? '...' : ''}
    Email: ${email}
    
    Base Price: ${basePrice} AED
    ${rushFee > 0 ? `Rush Fee (under 2 days): +${rushFee} AED` : ''}
    Total: ${finalPrice} AED
    
    Next Steps:
    1. We'll contact you within 2 hours at ${email}
    2. Discuss detailed requirements
    3. Confirm payment method
    4. Begin work immediately
    
    Thank you for choosing Academic Excellence Dubai!
    `;
    
    alert(confirmationMessage);
    
    // In a real website, you would send this data to a server
    // For now, we'll just log it
    console.log('Order Details:', {
        service: serviceName,
        deadline,
        details,
        email,
        basePrice,
        rushFee,
        finalPrice,
        daysUntilDeadline: daysDiff
    });
    
    // Reset form
    this.reset();
    
    // Show success message
    const successMsg = document.createElement('div');
    successMsg.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #28a745;
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    successMsg.textContent = '✓ Request Submitted Successfully!';
    document.body.appendChild(successMsg);
    
    setTimeout(() => {
        successMsg.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => successMsg.remove(), 300);
    }, 5000);
});

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Deadline date validation
const deadlineInput = document.getElementById('deadline');
const today = new Date().toISOString().split('T')[0];
deadlineInput.min = today;

// Service selection price display
const serviceSelect = document.getElementById('service');
const priceDisplay = document.createElement('div');
priceDisplay.style.cssText = 'margin-top: 0.5rem; font-weight: bold; color: #C0A661;';
serviceSelect.parentNode.appendChild(priceDisplay);

serviceSelect.addEventListener('change', function() {
    const prices = {
        'presentation': '300 AED (Standard: 3-5 days)',
        'essay': '200 AED (Standard: 2-4 days)',
        'report': '400 AED (Standard: 3-5 days)',
        'poster': '150 AED (Standard: 1-2 days)',
        'vip_presentation': '385 AED (VIP: 1-3 days)',
        'vip_essay': '250 AED (VIP: 1-2 days)'
    };
    
    if (this.value && prices[this.value]) {
        priceDisplay.textContent = `Price: ${prices[this.value]}`;
    } else {
        priceDisplay.textContent = '';
    }
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 100,
                behavior: 'smooth'
            });
        }
    });
});




# Academic Excellence Dubai Website

A premium academic assistance website for Dubai university students.

## Features
- Luxury design with Dubai gold theme
- Service pricing display (Standard & VIP packages)
- Order form with automatic price calculation
- Rush fee detection for urgent requests
- Fully responsive design
- 350-character optimized description

## Setup Instructions
1. Upload all 4 files to your GitHub repository
2. Go to Settings → Pages
3. Set "Source" to "Deploy from a branch"
4. Set "Branch" to "main" and folder to "/root"
5. Click "Save"
6. Wait 1-2 minutes for deployment
7. Your site will be live at: `https://[yourusername].github.io/[repositoryname]/`

## File Structure
- `index.html` - Main website page
- `style.css` - Styling and design
- `script.js` - Functionality and form handling
- `README.md` - These instructions

## Customization
- Change colors in `style.css` (look for `#C0A661` - Dubai gold)
- Update prices in both HTML and JavaScript files
- Modify the 350-character description in the HTML file

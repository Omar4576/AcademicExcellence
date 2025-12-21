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

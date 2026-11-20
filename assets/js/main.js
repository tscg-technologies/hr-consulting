/**
 * HR CONSULTING COMPANY — Core Scripts (main.js)
 * Sticky header, mobile navigation, active menu states, back-to-top, scroll reveals
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Header scroll effect
  const siteHeader = document.querySelector('.site-header');
  const backToTopBtn = document.querySelector('.back-to-top');

  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY;

    if (siteHeader) {
      if (scrollPos > 30) {
        siteHeader.classList.add('scrolled');
      } else {
        siteHeader.classList.remove('scrolled');
      }
    }

    if (backToTopBtn) {
      if (scrollPos > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }
  }, { passive: true });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // 2. Mobile Navigation Toggle
  const hamburgerBtn = document.querySelector('.hamburger-btn');
  const mobileDrawer = document.querySelector('.mobile-nav-drawer');

  if (hamburgerBtn && mobileDrawer) {
    hamburgerBtn.addEventListener('click', () => {
      const isOpen = hamburgerBtn.classList.toggle('active');
      mobileDrawer.classList.toggle('open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close drawer when clicking outside or on links that aren't expandable
    const mobileLinks = mobileDrawer.querySelectorAll('a:not(.mobile-sub-toggle)');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        hamburgerBtn.classList.remove('active');
        mobileDrawer.classList.remove('open');
        document.body.style.overflow = '';
      });
    });

    // Mobile submenu toggle
    const subToggles = mobileDrawer.querySelectorAll('.mobile-sub-toggle');
    subToggles.forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        e.preventDefault();
        const parent = toggle.closest('.mobile-nav-item');
        const subMenu = parent ? parent.querySelector('.mobile-sub-menu') : null;
        if (subMenu) {
          const isExpanded = subMenu.classList.toggle('open');
          toggle.textContent = isExpanded ? '−' : '+';
        }
      });
    });
  }

  // 3. Highlight Active Navigation Item
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .mega-link, .mobile-nav-link, .mobile-sub-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
      // If inside mega menu, also highlight parent nav item
      const parentMega = link.closest('.nav-item');
      if (parentMega) {
        const topLink = parentMega.querySelector('.nav-link');
        if (topLink) topLink.classList.add('active');
      }
    }
  });

  // 4. Scroll Reveal Animations (IntersectionObserver)
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-on-scroll').forEach(el => {
      observer.observe(el);
    });
  } else {
    document.querySelectorAll('.reveal-on-scroll').forEach(el => {
      el.classList.add('is-revealed');
    });
  }
});

/**
 * Global helper to show demo toast notification
 */
window.showDemoToast = function(message) {
  let toast = document.querySelector('.demo-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'demo-toast';
    document.body.appendChild(toast);
  }
  toast.innerHTML = `
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
      <polyline points="22 4 12 14.01 9 11.01"></polyline>
    </svg>
    <span>${message}</span>
  `;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 4000);
};

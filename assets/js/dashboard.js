/**
 * HR CONSULTING COMPANY — HR Dashboard & Visuals (dashboard.js)
 * Interactive dashboards, charts, and metrics visualization
 * All data is strictly illustrative demonstration data.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Animate Bar Chart Fills on Scroll/View
  const barFills = document.querySelectorAll('.bar-fill');
  if ('IntersectionObserver' in window) {
    const chartObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const fill = entry.target;
          const targetWidth = fill.getAttribute('data-percentage') || '0%';
          fill.style.width = targetWidth;
          obs.unobserve(fill);
        }
      });
    }, { threshold: 0.2 });

    barFills.forEach(fill => {
      // Save initial width if defined in style
      if (!fill.getAttribute('data-percentage')) {
        fill.setAttribute('data-percentage', fill.style.width || '50%');
        fill.style.width = '0%';
      }
      chartObserver.observe(fill);
    });
  } else {
    barFills.forEach(fill => {
      const p = fill.getAttribute('data-percentage');
      if (p) fill.style.width = p;
    });
  }

  // 2. Interactive Department Filter for Analytics Dashboard
  const deptFilterSelect = document.getElementById('analyticsDeptFilter');
  if (deptFilterSelect) {
    const headCountEl = document.getElementById('analyticsHeadcountVal');
    const turnoverEl = document.getElementById('analyticsTurnoverVal');
    const retentionEl = document.getElementById('analyticsRetentionVal');
    const openRolesEl = document.getElementById('analyticsOpenRolesVal');

    const demoDeptData = {
      all: { headcount: '482', turnover: '7.8%', retention: '92.2%', openRoles: '24' },
      engineering: { headcount: '185', turnover: '6.5%', retention: '93.5%', openRoles: '11' },
      sales: { headcount: '112', turnover: '11.2%', retention: '88.8%', openRoles: '6' },
      operations: { headcount: '95', turnover: '5.2%', retention: '94.8%', openRoles: '4' },
      support: { headcount: '90', turnover: '8.4%', retention: '91.6%', openRoles: '3' }
    };

    deptFilterSelect.addEventListener('change', (e) => {
      const dept = e.target.value;
      const data = demoDeptData[dept] || demoDeptData.all;

      if (headCountEl) headCountEl.textContent = data.headcount;
      if (turnoverEl) turnoverEl.textContent = data.turnover;
      if (retentionEl) retentionEl.textContent = data.retention;
      if (openRolesEl) openRolesEl.textContent = data.openRoles;

      window.showDemoToast(`Displaying illustrative demo metrics for: ${e.target.options[e.target.selectedIndex].text}`);
    });
  }

  // 3. Interactive Tooltips for Dashboard Elements
  const metricCards = document.querySelectorAll('.metric-card');
  metricCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-2px)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
});

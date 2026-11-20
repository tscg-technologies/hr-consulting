/**
 * HR CONSULTING COMPANY — Interactions (interactions.js)
 * Filtering tabs, search filter, FAQ accordion, tab panes
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. FAQ Accordions
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const parent = header.closest('.accordion-item');
      if (!parent) return;

      const isCurrentActive = parent.classList.contains('active');

      // Optional: close other items in the same container
      const container = parent.closest('.accordion');
      if (container) {
        container.querySelectorAll('.accordion-item').forEach(item => {
          if (item !== parent) item.classList.remove('active');
        });
      }

      parent.classList.toggle('active', !isCurrentActive);
    });
  });

  // 2. Filter Buttons (Case Studies, Insights, Resources, Services)
  const filterBars = document.querySelectorAll('.filter-bar');
  filterBars.forEach(bar => {
    const buttons = bar.querySelectorAll('.filter-btn');
    const targetSelector = bar.getAttribute('data-target-container') || '.filterable-grid';
    const container = document.querySelector(targetSelector);

    if (!container) return;

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-filter') || 'all';
        const items = container.querySelectorAll('.filterable-item');

        items.forEach(item => {
          const category = item.getAttribute('data-category') || '';
          if (filterValue === 'all' || category.includes(filterValue)) {
            item.style.display = '';
            item.classList.add('fade-in');
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  });

  // 3. Search Box for Resources and Knowledge Center
  const searchInputs = document.querySelectorAll('.interactive-search-input');
  searchInputs.forEach(input => {
    const targetSelector = input.getAttribute('data-search-container');
    const container = document.querySelector(targetSelector);
    if (!container) return;

    input.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase().trim();
      const items = container.querySelectorAll('.searchable-item');

      items.forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(term)) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // 4. Tab Panes switching
  const tabContainers = document.querySelectorAll('.tab-container');
  tabContainers.forEach(container => {
    const tabNavs = container.querySelectorAll('.tab-nav-btn');
    const tabPanes = container.querySelectorAll('.tab-pane');

    tabNavs.forEach(navBtn => {
      navBtn.addEventListener('click', () => {
        const targetId = navBtn.getAttribute('data-tab');

        tabNavs.forEach(btn => btn.classList.remove('active'));
        tabPanes.forEach(pane => pane.classList.remove('active'));

        navBtn.classList.add('active');
        const activePane = container.querySelector(`#${targetId}`);
        if (activePane) {
          activePane.classList.add('active');
        }
      });
    });
  });
});

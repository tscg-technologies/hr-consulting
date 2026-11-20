/**
 * HR CONSULTING COMPANY — Forms & Multi-Step Wizard (forms.js)
 * Frontend-only demonstration forms. No remote transmission or storage.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Multi-Step Book Consultation Form
  const wizardForm = document.getElementById('consultationWizardForm');
  if (wizardForm) {
    const panes = wizardForm.querySelectorAll('.wizard-pane');
    const nodes = document.querySelectorAll('.wizard-step-node');
    const progressBar = document.querySelector('.wizard-progress-bar');
    const prevBtn = document.getElementById('wizardPrevBtn');
    const nextBtn = document.getElementById('wizardNextBtn');
    const submitBtn = document.getElementById('wizardSubmitBtn');
    const reviewBox = document.getElementById('wizardReviewSummary');
    const confirmationBox = document.getElementById('wizardConfirmationBox');

    let currentStep = 1;
    const totalSteps = panes.length;

    function updateWizardState() {
      panes.forEach(pane => {
        pane.classList.remove('active');
        if (parseInt(pane.getAttribute('data-step'), 10) === currentStep) {
          pane.classList.add('active');
        }
      });

      nodes.forEach((node, idx) => {
        const stepNum = idx + 1;
        node.classList.remove('active', 'completed');
        if (stepNum === currentStep) {
          node.classList.add('active');
        } else if (stepNum < currentStep) {
          node.classList.add('completed');
        }
      });

      if (progressBar) {
        const percent = ((currentStep - 1) / (totalSteps - 1)) * 100;
        progressBar.style.width = `${percent}%`;
      }

      // Nav buttons state
      if (prevBtn) {
        prevBtn.style.display = currentStep > 1 ? 'inline-flex' : 'none';
      }
      if (nextBtn) {
        nextBtn.style.display = currentStep < totalSteps ? 'inline-flex' : 'none';
      }
      if (submitBtn) {
        submitBtn.style.display = currentStep === totalSteps ? 'inline-flex' : 'none';
      }

      // If at review step, populate review summary
      if (currentStep === 6 && reviewBox) {
        populateReviewSummary();
      }

      // Scroll to wizard top
      const wizardContainer = document.querySelector('.wizard-container');
      if (wizardContainer) {
        wizardContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function validateCurrentStep() {
      const activePane = wizardForm.querySelector(`.wizard-pane[data-step="${currentStep}"]`);
      if (!activePane) return true;

      let isValid = true;
      const requiredInputs = activePane.querySelectorAll('[required]');

      requiredInputs.forEach(input => {
        const formGroup = input.closest('.form-group') || input.parentElement;
        if (!input.value.trim()) {
          isValid = false;
          formGroup.classList.add('has-error');
        } else {
          formGroup.classList.remove('has-error');
        }
      });

      return isValid;
    }

    function populateReviewSummary() {
      const fd = new FormData(wizardForm);
      const fullName = fd.get('fullName') || '—';
      const email = fd.get('email') || '—';
      const phone = fd.get('phone') || '—';
      const orgName = fd.get('orgName') || '—';
      const designation = fd.get('designation') || '—';
      const industry = fd.get('industry') || '—';
      const employeeCount = fd.get('employeeCount') || '—';
      const businessStage = fd.get('businessStage') || '—';
      const existingHr = fd.get('existingHr') || '—';

      const services = [];
      wizardForm.querySelectorAll('input[name="services"]:checked').forEach(cb => {
        services.push(cb.value);
      });

      const mainChallenge = fd.get('mainChallenge') || '—';
      const desiredOutcome = fd.get('desiredOutcome') || '—';
      const consultMode = fd.get('consultMode') || 'Online Consultation';
      const preferredDate = fd.get('preferredDate') || '—';
      const preferredTime = fd.get('preferredTime') || '—';

      reviewBox.innerHTML = `
        <div class="table-responsive">
          <table class="table-custom">
            <tbody>
              <tr><th style="width: 35%;">Full Name</th><td>${escapeHtml(fullName)}</td></tr>
              <tr><th>Work Email & Phone</th><td>${escapeHtml(email)} | ${escapeHtml(phone)}</td></tr>
              <tr><th>Organization & Role</th><td>${escapeHtml(orgName)} (${escapeHtml(designation)})</td></tr>
              <tr><th>Industry & Headcount</th><td>${escapeHtml(industry)} | ${escapeHtml(employeeCount)} employees</td></tr>
              <tr><th>Business Stage & HR Team</th><td>${escapeHtml(businessStage)} | Current HR: ${escapeHtml(existingHr)}</td></tr>
              <tr><th>Selected Services</th><td><strong>${services.length > 0 ? services.map(s => escapeHtml(s)).join(', ') : 'None selected'}</strong></td></tr>
              <tr><th>Primary Challenge</th><td>${escapeHtml(mainChallenge)}</td></tr>
              <tr><th>Desired Outcome</th><td>${escapeHtml(desiredOutcome)}</td></tr>
              <tr><th>Meeting Preference</th><td>${escapeHtml(consultMode)} on ${escapeHtml(preferredDate)} (${escapeHtml(preferredTime)})</td></tr>
            </tbody>
          </table>
        </div>
      `;
    }

    function escapeHtml(text) {
      const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
      };
      return String(text).replace(/[&<>"']/g, m => map[m]);
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (validateCurrentStep()) {
          if (currentStep < totalSteps) {
            currentStep++;
            updateWizardState();
          }
        } else {
          window.showDemoToast('Please fill in all required fields before proceeding.');
        }
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (currentStep > 1) {
          currentStep--;
          updateWizardState();
        }
      });
    }

    wizardForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!validateCurrentStep()) {
        window.showDemoToast('Please verify all details before submitting.');
        return;
      }

      // Hide form and show demo confirmation
      wizardForm.style.display = 'none';
      if (confirmationBox) {
        confirmationBox.style.display = 'block';
        confirmationBox.scrollIntoView({ behavior: 'smooth' });
      }
      window.showDemoToast('Enquiry received! This is a frontend demo simulation.');
    });

    // Initialize
    updateWizardState();
  }

  // 2. Contact Page Form
  const contactForm = document.getElementById('contactEnquiryForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let isValid = true;
      const required = contactForm.querySelectorAll('[required]');

      required.forEach(input => {
        const group = input.closest('.form-group') || input.parentElement;
        if (!input.value.trim()) {
          isValid = false;
          group.classList.add('has-error');
        } else {
          group.classList.remove('has-error');
        }
      });

      if (!isValid) {
        window.showDemoToast('Please complete all mandatory fields.');
        return;
      }

      // Show frontend demo success
      const successDiv = document.getElementById('contactFormSuccess');
      if (successDiv) {
        contactForm.style.display = 'none';
        successDiv.style.display = 'block';
      }
      window.showDemoToast('Message submitted in Demo Mode. No data was transmitted.');
    });
  }

  // 3. Careers Page Application Form
  const careerForm = document.getElementById('careerApplicationForm');
  if (careerForm) {
    careerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let isValid = true;
      const required = careerForm.querySelectorAll('[required]');

      required.forEach(input => {
        const group = input.closest('.form-group') || input.parentElement;
        if (!input.value.trim()) {
          isValid = false;
          group.classList.add('has-error');
        } else {
          group.classList.remove('has-error');
        }
      });

      if (!isValid) {
        window.showDemoToast('Please complete all required fields.');
        return;
      }

      const successDiv = document.getElementById('careerFormSuccess');
      if (successDiv) {
        careerForm.style.display = 'none';
        successDiv.style.display = 'block';
      }
      window.showDemoToast('Application submitted in Demo Mode.');
    });
  }
});

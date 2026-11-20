# HR CONSULTING COMPANY — Premium Corporate Website

A complete, modern, multi-page static website representing a generic international **HR Consulting and Human Capital Advisory Company**.

Built strictly with **HTML5, CSS3, and Vanilla JavaScript** with zero external frameworks, libraries, or backend dependencies. Fully responsive across mobile, tablet, laptop, and desktop displays, and 100% compatible with Hostinger static hosting.

---

## 1. Project Overview & Identity Rules
- **Brand Identity:** Generic "HR CONSULTING COMPANY" (no fabricated company name, founder names, employee counts, or awards).
- **Logo:** Abstract geometric symbol (SVG vector) with corporate typography.
- **Color Palette:**
  - Primary Navy: `#13243A`
  - Dark Navy: `#0C192B`
  - Secondary Blue: `#28547A`
  - Accent Teal: `#2F9C95`
  - Light Teal: `#E6F4F1`
  - Warm White: `#FAFBFC`
  - Muted Gold: `#B8A06A`
  - Main Text: `#1B2938`
  - Secondary Text: `#687789`
  - Border: `#E1E7EC`
- **Contact Details (Dummy Placeholders):**
  - Phone: `0000000000`
  - Email: `demo@example.com`
  - Address: Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000.
  - Working Hours: Monday–Saturday: 9:00 AM–6:00 PM.

---

## 2. Directory Structure
```text
hr-consulting/
│
├── index.html                           # Page 1: Homepage (High-priority design showcase)
├── about.html                           # Page 2: About Our Philosophy & Approach
├── services.html                        # Page 3: Services Overview (All 22 services)
├── hr-strategy.html                     # Page 4: HR Strategy & Operating Model
├── hr-audit.html                        # Page 5: HR Process Audit & Assessment
├── talent-acquisition.html              # Page 6: Talent Acquisition & Sourcing
├── recruitment-consulting.html          # Page 7: Recruitment Process Consulting
├── workforce-planning.html              # Page 8: Workforce & Headcount Planning
├── organizational-development.html      # Page 9: Org Structure Design & Job Bands
├── hr-policies.html                     # Page 10: HR Policies & Policy Library
├── employee-handbook.html               # Page 11: Employee Handbook Development
├── performance-management.html          # Page 12: Performance & KPI Management
├── employee-engagement.html             # Page 13: Engagement & Pulse Surveys
├── learning-development.html            # Page 14: Learning & Capability Strategy
├── leadership-development.html          # Page 15: Leadership Capability Framework
├── compensation-benefits.html           # Page 16: Compensation, Grading & Total Rewards
├── payroll-advisory.html                # Page 17: Payroll Workflow & SLA Advisory
├── hr-compliance.html                   # Page 18: HR Compliance & Record Governance
├── posh-consulting.html                 # Page 19: POSH Workplace Awareness (India)
├── employee-relations.html              # Page 20: Employee Relations & Grievances
├── succession-planning.html             # Page 21: Succession Planning & 9-Box Matrix
├── change-management.html               # Page 22: Change Management & Transformation
├── hr-technology.html                   # Page 23: HR Technology & HRMS Selection
├── hr-analytics.html                    # Page 24: People Analytics & Executive Dashboards
├── hr-outsourcing.html                  # Page 25: Managed HR Operations Support
├── industries.html                      # Page 26: Sector Solutions (14 Industries)
├── methodology.html                     # Page 27: 5-Stage Consulting Methodology
├── case-studies.html                    # Page 28: Illustrative Case Study Gallery
├── case-study-details.html              # Page 29: Case Study Blueprint Template
├── team.html                            # Page 30: Functional Practice Area Leaders
├── insights.html                        # Page 31: HR Knowledge Center (12 Articles)
├── article-details.html                 # Page 32: Deep-Dive Editorial Article
├── resources.html                       # Page 33: Templates, Checklists & Worksheets
├── pricing.html                         # Page 34: Engagement Packages & Comparison
├── faq.html                             # Page 35: 16 Categorized FAQs with Accordion
├── careers.html                         # Page 36: Careers & Demo Application Form
├── contact.html                         # Page 37: Contact Information & Enquiry Form
├── book-consultation.html               # Page 38: Multi-Step Consultation Booking Wizard
├── privacy-policy.html                  # Page 39: Privacy Policy (Demo Disclosure)
├── terms-and-conditions.html            # Page 40: Terms of Use & Consulting Scope
│
├── assets/
│   ├── css/
│   │   ├── style.css                    # Design system, components, layout, typography
│   │   ├── responsive.css               # Media queries for 360px up to 1920px
│   │   └── animations.css               # Transitions & prefers-reduced-motion support
│   │
│   ├── js/
│   │   ├── main.js                      # Sticky nav, mobile drawer, scroll reveal
│   │   ├── interactions.js              # FAQ accordions, category filters, live search
│   │   ├── forms.js                     # 6-step consultation wizard, contact & careers forms
│   │   └── dashboard.js                 # Interactive HR dashboards & chart bar animations
│   │
│   ├── images/                          # Destination for Google Flow generated images
│   └── icons/                           # Crisp inline SVG vector icons
│
├── IMAGE-GENERATION-GUIDE.md            # Complete prompt manual for Google Flow
├── sitemap.xml                          # Complete XML sitemap for SEO
├── robots.txt                           # Search engine indexing directives
└── README.md                            # Comprehensive documentation manual
```

---

## 3. How to Open and Test the Website Locally
1. Clone or download the repository folder.
2. Open any HTML file directly in any modern browser (e.g. double-click `index.html` or open in Chrome / Edge / Firefox / Safari).
3. Alternatively, launch a lightweight local server:
   ```bash
   python -m http.server 8000
   ```
   and navigate to `http://localhost:8000/`.

---

## 4. Key Interactive Components
1. **Multi-Step Consultation Booking Wizard (`book-consultation.html`):**
   - 6 progressive steps: Contact Info &rarr; Organization &rarr; Services &rarr; Challenges &rarr; Schedule &rarr; Review & Submit.
   - Client-side field validation, step progress indicator, review summary aggregator, and demo completion state.
2. **Interactive HR Analytics Dashboard (`hr-analytics.html`):**
   - Dynamic department filter dynamically switching headcount, turnover, and open role metrics.
   - Animated CSS/JS bar chart fills showing distributions.
3. **Interactive Knowledge Center & Resources (`insights.html` & `resources.html`):**
   - Filter bar by functional categories.
   - Live instantaneous search bar filtering items in real time.
4. **FAQ Accordion (`faq.html`):**
   - Smooth animated accordion items with accessible keyboard interactions.
5. **Mobile Navigation Drawer:**
   - Touch-friendly hamburger toggle with expandable nested services submenu.

---

## 5. Visual Assets & Image Integration
- **Fully Integrated:** All 52 photographic assets generated for the website are located in `images/` (and mirrored in `assets/images/`) and directly integrated across all 40 HTML pages via standard semantic `<img>` tags.
- **Performance Optimized:** 
  - Above-the-fold hero imagery (`images/hero-hr-consulting-team.jpeg`) loads eagerly with `fetchpriority="high"`.
  - All subsequent section and card images use native browser lazy-loading (`loading="lazy"`).
  - Explicit aspect ratios (`16:9`, `4:3`, `3:4`) are defined via CSS to prevent Cumulative Layout Shifts (CLS).
- **Prompt Reference:** For the complete prompt history and design specifications for each image, refer to [IMAGE-GENERATION-GUIDE.md](IMAGE-GENERATION-GUIDE.md).

---

## 6. How to Deploy on Hostinger Static Hosting
1. Log in to your **Hostinger Control Panel (hPanel)**.
2. Navigate to **Websites** &rarr; Select your domain &rarr; Click **File Manager**.
3. Open the `public_html` directory.
4. Upload all files from this project directory into `public_html`:
   - All `.html` files
   - `assets/` folder (with `css/`, `js/`, `images/`)
   - `sitemap.xml`
   - `robots.txt`
5. Ensure `index.html` resides directly inside `public_html/`.
6. Your website is immediately live and lightning-fast worldwide.

---

## 7. How to Update Dummy Contact Information
To update phone numbers, emails, and office addresses across all pages, search and replace the following strings across all `.html` files:
- Phone: `0000000000` &rarr; `[Your Actual Phone Number]`
- Email: `demo@example.com` &rarr; `[Your Actual Email]`
- Address: `Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000.` &rarr; `[Your Official Physical Address]`

---

## 8. Compliance & Safeguard Rules
- **No Fabricated Data:** All case studies, dashboards, team profiles, and statistics are clearly marked as **Illustrative Demonstration Content**.
- **Statutory Safeguards (India & General):** Advisory descriptions state clearly that employment policies, POSH committee operations, and compliance calendars must be validated with qualified legal counsel.

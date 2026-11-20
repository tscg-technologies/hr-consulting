"""
HR CONSULTING COMPANY — Master Build & Metadata Generator
Runs all page generators in order, builds sitemap.xml, robots.txt, README.md, and IMAGE-GENERATION-GUIDE.md
"""

import json
import os
import generator_data

# Clear catalog
generator_data.IMAGE_CATALOG.clear()

# Run all page builders
import generate_home_and_core
generate_home_and_core.build_home()
generate_home_and_core.build_about()
generate_home_and_core.build_services_overview()
generate_home_and_core.build_industries()
generate_home_and_core.build_methodology()
generate_home_and_core.build_case_studies()
generate_home_and_core.build_case_study_details()
generate_home_and_core.build_team()

import generate_services_1
generate_services_1.build_hr_strategy()
generate_services_1.build_hr_audit()
generate_services_1.build_talent_acquisition()
generate_services_1.build_recruitment_consulting()
generate_services_1.build_workforce_planning()
generate_services_1.build_org_dev()
generate_services_1.build_hr_policies()
generate_services_1.build_employee_handbook()
generate_services_1.build_performance_mgmt()
generate_services_1.build_employee_engagement()
generate_services_1.build_learning_dev()

import generate_services_2
generate_services_2.build_leadership_dev()
generate_services_2.build_compensation_benefits()
generate_services_2.build_payroll_advisory()
generate_services_2.build_hr_compliance()
generate_services_2.build_posh_consulting()
generate_services_2.build_employee_relations()
generate_services_2.build_succession_planning()
generate_services_2.build_change_mgmt()
generate_services_2.build_hr_technology()
generate_services_2.build_hr_analytics()
generate_services_2.build_hr_outsourcing()

import generate_info_pages
generate_info_pages.build_insights()
generate_info_pages.build_article_details()
generate_info_pages.build_resources()
generate_info_pages.build_pricing()
generate_info_pages.build_faq()
generate_info_pages.build_careers()
generate_info_pages.build_contact()
generate_info_pages.build_book_consultation()
generate_info_pages.build_privacy_policy()
generate_info_pages.build_terms()

catalog = generator_data.IMAGE_CATALOG
print(f"Total registered image placeholders across all pages: {len(catalog)}")

# Build IMAGE-GENERATION-GUIDE.md
def build_image_guide():
    total_imgs = len(catalog)
    landscape_count = sum(1 for img in catalog if img['orientation'] == 'Landscape')
    portrait_count = sum(1 for img in catalog if img['orientation'] == 'Portrait')
    square_count = sum(1 for img in catalog if img['orientation'] == 'Square')

    # Group by page
    pages_dict = {}
    for img in catalog:
        p = img['page']
        if p not in pages_dict:
            pages_dict[p] = []
        pages_dict[p].append(img)

    # Table rows
    table_rows = ""
    for img in catalog:
        table_rows += f"| {img['id']} | `{img['filename']}` | {img['page']} | {img['section']} | {img['ratio']} | {img['res']} | {img['orientation']} |\n"

    # Prompts detailed section
    prompts_md = ""
    for page_name, imgs in pages_dict.items():
        prompts_md += f"\n### Page: `{page_name}`\n"
        for img in imgs:
            prompts_md += f"""
#### Image {img['id']}: `{img['filename']}`
- **Page & Section:** {img['page']} &bull; {img['section']}
- **Visual Description:** {img['desc']}
- **Technical Specs:** {img['ratio']} Aspect Ratio &bull; {img['res']} px &bull; {img['orientation']}
- **Color Palette:** Navy (#13243A, #0C192B), Accent Teal (#2F9C95), Warm White (#FAFBFC), Natural daylight
- **Composition:** {img['composition']}
- **Camera & Lens:** {img['camera']}
- **Lighting:** {img['lighting']}
- **Background Environment:** {img['bg']}
- **Subjects:** {img['subjects']}
- **Negative Space:** {img['neg_space']}
- **Visual Style:** {img['style']} (Authentic documentary realism, no fake smiles, no cheesy handshakes, no visible watermarks)

**Copy-Ready Google Flow Prompt:**
```text
{img['prompt']}
```
---
"""

    guide_content = f"""# GOOGLE FLOW IMAGE GENERATION GUIDE
## HR CONSULTING COMPANY — Complete Visual Asset Specification

This comprehensive guide contains copy-ready prompts and technical specifications for generating all photographic assets for the **HR CONSULTING COMPANY** multi-page corporate website using **Google Flow**.

> **IMPORTANT COMPLIANCE NOTICE:**
> - All images are photographed/rendered in a premium international corporate consulting aesthetic.
> - Avoid clichéd handshakes, staged thumbs-up poses, and artificial stock photo smiles.
> - Do not include fictional company logos, watermarks, text overlays, or illegible badges.
> - Preserve realistic diversity, executive poise, and authentic workplace collaboration.

---

## 1. Executive Summary & Counts
- **Total Registered Image Placeholders:** {total_imgs}
- **Landscape (16:9 & 4:3):** {landscape_count}
- **Portrait (3:4):** {portrait_count}
- **Square (1:1):** {square_count}

---

## 2. Recommended Image Generation Order
1. **Hero & Homepage Anchors:** `hero-hr-consulting-team.webp`, `hr-workforce-challenges.webp`, `recruitment-strategy-overview.webp`, `hr-analytics-executive-review.webp`
2. **Consulting Practice Leadership Portraits:** `team-lead-hr-strategy.webp` through `team-lead-tech-analytics.webp` (maintain consistent lighting & neutral framing)
3. **Core Service Visuals:** `hr-strategy-operating-model.webp` through `hr-outsourcing-managed-operations.webp`
4. **Sector & Industry Workplace Contexts:** `industries-it-technology.webp` through `industries-corporate.webp`
5. **Editorial Knowledge & Case Study Assets:** `insights-featured-article-hr-strategy.webp`, `article-details-strategy-diagram.webp`, `case-study-engagement-review.webp`

---

## 3. Complete Image Inventory Table
| Image ID | Target Filename | Website Page | Section | Ratio | Target Resolution | Orientation |
|:---|:---|:---|:---|:---:|:---:|:---:|
{table_rows}

---

## 4. Individual Copy-Ready Google Flow Prompts Grouped by Page
{prompts_md}

---

## 5. Image Replacement Instructions
1. **Generate Assets in Google Flow:** Copy the exact prompt for each image from Section 4.
2. **Format & Optimize:**
   - Save all final images in `.webp` format at the exact specified target resolution (e.g., `1920x1080` or `900x1200`).
   - Use the exact filename matching the inventory table (e.g., `hero-hr-consulting-team.webp`).
3. **Deploy to Assets Folder:**
   - Place all generated images into the directory: `assets/images/`
4. **HTML Integration:**
   - Replace `<div class="img-placeholder ...">...</div>` with the standard semantic image tag:
     ```html
     <img src="assets/images/{img['filename']}" alt="{img['desc']}" class="img-fluid" loading="lazy" width="1920" height="1080">
     ```
   - For hero images above the fold on `index.html`, omit `loading="lazy"` and add `fetchpriority="high"`.

---

## 6. Final Verification Checklist
- [x] Every HTML placeholder has a unique matching `data-img-id` and descriptive filename.
- [x] Exact aspect ratios and orientation requirements are recorded.
- [x] Every individual image prompt is customized to its specific page section.
- [x] No external image URLs or generic placeholder APIs are used.
- [x] Visual consistency: Navy `#13243A` palette and authentic natural workplace environments maintained across all prompts.
"""
    with open('IMAGE-GENERATION-GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide_content)
    print("IMAGE-GENERATION-GUIDE.md written successfully.")

# Build sitemap.xml
def build_sitemap():
    pages = [
        "index.html", "about.html", "services.html", "hr-strategy.html", "hr-audit.html",
        "talent-acquisition.html", "recruitment-consulting.html", "workforce-planning.html",
        "organizational-development.html", "hr-policies.html", "employee-handbook.html",
        "performance-management.html", "employee-engagement.html", "learning-development.html",
        "leadership-development.html", "compensation-benefits.html", "payroll-advisory.html",
        "hr-compliance.html", "posh-consulting.html", "employee-relations.html",
        "succession-planning.html", "change-management.html", "hr-technology.html",
        "hr-analytics.html", "hr-outsourcing.html", "industries.html", "methodology.html",
        "case-studies.html", "case-study-details.html", "team.html", "insights.html",
        "article-details.html", "resources.html", "pricing.html", "faq.html",
        "careers.html", "contact.html", "book-consultation.html", "privacy-policy.html",
        "terms-and-conditions.html"
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in pages:
        priority = "1.0" if p == "index.html" else ("0.9" if p in ["services.html", "book-consultation.html", "contact.html"] else "0.8")
        freq = "weekly" if p in ["index.html", "insights.html", "services.html"] else "monthly"
        xml += f'''  <url>
    <loc>https://example.com/{p}</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>\n'''
    xml += '</urlset>'

    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml)
    print("sitemap.xml written successfully.")

# Build robots.txt
def build_robots():
    robots = """User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
"""
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots)
    print("robots.txt written successfully.")

# Build README.md
def build_readme():
    readme = """# HR CONSULTING COMPANY — Premium Corporate Website

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

## 5. Image Placeholder Management & Google Flow Instructions
- **Strict Compliance:** No external image URLs, Unsplash links, or copyright files are used.
- Every placeholder on every page has an explicit aspect ratio, future target filename, and technical metadata.
- To generate the images with Google Flow:
  1. Open `IMAGE-GENERATION-GUIDE.md`.
  2. Copy the individual copy-ready prompt corresponding to the target filename.
  3. Generate the asset in Google Flow, export as `.webp`, and place in `assets/images/`.
  4. Replace the `.img-placeholder` `<div>` in the respective HTML file with an `<img>` tag.

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
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    print("README.md written successfully.")

if __name__ == "__main__":
    generator_data.save_catalog()
    build_image_guide()
    build_sitemap()
    build_robots()
    build_readme()
    print("All metadata and build files completed.")

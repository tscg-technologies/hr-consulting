"""
Generates Information, Knowledge, Engagement & Compliance Pages:
- insights.html
- article-details.html
- resources.html
- pricing.html
- faq.html
- careers.html
- contact.html
- book-consultation.html
- privacy-policy.html
- terms-and-conditions.html
"""

from generator_data import register_img, render_img, get_page_hero, get_demo_disclaimer, get_cta_section, write_html_page

def build_insights():
    img_featured = register_img(
        filename="insights-featured-article-hr-strategy.webp",
        page="insights.html",
        section="Featured Article",
        desc="Senior HR management consultants and executive directors reviewing strategic organizational growth frameworks in a modern glass boardroom.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Editorial corporate photography for a human resources thought leadership feature. Business leaders and HR consultants engaged in strategic dialogue around a conference table with analytical documents and digital tablets. Sophisticated modern office, warm natural sunlight, cinematic depth of field.",
        composition="Wide horizontal shot featuring leaders engaged in strategic review",
        camera="50mm lens, f/2.5",
        lighting="Natural ambient morning lighting",
        bg="Minimalist modern executive conference room",
        subjects="Three business executives in discussion",
        neg_space="Left upper area uncluttered"
    )

    articles = [
        ("Why Every Growing Business Needs an HR Strategy", "hr-strategy", "8 min read", "Informal people management works for 10 people, but creates systemic bottlenecks as teams reach 50+ staff.", "article-details.html"),
        ("How to Build an Effective Recruitment Process", "recruitment", "6 min read", "Transition from hasty keyword searches to structured competency rubrics that consistently identify top performers.", "article-details.html"),
        ("HR Policies Every Organization Should Review", "policies", "7 min read", "Key workplace policies that require regular updates to reflect hybrid work, attendance, and conduct standards.", "article-details.html"),
        ("Understanding Strategic Workforce Planning", "workforce-planning", "9 min read", "How to accurately project manpower costs, forecast hiring needs, and eliminate costly overstaffing cycles.", "article-details.html"),
        ("How to Create a Performance Management Framework", "performance", "8 min read", "Replace dread-inducing annual reviews with continuous feedback cadences and transparent quarterly OKRs.", "article-details.html"),
        ("Employee Engagement Strategies for Growing Teams", "engagement", "5 min read", "Practical listening surveys and manager habits that combat quiet quitting and reinforce workplace culture.", "article-details.html"),
        ("How HR Analytics Supports Executive Business Decisions", "analytics", "6 min read", "Moving beyond simple headcount counts to predictive turnover modeling and recruitment funnel velocity.", "article-details.html"),
        ("The Critical Importance of Structured Employee Onboarding", "recruitment", "5 min read", "Why the first 30 days dictate long-term employee retention, engagement, and time-to-productivity.", "article-details.html"),
        ("How to Improve Organizational Structure & Role Clarity", "org-dev", "7 min read", "Techniques for eliminating territorial overlap and clarifying managerial authority with RACI matrices.", "article-details.html"),
        ("HR Technology Trends for Modern Mid-Sized Businesses", "tech", "6 min read", "How to navigate the confusing HRMS vendor marketplace and select tools employees will actually adopt.", "article-details.html"),
        ("Building a Practical Learning & Development Plan", "learning", "7 min read", "How to conduct an objective Training Needs Assessment without wasting capital on generic seminars.", "article-details.html"),
        ("Understanding POSH Workplace Awareness in India", "compliance", "10 min read", "A comprehensive guide to statutory mandates, Internal Committee responsibilities, and prevention training.", "article-details.html")
    ]

    cards_html = ""
    for title, cat, read_time, snippet, link in articles:
        cards_html += f'''
      <div class="card filterable-item searchable-item" data-category="{cat} all">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.75rem;">
          <span class="badge badge-navy" style="font-size:0.7rem;">{cat.upper()}</span>
          <span style="font-size:0.75rem; color:var(--color-secondary-text);">{read_time}</span>
        </div>
        <h3 class="card-title" style="font-size:1.15rem;"><a href="{link}">{title}</a></h3>
        <p class="card-text" style="font-size:0.875rem;">{snippet}</p>
        <div class="card-footer">
          <a href="{link}" class="link-arrow">Read Full Article &rarr;</a>
        </div>
      </div>'''

    content = f'''
{get_page_hero("HR Knowledge Center & Executive Insights", "Strategic perspectives on human capital management, workforce planning, recruitment, and organizational design.", [("Insights", "insights.html")])}

<section class="section">
  <div class="container">
    <!-- Featured Article Banner -->
    <div class="card" style="padding:2.5rem; margin-bottom:3.5rem; background:linear-gradient(135deg, #F8FAFC 0%, #FFFFFF 100%);">
      <div class="grid grid-2 items-center gap-xl">
        <div>
          <span class="badge badge-teal" style="margin-bottom:0.75rem;">Featured Editorial</span>
          <h2 style="font-size:1.85rem; margin-bottom:1rem;"><a href="article-details.html">Why Every Growing Business Needs a Strategic HR Foundation</a></h2>
          <p class="lead" style="font-size:1.05rem;">As organizations expand beyond early founder-led management, informal people practices inevitably break down. Discover how structured HR architectures unlock operational resilience.</p>
          <div style="margin: 1.5rem 0;">
            <a href="article-details.html" class="btn btn-primary">Read Complete Deep-Dive Article &rarr;</a>
          </div>
          <span style="font-size:0.8125rem; color:var(--color-secondary-text);">Practice Insight &bull; 8 Min Read &bull; Strategy & Org Design</span>
        </div>
        <div>
          {render_img(img_featured)}
        </div>
      </div>
    </div>

    <!-- Category Filters and Live Search -->
    <div style="display:flex; flex-direction:column; gap:1.5rem; align-items:center; margin-bottom:2.5rem;">
      <div style="width:100%; max-width:500px;">
        <input type="text" class="form-control interactive-search-input" data-search-container=".filterable-grid" placeholder="Search knowledge articles by keyword..." style="padding:0.85rem 1.25rem; border-radius:var(--radius-full); box-shadow:var(--shadow-sm);">
      </div>

      <div class="filter-bar" data-target-container=".filterable-grid" style="margin-bottom:0;">
        <button class="filter-btn active" data-filter="all">All Topics</button>
        <button class="filter-btn" data-filter="hr-strategy">Strategy</button>
        <button class="filter-btn" data-filter="recruitment">Recruitment</button>
        <button class="filter-btn" data-filter="policies">Policies</button>
        <button class="filter-btn" data-filter="performance">Performance</button>
        <button class="filter-btn" data-filter="engagement">Engagement</button>
        <button class="filter-btn" data-filter="analytics">Analytics</button>
        <button class="filter-btn" data-filter="compliance">Compliance</button>
      </div>
    </div>

    {get_demo_disclaimer("Articles in this knowledge center provide educational perspectives and sample frameworks. They are not intended as legal or certified professional advice.")}

    <div class="grid grid-3 gap-lg filterable-grid" style="margin-top:2rem;">
      {cards_html}
    </div>
  </div>
</section>

{get_cta_section()}
'''
    write_html_page("insights.html", "HR Insights & Knowledge Center | Human Capital Perspectives",
                    "Explore our human resources knowledge center for actionable insights on HR strategy, workforce planning, performance management, and compliance.", content, "Insights")

def build_article_details():
    img_article = register_img(
        filename="article-details-strategy-diagram.webp",
        page="article-details.html",
        section="Article Body",
        desc="An executive HR diagram illustrating the alignment of business milestones with workforce capabilities and HR operating models.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="High quality editorial diagram photography. A sleek digital strategy diagram displaying human capital architecture, talent acquisition pipelines, and performance evaluation cycles displayed on a frosted glass screen in an executive suite. Clean, professional.",
        composition="Medium shot showing detailed strategic diagram",
        camera="50mm lens, f/2.8",
        lighting="Clear ambient studio daylight",
        bg="Minimalist modern executive conference room",
        subjects="Diagram presentation on digital glass surface",
        neg_space="Left and upper margins clean"
    )

    content = f'''
{get_page_hero("Why Every Growing Business Needs an HR Strategy", "How transitioning from informal practices to structured HR systems protects enterprise value.", [("Insights", "insights.html"), ("Article Details", "article-details.html")])}

<section class="section">
  <div class="container container-narrow">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2rem; padding-bottom:1rem; border-bottom:1px solid var(--color-border);">
      <span class="badge badge-teal">Strategic HR Practice</span>
      <span style="font-size:0.84rem; color:var(--color-secondary-text);">Estimated Reading Time: 8 Minutes &bull; Educational Guide</span>
    </div>

    <div style="margin-bottom:2.5rem;">
      {render_img(img_article)}
    </div>

    <!-- Table of Contents -->
    <div class="card" style="background:var(--color-bg-alt); padding:1.5rem; margin-bottom:2.5rem;">
      <h4 style="font-size:1.05rem; margin-bottom:0.75rem;">Table of Contents</h4>
      <ul style="font-size:0.875rem; line-height:1.7;">
        <li><a href="#section-1">1. The Inflection Point: From Founder Intuition to Structured Systems</a></li>
        <li><a href="#section-2">2. The Hidden Costs of Reactive People Management</a></li>
        <li><a href="#section-3">3. Four Pillars of a Sustainable HR Foundation</a></li>
        <li><a href="#section-4">4. Building a Phased Implementation Roadmap</a></li>
        <li><a href="#section-5">5. Key Executive Takeaways</a></li>
      </ul>
    </div>

    <article style="line-height:1.8; font-size:1.02rem;">
      <h3 id="section-1">1. The Inflection Point: From Founder Intuition to Structured Systems</h3>
      <p>In the earliest days of an enterprise, people management happens organically. Founders sit alongside the first dozen hires, transmitting cultural expectations over lunch, reviewing work informally, and resolving disputes in real time. Because communication paths are short and direct, formal HR policies feel superfluous.</p>
      <p>However, once headcount crosses roughly 30 to 50 employees, informal methods inevitably break down. Departmental siloes emerge, line managers apply contradictory standards to their teams, and newly hired employees lack clear benchmarks for performance success. Without deliberate systems, organizational growth becomes hindered by internal friction.</p>

      <h3 id="section-2" style="margin-top:2.5rem;">2. The Hidden Costs of Reactive People Management</h3>
      <p>When organizations treat human resources as purely administrative paperwork rather than an enterprise capability, three costly failure modes predictably emerge:</p>
      <div class="deliverables-list" style="margin:1rem 0;">
        <ul>
          <li><strong>Prolonged Recruitment Cycles & Mis-Hires:</strong> Hiring managers without structured interview rubrics rely on gut feeling, resulting in costly mismatched appointments and early turnover.</li>
          <li><strong>Manager Inconsistency:</strong> One manager might permit flexible hours while another penalizes remote work, breeding resentment and perceived favoritism among staff.</li>
          <li><strong>Evaluation Friction:</strong> Without objective KRAs, annual compensation reviews become contentious debates based on recency bias rather than measurable output.</li>
        </ul>
      </div>

      <h3 id="section-3" style="margin-top:2.5rem;">3. Four Pillars of a Sustainable HR Foundation</h3>
      <p>Establishing an effective HR foundation does not mean instituting stifling bureaucracy. Rather, it means creating a transparent operating model built on four foundational pillars:</p>
      <ol style="padding-left:1.5rem; margin-bottom:1.5rem;">
        <li style="margin-bottom:0.75rem;"><strong>Clear Job Architecture:</strong> Standardized role profiles and title bands that define expectations at every organizational level.</li>
        <li style="margin-bottom:0.75rem;"><strong>Structured Sourcing & Evaluation:</strong> Competency-based interview guides that ensure consistent evaluation across candidates.</li>
        <li style="margin-bottom:0.75rem;"><strong>Objective Performance Cadences:</strong> Quarterly goal alignment meetings centered on verifiable deliverables.</li>
        <li style="margin-bottom:0.75rem;"><strong>Transparent Workplace Governance:</strong> An accessible Employee Handbook that clearly explains leave, conduct, and dispute resolution procedures.</li>
      </ol>

      <h3 id="section-4" style="margin-top:2.5rem;">4. Building a Phased Implementation Roadmap</h3>
      <p>Rather than attempting to overhaul all people practices simultaneously, leadership teams should sequence changes in logical phases. Start with an operational audit to uncover existing vulnerabilities, followed by standardizing core policies and job descriptions, before layering advanced performance metrics and analytics dashboards.</p>

      <h3 id="section-5" style="margin-top:2.5rem;">5. Key Executive Takeaways</h3>
      <p>Investing in HR infrastructure is not an overhead expense—it is a preventative safeguard that protects corporate velocity, preserves workplace culture, and enables predictable business scaling.</p>
    </article>

    {get_demo_disclaimer("This article is an educational publication produced by our consulting practice. Adaptations of these concepts should be validated against your organizational circumstances.")}

    <div style="margin-top:3rem; padding-top:2rem; border-top:1px solid var(--color-border); display:flex; justify-content:space-between; align-items:center;">
      <a href="insights.html" class="btn btn-outline">&larr; Back to All Insights</a>
      <a href="book-consultation.html" class="btn btn-teal">Discuss Strategic HR for Your Firm</a>
    </div>
  </div>
</section>

{get_cta_section()}
'''
    write_html_page("article-details.html", "Why Every Growing Business Needs an HR Strategy | HR Insights",
                    "Read our comprehensive executive guide on how building a strategic HR foundation transforms workforce performance and scales operations.", content, "Insights")

def build_resources():
    resources_list = [
        ("HR Audit Baseline Checklist", "audit", "A comprehensive 40-point diagnostic checklist to review employee documentation, onboarding hygiene, and policy records."),
        ("Workplace Policy Library Checklist", "policies", "An essential inventory checklist covering attendance, leave, remote working, and code of conduct standard clauses."),
        ("Recruitment Process & SLA Checklist", "recruitment", "A standardized hiring workflow checklist with manager interview scorecards and stage turnaround benchmarks."),
        ("Employee Onboarding 30-60-90 Day Plan", "onboarding", "A structured orientation template ensuring new hires achieve clarity, peer connections, and early milestone success."),
        ("Quarterly Performance Review Template", "performance", "An objective appraisal form combining core competencies, measurable OKR scoring, and developmental action plans."),
        ("Workforce Headcount Planning Worksheet", "planning", "A multi-departmental forecasting model template to project staffing needs, vacancy gaps, and compensation budgets."),
        ("Employee Handbook Standard Outline", "handbook", "A comprehensive table of contents and section blueprint for creating a customized company handbook."),
        ("Training Needs Assessment (TNA) Survey", "learning", "A manager survey instrument to identify team skill gaps, technical training requirements, and supervisory needs."),
        ("Employee Engagement Pulse Survey Model", "engagement", "A 15-question validated survey template measuring role clarity, manager feedback, and team sentiment."),
        ("HR Executive KPI Dashboard Specifications", "analytics", "A blueprint defining core people metrics including voluntary turnover, time-to-fill, and retention formulas."),
        ("Annual HR Compliance Governance Calendar", "compliance", "A periodic calendar template tracking monthly wage registers, quarterly committee meetings, and annual filings."),
        ("POSH Awareness & IC Readiness Checklist", "posh", "A procedural checklist for organizations in India to verify policy publication, IC constitution, and annual reporting.")
    ]

    cards_html = ""
    for title, cat, desc in resources_list:
        cards_html += f'''
      <div class="card filterable-item searchable-item" data-category="{cat} all">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.75rem;">
          <span class="badge badge-teal" style="font-size:0.7rem;">{cat.upper()}</span>
          <span class="badge badge-demo" style="font-size:0.65rem;">Sample Template</span>
        </div>
        <h3 class="card-title" style="font-size:1.15rem;">{title}</h3>
        <p class="card-text" style="font-size:0.875rem;">{desc}</p>
        <div class="card-footer">
          <a href="book-consultation.html" class="link-arrow">Request Tailored Template &rarr;</a>
        </div>
      </div>'''

    content = f'''
{get_page_hero("HR Templates, Checklists & Worksheets Library", "A curated collection of practical human capital frameworks, checklists, and management templates.", [("Resources", "resources.html")])}

<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Toolkit</span>
      <h2>Practical Resources for People Managers</h2>
      <p class="section-subtitle">Preview standardized checklists, review templates, and operational roadmaps developed by our consulting practice.</p>
    </div>

    <!-- Search Input -->
    <div style="max-width:500px; margin:0 auto 2.5rem;">
      <input type="text" class="form-control interactive-search-input" data-search-container=".filterable-grid" placeholder="Search templates and checklists by name..." style="padding:0.85rem 1.25rem; border-radius:var(--radius-full); box-shadow:var(--shadow-sm);">
    </div>

    {get_demo_disclaimer("All templates and checklists listed below represent illustrative demonstration frameworks. Employment documentation must be customized and legally reviewed against applicable jurisdictional regulations before operational implementation.")}

    <div class="grid grid-3 gap-lg filterable-grid" style="margin-top:2rem;">
      {cards_html}
    </div>
  </div>
</section>

{get_cta_section("Need a Customized HR Toolkit?", "Our consulting team can adapt and customize these resources to match your organizational workflow.")}
'''
    write_html_page("resources.html", "HR Resources & Templates | Checklists & Management Worksheets",
                    "Browse practical HR checklists, performance review templates, onboarding guides, and workforce planning worksheets.", content, "Resources")

def build_pricing():
    content = f'''
{get_page_hero("HR Consulting Engagement Models & Service Packages", "Flexible, transparent consulting packages structured to support businesses at every growth stage.", [("Pricing", "pricing.html")])}

<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Engagement Structures</span>
      <h2>Three Illustrative Consulting Service Packages</h2>
      <p class="section-subtitle">Whether establishing initial people systems or transforming enterprise workforce operations, we offer tailored models.</p>
    </div>

    <div class="grid grid-3 gap-lg">
      <div class="card" style="border-top:4px solid var(--color-secondary-blue);">
        <h3 class="card-title">HR Foundation Assessment</h3>
        <p class="card-text">Ideal for startups and growing SMEs (20&ndash;60 staff) looking to baseline existing HR practices and identify compliance risks.</p>
        <div style="font-size:1.35rem; font-weight:800; color:var(--color-dark-navy); margin:1.25rem 0;">Custom Proposal</div>
        <ul class="deliverables-list" style="margin-bottom:1.5rem;">
          <li>Baseline HR process & file audit.</li>
          <li>Comprehensive gap analysis report.</li>
          <li>Initial policy hygiene recommendations.</li>
          <li>Executive debriefing presentation.</li>
        </ul>
        <div class="card-footer">
          <a href="book-consultation.html" class="btn btn-outline" style="width:100%;">Request Custom Proposal</a>
        </div>
      </div>

      <div class="card" style="border-top:4px solid var(--color-accent-teal); transform:translateY(-8px); box-shadow:var(--shadow-xl);">
        <span class="badge badge-teal" style="width:fit-content; margin-bottom:0.5rem;">Most Comprehensive</span>
        <h3 class="card-title">HR Systems & Process Development</h3>
        <p class="card-text">Tailored for scaling organizations (60&ndash;250 staff) needing complete policies, job bands, and performance management.</p>
        <div style="font-size:1.35rem; font-weight:800; color:var(--color-dark-navy); margin:1.25rem 0;">Custom Proposal</div>
        <ul class="deliverables-list" style="margin-bottom:1.5rem;">
          <li>Everything in Foundation Assessment.</li>
          <li>Custom Employee Handbook development.</li>
          <li>Job architecture & role leveling bands.</li>
          <li>Quarterly KPI/OKR review framework.</li>
          <li>Manager interview enablement workshops.</li>
        </ul>
        <div class="card-footer">
          <a href="book-consultation.html" class="btn btn-teal" style="width:100%;">Request Custom Proposal</a>
        </div>
      </div>

      <div class="card" style="border-top:4px solid var(--color-primary-navy);">
        <h3 class="card-title">Strategic HR Partnership</h3>
        <p class="card-text">Designed for enterprise organizations (250+ staff) seeking an ongoing strategic human capital advisory and transformation partner.</p>
        <div style="font-size:1.35rem; font-weight:800; color:var(--color-dark-navy); margin:1.25rem 0;">Custom Proposal</div>
        <ul class="deliverables-list" style="margin-bottom:1.5rem;">
          <li>Ongoing executive workforce advisory.</li>
          <li>Succession planning & 9-box matrices.</li>
          <li>Independent HRMS software evaluation.</li>
          <li>Executive people analytics scorecards.</li>
          <li>Quarterly strategy & governance reviews.</li>
        </ul>
        <div class="card-footer">
          <a href="book-consultation.html" class="btn btn-outline" style="width:100%;">Request Custom Proposal</a>
        </div>
      </div>
    </div>

    <div class="demo-banner" style="margin-top:3rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      <div>
        <strong>Engagement Pricing Disclaimer:</strong>
        <p style="margin-top:0.25rem;">Final consulting fees depend on workforce size, business requirements, engagement scope, duration, and agreed deliverables. We do not publish arbitrary fixed fees because every enterprise people architecture is unique.</p>
      </div>
    </div>
  </div>
</section>

<!-- Detailed Deliverables Comparison Table -->
<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Scope Comparison</span>
      <h2>Deliverable Scope Matrix</h2>
      <p class="section-subtitle">Examine the detailed breakdown of advisory deliverables across engagement tiers.</p>
    </div>

    <div class="table-responsive">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Advisory Scope Element</th>
            <th>Foundation Assessment</th>
            <th>Systems & Process Development</th>
            <th>Strategic HR Partnership</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Initial HR Process Audit & Gap Analysis</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Personnel Documentation Review</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Customized Employee Handbook</td>
            <td>&mdash;</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Job Architecture & Leveling Bands</td>
            <td>&mdash;</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Quarterly KPI / Review System Design</td>
            <td>&mdash;</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Hiring Manager Interview Training</td>
            <td>&mdash;</td>
            <td>✓ Included</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Succession Planning & Talent Matrix</td>
            <td>&mdash;</td>
            <td>&mdash;</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Executive People Analytics Dashboards</td>
            <td>&mdash;</td>
            <td>&mdash;</td>
            <td>✓ Included</td>
          </tr>
          <tr>
            <td>Ongoing Executive Advisory Retainer</td>
            <td>&mdash;</td>
            <td>&mdash;</td>
            <td>✓ Included</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

{get_cta_section("Request a Custom HR Proposal", "Contact our advisory practice to receive a tailored scope of work aligned with your business scale.")}
'''
    write_html_page("pricing.html", "Engagement Models & Pricing | HR Consulting Packages",
                    "Explore our three tailored HR consulting engagement packages: Foundation Assessment, Systems & Process Development, and Strategic HR Partnership.", content, "Pricing")

def build_faq():
    faqs = [
        ("What does an HR consulting company do?", "An HR consulting company helps organizations structure, optimize, and manage their workforce practices. This includes drafting policies, building recruitment pipelines, designing performance review frameworks, conducting compliance audits, and aligning people strategies with business growth."),
        ("How can HR consulting help a growing business?", "As companies grow beyond early team sizes, informal people management breaks down. HR consulting helps establish scalable systems, reduces costly hiring mistakes, resolves manager inconsistencies, improves employee retention, and ensures documentation hygiene."),
        ("Do you help startups establish HR systems from scratch?", "Yes. We frequently consult with early-stage and seed-funded companies to create foundational HR infrastructure: standard offer letter templates, an employee handbook, initial job bands, and structured hiring checklists."),
        ("Can you develop a customized employee handbook for our company?", "Yes. We develop comprehensive, tailored employee handbooks reflecting your company's values, culture, and operational realities, including attendance, leave, remote working, conduct, and grievance procedures."),
        ("Do you provide recruitment consulting?", "Yes. Our recruitment consulting optimizes internal hiring processes. We author competency-based job descriptions, design interview scoring rubrics, train hiring managers, and streamline recruiter tracking metrics."),
        ("Can you help with workforce and headcount planning?", "Yes. We evaluate current employee utilization, conduct skills gap analyses, model multi-scenario headcount projections, and align recruitment budgets with projected business revenue."),
        ("Do you support employee onboarding processes?", "Yes. We design structured 30-60-90 day onboarding frameworks, orientation schedules, and manager checklists that accelerate new hire time-to-productivity and reduce early turnover."),
        ("Can you design performance management systems?", "Yes. We replace subjective annual appraisals with objective quarterly OKR/KPI frameworks, continuous 1-on-1 check-in guides, 360-degree feedback tools, and structured performance improvement plans (PIPs)."),
        ("What is included in an operational HR audit?", "An operational HR audit systematically inspects personnel files, onboarding records, leave tracking systems, separation documentation, and managerial review cadences to identify inefficiencies and administrative gaps."),
        ("Can you help measure and improve employee engagement?", "Yes. We formulate anonymous pulse surveys, conduct culture assessments, analyze feedback themes, and equip department leaders with actionable retention and recognition blueprints."),
        ("What is the difference between HR consulting and HR outsourcing?", "HR consulting focuses on high-level strategic advisory, framework architecture, policy design, and process optimization. HR outsourcing involves executing daily administrative operations such as onboarding coordination and employee records maintenance."),
        ("Can you provide HRMS software selection consulting?", "Yes. We act as an independent technology advisor. We define software requirements, author RFP evaluation rubrics, objectively compare commercial HRMS vendors, and oversee system adoption."),
        ("Do you provide POSH awareness consulting in India?", "Yes. We provide policy drafting advisory, employee awareness training frameworks, and procedural guidance for Internal Committees (IC) under the Indian POSH Act, 2013."),
        ("How are consulting fees calculated?", "Fees are structured around engagement scope, organization headcount, project duration, and agreed deliverable milestones. We provide detailed, transparent proposals following an initial discovery meeting."),
        ("Can HR consulting services be customized to our needs?", "Absolutely. Every engagement is modular. Organizations can commission targeted interventions, such as a standalone policy manual or performance framework, or comprehensive enterprise transformations."),
        ("How does an HR consulting engagement begin?", "Engagements typically begin with an introductory discovery consultation to evaluate your organizational scale, people management challenges, and commercial milestones, followed by a formal scope proposal.")
    ]

    faq_html = ""
    for idx, (q, a) in enumerate(faqs):
        active_cls = "active" if idx == 0 else ""
        faq_html += f'''
      <div class="accordion-item {active_cls}">
        <div class="accordion-header">
          <h4 class="accordion-title">{q}</h4>
          <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
        <div class="accordion-content">
          <p>{a}</p>
        </div>
      </div>'''

    content = f'''
{get_page_hero("Frequently Asked Questions", "Answers to common questions about HR consulting, workforce planning, recruitment advisory, and engagement scopes.", [("FAQ", "faq.html")])}

<section class="section">
  <div class="container container-narrow">
    <div class="section-header text-center">
      <span class="section-tag">Clear Answers</span>
      <h2>Everything You Need to Know About Our Advisory</h2>
      <p class="section-subtitle">Browse answers to frequent inquiries across our functional human capital practice domains.</p>
    </div>

    <div class="accordion">
      {faq_html}
    </div>
  </div>
</section>

{get_cta_section("Still Have Questions?", "Schedule an exploratory call with our consulting team to discuss your specific questions.")}
'''
    write_html_page("faq.html", "Frequently Asked Questions | HR Consulting Company",
                    "Find answers to frequently asked questions about HR strategy, recruitment consulting, performance management, policies, and pricing.", content, "FAQ")

def build_careers():
    opportunities = [
        ("Senior HR Strategy Consultant", "Advisory Practice", "Lead client diagnostic audits, operating model designs, and strategic workforce roadmaps for scaling enterprises."),
        ("Talent Acquisition Strategist", "Recruitment Advisory", "Architect client candidate sourcing pipelines, interview scoring rubrics, and recruiter training workshops."),
        ("Performance & Total Rewards Consultant", "Compensation Practice", "Design job architecture bandings, quarterly review frameworks, and variable compensation incentive models."),
        ("HR Operations & Documentation Specialist", "Policy & Compliance", "Draft employee handbooks, standard operating procedures, and compliance record maintenance calendars."),
        ("Organizational Development Advisor", "Org Effectiveness", "Guide enterprise clients through reporting line restructurings, RACI responsibility mapping, and cultural assessments."),
        ("People Analytics & HRMS Consultant", "HR Technology", "Configure workforce reporting dashboards, turnover predictive models, and HRMS vendor evaluation matrices."),
        ("L&D Program Designer", "Learning Practice", "Formulate corporate Training Needs Assessments (TNAs), managerial development curricula, and capability calendars."),
        ("Human Capital Consulting Intern", "Graduate Fellowship", "Support senior advisors with industry research, diagnostic data cleaning, and presentation formatting.")
    ]

    cards_html = ""
    for title, dept, desc in opportunities:
        cards_html += f'''
      <div class="card">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
          <span class="badge badge-navy">{dept}</span>
          <span class="badge badge-demo" style="font-size:0.65rem;">Illustrative Role</span>
        </div>
        <h3 class="card-title" style="font-size:1.15rem;">{title}</h3>
        <p class="card-text" style="font-size:0.875rem;">{desc}</p>
        <div class="card-footer">
          <a href="#applySection" class="link-arrow">Apply Below &rarr;</a>
        </div>
      </div>'''

    content = f'''
{get_page_hero("Careers in Human Capital Advisory", "Join a disciplined consulting practice dedicated to building stronger teams and better workplaces.", [("Careers", "careers.html")])}

<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Join The Practice</span>
      <h2>Illustrative Consulting Opportunities</h2>
      <p class="section-subtitle">We collaborate with analytical, human-centered professionals who thrive on solving complex workforce challenges.</p>
    </div>

    {get_demo_disclaimer("Job listings displayed below represent illustrative demonstration profiles. They do not constitute active commercial vacancies, binding employment offers, or formal recruitment commitments.")}

    <div class="grid grid-2 gap-lg" style="margin-top:2rem;">
      {cards_html}
    </div>
  </div>
</section>

<!-- Application Form -->
<section class="section section-bg-alt" id="applySection">
  <div class="container container-narrow">
    <div class="section-header text-center">
      <span class="section-tag">Application</span>
      <h2>Submit Your Expression of Interest (Demo Form)</h2>
      <p class="section-subtitle">This form is a client-side frontend demonstration. No personal data will be transmitted or stored remotely.</p>
    </div>

    <div class="form-card">
      <form id="careerApplicationForm">
        <div class="grid grid-2 gap-md">
          <div class="form-group">
            <label class="form-label">Full Name *</label>
            <input type="text" class="form-control" name="candidateName" placeholder="e.g. Jane Doe" required>
            <div class="form-error">Please provide your full name.</div>
          </div>
          <div class="form-group">
            <label class="form-label">Email Address *</label>
            <input type="email" class="form-control" name="candidateEmail" placeholder="e.g. jane@example.com" required>
            <div class="form-error">Please provide a valid email.</div>
          </div>
        </div>

        <div class="grid grid-2 gap-md">
          <div class="form-group">
            <label class="form-label">Phone Number *</label>
            <input type="tel" class="form-control" name="candidatePhone" placeholder="e.g. 0000000000" required>
            <div class="form-error">Please provide a contact phone number.</div>
          </div>
          <div class="form-group">
            <label class="form-label">Practice Area of Interest *</label>
            <select class="form-select" name="practiceArea" required>
              <option value="">Select practice area...</option>
              <option value="strategy">HR Strategy & Org Design</option>
              <option value="recruitment">Talent Acquisition & Sourcing</option>
              <option value="compensation">Performance & Compensation</option>
              <option value="policy">HR Policies & Compliance</option>
              <option value="tech">HR Technology & Analytics</option>
              <option value="intern">Graduate Consulting Internship</option>
            </select>
            <div class="form-error">Please select a practice area.</div>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Brief Summary of Experience *</label>
          <textarea class="form-textarea" name="experienceSummary" placeholder="Briefly describe your human resources, consulting, or organizational background..." required></textarea>
          <div class="form-error">Please provide a brief background summary.</div>
        </div>

        <button type="submit" class="btn btn-teal btn-lg" style="width:100%;">Submit Demo Application</button>
      </form>

      <div id="careerFormSuccess" style="display:none; text-align:center; padding:2rem 1rem;">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F9C95" stroke-width="2" style="margin:0 auto 1rem;">
          <circle cx="12" cy="12" r="10"></circle><polyline points="16 12 12 8 8 12"></polyline><line x1="12" y1="16" x2="12" y2="8"></line>
        </svg>
        <h3 style="color:var(--color-dark-navy); margin-bottom:0.5rem;">Application Received (Demo Mode)</h3>
        <p style="color:var(--color-secondary-text); max-width:500px; margin:0 auto;">Thank you for exploring careers with HR CONSULTING COMPANY. This website operates strictly as an illustrative demonstration; no information was transmitted.</p>
      </div>
    </div>
  </div>
</section>
'''
    write_html_page("careers.html", "Careers in Human Capital Advisory | HR Consulting Company",
                    "Explore illustrative career opportunities across our HR consulting practices and submit an expression of interest.", content, "Careers")

def build_contact():
    content = f'''
{get_page_hero("Let's Build a Stronger HR Foundation for Your Business", "Connect with our advisory practice to discuss workforce planning, recruitment, or policies.", [("Contact", "contact.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 gap-xl">
      <!-- Contact Information -->
      <div>
        <span class="section-tag">Direct Inquiry</span>
        <h2>How to Reach Our Advisory Team</h2>
        <p class="lead">Whether you are planning to formalize your company's first employee handbook or evaluate enterprise performance metrics, our consultants are ready to assist.</p>

        <div class="card" style="margin:2rem 0; padding:1.75rem;">
          <div class="footer-contact-item" style="margin-bottom:1.25rem;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:22px; height:22px; color:var(--color-accent-teal); flex-shrink:0;">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
            </svg>
            <div>
              <strong style="color:var(--color-dark-navy);">Phone Enquiries:</strong><br>
              Primary: <a href="tel:0000000000">0000000000</a><br>
              Alternative: <a href="tel:0000000000">0000000000</a>
            </div>
          </div>

          <div class="footer-contact-item" style="margin-bottom:1.25rem;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:22px; height:22px; color:var(--color-accent-teal); flex-shrink:0;">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline>
            </svg>
            <div>
              <strong style="color:var(--color-dark-navy);">Email Address:</strong><br>
              <a href="mailto:demo@example.com">demo@example.com</a>
            </div>
          </div>

          <div class="footer-contact-item" style="margin-bottom:1.25rem;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:22px; height:22px; color:var(--color-accent-teal); flex-shrink:0;">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle>
            </svg>
            <div>
              <strong style="color:var(--color-dark-navy);">Advisory Office Location:</strong><br>
              Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana &ndash; 000000.
            </div>
          </div>

          <div class="footer-contact-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:22px; height:22px; color:var(--color-accent-teal); flex-shrink:0;">
              <circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            <div>
              <strong style="color:var(--color-dark-navy);">Operating Hours:</strong><br>
              Monday &ndash; Saturday: 9:00 AM &ndash; 6:00 PM
            </div>
          </div>
        </div>

        {get_demo_disclaimer("Contact phone numbers, email addresses, and postal addresses displayed above are dummy demonstration placeholders.")}
      </div>

      <!-- Contact Form -->
      <div>
        <div class="form-card">
          <h3 style="margin-bottom:1.5rem; font-size:1.35rem;">Send a Consultation Enquiry</h3>
          <form id="contactEnquiryForm">
            <div class="grid grid-2 gap-md">
              <div class="form-group">
                <label class="form-label">Full Name *</label>
                <input type="text" class="form-control" name="fullName" placeholder="e.g. Alex Morgan" required>
                <div class="form-error">Please enter your name.</div>
              </div>
              <div class="form-group">
                <label class="form-label">Email Address *</label>
                <input type="email" class="form-control" name="email" placeholder="e.g. alex@company.com" required>
                <div class="form-error">Please enter a valid work email.</div>
              </div>
            </div>

            <div class="grid grid-2 gap-md">
              <div class="form-group">
                <label class="form-label">Phone Number *</label>
                <input type="tel" class="form-control" name="phone" placeholder="e.g. 0000000000" required>
                <div class="form-error">Please enter a contact number.</div>
              </div>
              <div class="form-group">
                <label class="form-label">Organization Name *</label>
                <input type="text" class="form-control" name="orgName" placeholder="e.g. Acme Enterprises" required>
                <div class="form-error">Please enter your company name.</div>
              </div>
            </div>

            <div class="grid grid-2 gap-md">
              <div class="form-group">
                <label class="form-label">Industry *</label>
                <select class="form-select" name="industry" required>
                  <option value="">Select industry...</option>
                  <option value="IT & Technology">IT & Technology</option>
                  <option value="Manufacturing">Manufacturing</option>
                  <option value="Healthcare">Healthcare</option>
                  <option value="Education">Education</option>
                  <option value="Retail & E-commerce">Retail & E-commerce</option>
                  <option value="Professional Services">Professional Services</option>
                  <option value="Other">Other Industry</option>
                </select>
                <div class="form-error">Please select your industry.</div>
              </div>
              <div class="form-group">
                <label class="form-label">Employee Count Range *</label>
                <select class="form-select" name="employeeRange" required>
                  <option value="">Select range...</option>
                  <option value="1 - 25">1 - 25 Employees</option>
                  <option value="26 - 75">26 - 75 Employees</option>
                  <option value="76 - 200">76 - 200 Employees</option>
                  <option value="201 - 500">201 - 500 Employees</option>
                  <option value="500+">500+ Employees</option>
                </select>
                <div class="form-error">Please select employee count.</div>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">HR Service Required *</label>
              <select class="form-select" name="serviceRequired" required>
                <option value="">Select primary service...</option>
                <option value="HR Strategy">HR Strategy & Operating Model</option>
                <option value="HR Audit">HR Process Audit & Assessment</option>
                <option value="Talent Acquisition">Talent Acquisition & Sourcing</option>
                <option value="Workforce Planning">Workforce & Headcount Planning</option>
                <option value="HR Policies">HR Policies & Employee Handbook</option>
                <option value="Performance Management">Performance Management & KPIs</option>
                <option value="POSH Consulting">POSH Awareness Consulting</option>
                <option value="HR Technology">HR Technology & HRMS Selection</option>
                <option value="Multiple Services">Multiple Services / Full Package</option>
              </select>
              <div class="form-error">Please select an HR service.</div>
            </div>

            <div class="form-group">
              <label class="form-label">Description of HR Requirements *</label>
              <textarea class="form-textarea" name="description" placeholder="Briefly outline your current workforce challenges and desired outcomes..." required></textarea>
              <div class="form-error">Please describe your requirements.</div>
            </div>

            <button type="submit" class="btn btn-teal btn-lg" style="width:100%;">Submit Consultation Request</button>
          </form>

          <div id="contactFormSuccess" style="display:none; text-align:center; padding:2rem 1rem;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F9C95" stroke-width="2" style="margin:0 auto 1rem;">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <h3 style="color:var(--color-dark-navy); margin-bottom:0.5rem;">Enquiry Submitted (Demo Mode)</h3>
            <p style="color:var(--color-secondary-text); max-width:480px; margin:0 auto;">Thank you for your enquiry. This static demonstration simulates form validation without transmitting or storing information remotely.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
'''
    write_html_page("contact.html", "Contact Us | HR Consulting Company",
                    "Contact our human resources consulting team for strategic HR audits, recruitment planning, policy development, and workforce advisory.", content, "Contact")

def build_book_consultation():
    content = f'''
{get_page_hero("Let's Understand Your HR Requirements", "Step-by-step consultation enquiry to align your workforce needs with tailored advisory solutions.", [("Book Consultation", "book-consultation.html")])}

<section class="section">
  <div class="container container-narrow wizard-container">
    <div class="section-header text-center">
      <span class="section-tag">Interactive Questionnaire</span>
      <h2>Multi-Step HR Consultation Request</h2>
      <p class="section-subtitle">Complete this 6-step assessment to help us prepare a tailored discussion agenda.</p>
    </div>

    <!-- Wizard Progress Bar -->
    <div class="wizard-progress">
      <div class="wizard-progress-bar"></div>
      <div class="wizard-step-node active" data-step="1">
        <div class="wizard-node-circle">1</div>
        <span class="wizard-node-label">Contact</span>
      </div>
      <div class="wizard-step-node" data-step="2">
        <div class="wizard-node-circle">2</div>
        <span class="wizard-node-label">Organization</span>
      </div>
      <div class="wizard-step-node" data-step="3">
        <div class="wizard-node-circle">3</div>
        <span class="wizard-node-label">Services</span>
      </div>
      <div class="wizard-step-node" data-step="4">
        <div class="wizard-node-circle">4</div>
        <span class="wizard-node-label">Challenges</span>
      </div>
      <div class="wizard-step-node" data-step="5">
        <div class="wizard-node-circle">5</div>
        <span class="wizard-node-label">Schedule</span>
      </div>
      <div class="wizard-step-node" data-step="6">
        <div class="wizard-node-circle">6</div>
        <span class="wizard-node-label">Review</span>
      </div>
    </div>

    <div class="form-card">
      <form id="consultationWizardForm">
        <!-- Step 1: Contact Information -->
        <div class="wizard-pane active" data-step="1">
          <h3 style="font-size:1.25rem; margin-bottom:1.5rem; color:var(--color-dark-navy);">Step 1: Your Contact Information</h3>
          <div class="grid grid-2 gap-md">
            <div class="form-group">
              <label class="form-label">Full Name *</label>
              <input type="text" class="form-control" name="fullName" placeholder="e.g. Sarah Jenkins" required>
              <div class="form-error">Please enter your name.</div>
            </div>
            <div class="form-group">
              <label class="form-label">Work Email Address *</label>
              <input type="email" class="form-control" name="email" placeholder="e.g. sarah@enterprise.com" required>
              <div class="form-error">Please enter a valid business email.</div>
            </div>
          </div>
          <div class="grid grid-2 gap-md">
            <div class="form-group">
              <label class="form-label">Phone Number *</label>
              <input type="tel" class="form-control" name="phone" placeholder="e.g. 0000000000" required>
              <div class="form-error">Please enter your contact phone.</div>
            </div>
            <div class="form-group">
              <label class="form-label">Designation / Role *</label>
              <input type="text" class="form-control" name="designation" placeholder="e.g. Managing Director / Founder / HR Head" required>
              <div class="form-error">Please enter your role.</div>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Organization Name *</label>
            <input type="text" class="form-control" name="orgName" placeholder="e.g. Global Tech Solutions" required>
            <div class="form-error">Please enter your organization name.</div>
          </div>
        </div>

        <!-- Step 2: Organization Details -->
        <div class="wizard-pane" data-step="2">
          <h3 style="font-size:1.25rem; margin-bottom:1.5rem; color:var(--color-dark-navy);">Step 2: Organization Profile</h3>
          <div class="grid grid-2 gap-md">
            <div class="form-group">
              <label class="form-label">Industry Sector *</label>
              <select class="form-select" name="industry" required>
                <option value="">Select industry...</option>
                <option value="IT & Technology">IT & Technology</option>
                <option value="Manufacturing">Manufacturing</option>
                <option value="Healthcare">Healthcare</option>
                <option value="Retail & E-commerce">Retail & E-commerce</option>
                <option value="Education">Education</option>
                <option value="Financial Services">Financial Services</option>
                <option value="Professional Services">Professional Services</option>
                <option value="Logistics">Logistics & Supply Chain</option>
                <option value="Other">Other Sector</option>
              </select>
              <div class="form-error">Please select your industry sector.</div>
            </div>
            <div class="form-group">
              <label class="form-label">Current Employee Headcount *</label>
              <select class="form-select" name="employeeCount" required>
                <option value="">Select headcount...</option>
                <option value="1 - 20">1 - 20 Employees</option>
                <option value="21 - 50">21 - 50 Employees</option>
                <option value="51 - 150">51 - 150 Employees</option>
                <option value="151 - 350">151 - 350 Employees</option>
                <option value="350+">350+ Employees</option>
              </select>
              <div class="form-error">Please select your headcount range.</div>
            </div>
          </div>
          <div class="grid grid-2 gap-md">
            <div class="form-group">
              <label class="form-label">Business Development Stage *</label>
              <select class="form-select" name="businessStage" required>
                <option value="">Select stage...</option>
                <option value="Early Growth / Seed">Early Growth / Seed</option>
                <option value="Fast Scaling Scale-Up">Fast Scaling Scale-Up</option>
                <option value="Established Mid-Market">Established Mid-Market</option>
                <option value="Mature Corporate">Mature Corporate</option>
              </select>
              <div class="form-error">Please select business stage.</div>
            </div>
            <div class="form-group">
              <label class="form-label">Existing In-House HR Team *</label>
              <select class="form-select" name="existingHr" required>
                <option value="">Select status...</option>
                <option value="No Dedicated HR (Founder-Led)">No Dedicated HR (Founder-Led)</option>
                <option value="Single HR Generalist / Admin">Single HR Generalist / Admin</option>
                <option value="Small Team (2-4 staff)">Small Team (2-4 staff)</option>
                <option value="Established HR Department">Established HR Department</option>
              </select>
              <div class="form-error">Please select existing HR status.</div>
            </div>
          </div>
        </div>

        <!-- Step 3: HR Requirements -->
        <div class="wizard-pane" data-step="3">
          <h3 style="font-size:1.25rem; margin-bottom:1.5rem; color:var(--color-dark-navy);">Step 3: Services Required (Select All That Apply)</h3>
          <div class="grid grid-2 gap-sm" style="margin-bottom:1.5rem;">
            <label class="form-check">
              <input type="checkbox" name="services" value="HR Strategy">
              <span class="form-check-label">HR Strategy & Operating Model</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="HR Audit">
              <span class="form-check-label">HR Process Audit & Assessment</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="Recruitment">
              <span class="form-check-label">Talent Acquisition & Sourcing</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="Workforce Planning">
              <span class="form-check-label">Workforce & Headcount Planning</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="HR Policies">
              <span class="form-check-label">HR Policies & Employee Handbook</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="Performance Mgmt">
              <span class="form-check-label">Performance Management & OKRs</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="Employee Engagement">
              <span class="form-check-label">Employee Engagement & Surveys</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="Learning & Dev">
              <span class="form-check-label">Learning & Leadership Development</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="POSH Consulting">
              <span class="form-check-label">POSH Workplace Awareness</span>
            </label>
            <label class="form-check">
              <input type="checkbox" name="services" value="HR Tech & Analytics">
              <span class="form-check-label">HRMS Software & People Analytics</span>
            </label>
          </div>
        </div>

        <!-- Step 4: Current HR Challenges -->
        <div class="wizard-pane" data-step="4">
          <h3 style="font-size:1.25rem; margin-bottom:1.5rem; color:var(--color-dark-navy);">Step 4: Current People Management Challenges</h3>
          <div class="form-group">
            <label class="form-label">What is the primary HR or workforce challenge facing your business? *</label>
            <textarea class="form-textarea" name="mainChallenge" placeholder="Describe the friction points, such as high employee turnover, lack of clear job roles, or missing review processes..." required></textarea>
            <div class="form-error">Please describe your main challenge.</div>
          </div>
          <div class="form-group">
            <label class="form-label">What is your desired outcome from this consulting engagement? *</label>
            <input type="text" class="form-control" name="desiredOutcome" placeholder="e.g. Implement structured performance reviews and clear job bands within 90 days." required>
            <div class="form-error">Please specify your target outcome.</div>
          </div>
        </div>

        <!-- Step 5: Consultation Preferences -->
        <div class="wizard-pane" data-step="5">
          <h3 style="font-size:1.25rem; margin-bottom:1.5rem; color:var(--color-dark-navy);">Step 5: Consultation Format & Timing</h3>
          <div class="form-group">
            <label class="form-label">Preferred Consultation Format *</label>
            <div style="display:flex; gap:1.5rem; margin-top:0.5rem;">
              <label class="form-check">
                <input type="radio" name="consultMode" value="Online Video Conference" checked>
                <span class="form-check-label">Online Video Conference (Zoom / Teams)</span>
              </label>
              <label class="form-check">
                <input type="radio" name="consultMode" value="In-Person Advisory Meeting">
                <span class="form-check-label">In-Person Advisory Meeting</span>
              </label>
            </div>
          </div>
          <div class="grid grid-2 gap-md">
            <div class="form-group">
              <label class="form-label">Target Consultation Date *</label>
              <input type="date" class="form-control" name="preferredDate" required>
              <div class="form-error">Please choose a preferred date.</div>
            </div>
            <div class="form-group">
              <label class="form-label">Preferred Time Window *</label>
              <select class="form-select" name="preferredTime" required>
                <option value="">Select time...</option>
                <option value="Morning (10:00 AM - 12:00 PM)">Morning (10:00 AM - 12:00 PM)</option>
                <option value="Afternoon (2:00 PM - 4:00 PM)">Afternoon (2:00 PM - 4:00 PM)</option>
                <option value="Late Afternoon (4:00 PM - 6:00 PM)">Late Afternoon (4:00 PM - 6:00 PM)</option>
              </select>
              <div class="form-error">Please select a time window.</div>
            </div>
          </div>
        </div>

        <!-- Step 6: Review & Submit -->
        <div class="wizard-pane" data-step="6">
          <h3 style="font-size:1.25rem; margin-bottom:1.5rem; color:var(--color-dark-navy);">Step 6: Review Your Consultation Details</h3>
          <p style="font-size:0.875rem; color:var(--color-secondary-text); margin-bottom:1rem;">Please confirm your entries before submitting this consultation enquiry.</p>
          <div id="wizardReviewSummary" style="margin-bottom:1.5rem;"></div>
          <div class="badge badge-demo" style="margin-bottom:1rem;">Frontend Demonstration Simulation &mdash; No Data Will Be Stored</div>
        </div>

        <!-- Navigation Buttons -->
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:2rem; padding-top:1.5rem; border-top:1px solid var(--color-border);">
          <button type="button" id="wizardPrevBtn" class="btn btn-outline" style="display:none;">&larr; Previous Step</button>
          <div style="margin-left:auto; display:flex; gap:1rem;">
            <button type="button" id="wizardNextBtn" class="btn btn-teal">Continue to Next Step &rarr;</button>
            <button type="submit" id="wizardSubmitBtn" class="btn btn-primary btn-lg" style="display:none;">Submit Consultation Request</button>
          </div>
        </div>
      </form>

      <!-- Confirmation Screen -->
      <div id="wizardConfirmationBox" style="display:none; text-align:center; padding:3rem 1.5rem;">
        <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#2F9C95" stroke-width="2" style="margin:0 auto 1.25rem;">
          <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        <h2 style="color:var(--color-dark-navy); margin-bottom:0.75rem;">Consultation Enquiry Received!</h2>
        <p class="lead" style="max-width:560px; margin:0 auto 1.5rem;">This interactive questionnaire operates in <strong>Demonstration Mode</strong>. No personal data was transmitted across the network, and no real calendar appointments were scheduled.</p>
        <div class="badge badge-demo" style="margin-bottom:2rem;">Simulation Completed Successfully</div>
        <div>
          <a href="index.html" class="btn btn-primary">Return to Homepage</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''
    write_html_page("book-consultation.html", "Book an HR Consultation | Multi-Step Assessment Wizard",
                    "Complete our interactive multi-step HR consultation wizard to align your organizational workforce requirements with tailored advisory solutions.", content, "Services")

def build_privacy_policy():
    content = f'''
{get_page_hero("Privacy Policy", "Information regarding website demonstration data, privacy standards, and form handling.", [("Privacy Policy", "privacy-policy.html")])}

<section class="section">
  <div class="container container-narrow">
    <div class="demo-banner" style="margin-bottom:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      <div>
        <strong>Demonstration Notice:</strong>
        <p style="margin-top:0.25rem;">This website is a static demonstration environment built to showcase UI/UX concepts for an HR consulting practice. It is not affiliated with any commercial operating entity. No submitted form data is transmitted or stored on remote servers.</p>
      </div>
    </div>

    <article style="line-height:1.8;">
      <h3>1. Demonstration Nature & Data Transmission</h3>
      <p>All forms on this website (including the Contact Form, Multi-Step Consultation Booking Wizard, and Careers Application Form) operate entirely within client-side JavaScript. When you submit a form, your input is processed locally in your browser to simulate interface interactions. No data is transmitted to an external server, saved to a database, or distributed to third parties.</p>

      <h3>2. Information Entered in Forms</h3>
      <p>Users are advised not to enter real, sensitive personal data, actual corporate financial details, confidential employee records, or personal identification numbers into any fields on this demonstration site.</p>

      <h3>3. Cookies and Local Browser Storage</h3>
      <p>This static website does not set tracking cookies or utilize third-party tracking pixels. Transient session state may be utilized solely for frontend UI components (such as interactive filters and accordion toggles) during your browsing session.</p>

      <h3>4. Analytics & Third-Party Scripts</h3>
      <p>This site does not load external tracking scripts, Google Analytics tags, or social media pixels. All scripts and stylesheets are hosted locally within the website directory.</p>

      <h3>5. Mandatory Legal Review Advisory</h3>
      <p>This privacy policy serves as an illustrative demonstration document. Any enterprise adopting or adapting these materials must ensure their production privacy policies are drafted and reviewed by qualified legal counsel in accordance with applicable data protection laws (such as GDPR, the Digital Personal Data Protection Act (DPDP), and relevant regional statutes).</p>

      <h3>6. Contact Information</h3>
      <p>For any questions regarding this demonstration website, please refer to the dummy contact channels: <a href="mailto:demo@example.com">demo@example.com</a> or telephone 0000000000.</p>
    </article>
  </div>
</section>
'''
    write_html_page("privacy-policy.html", "Privacy Policy | HR Consulting Company",
                    "Read our sample privacy policy detailing static demonstration data handling and browser privacy considerations.", content)

def build_terms():
    content = f'''
{get_page_hero("Terms and Conditions", "Website terms of use, consulting scope boundaries, and intellectual property disclaimers.", [("Terms & Conditions", "terms-and-conditions.html")])}

<section class="section">
  <div class="container container-narrow">
    <div class="demo-banner" style="margin-bottom:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      <div>
        <strong>Demonstration & Legal Disclaimer:</strong>
        <p style="margin-top:0.25rem;">This website and its contents are provided solely for demonstration and conceptual evaluation purposes. The content does not constitute formal legal, financial, or statutory advice and must be reviewed by qualified legal counsel prior to commercial use.</p>
      </div>
    </div>

    <article style="line-height:1.8;">
      <h3>1. Acceptance of Terms</h3>
      <p>By accessing this generic demonstration website for HR CONSULTING COMPANY, you acknowledge that all materials, diagrams, case studies, employee metrics, and service descriptions are presented for illustrative purposes only.</p>

      <h3>2. Scope of HR Consulting Services</h3>
      <p>Descriptions of human resources consulting services (including HR Strategy, HR Audit, Talent Acquisition, Performance Management, and POSH Consulting) represent operational frameworks. Formal advisory engagements require mutually executed master service agreements (MSAs) defining specific deliverables, timelines, confidentiality boundaries, and professional fees.</p>

      <h3>3. No Statutory or Legal Representation</h3>
      <p>HR CONSULTING COMPANY does not provide legal representation, statutory court filings, or guaranteed governmental approvals. Compliance requirements in any jurisdiction (including Indian central and state labor enactments) must be confirmed with practicing legal advocates or accredited statutory auditors.</p>

      <h3>4. Client Responsibilities & Data Confidentiality</h3>
      <p>In actual consulting engagements, clients retain full responsibility for verifying the accuracy of their underlying payroll data, attendance records, and employee information. Formal data processing agreements govern confidential information handling.</p>

      <h3>5. Limitation of Liability</h3>
      <p>Under no circumstances shall the creators of this demonstration site be liable for any direct, indirect, incidental, or consequential damages resulting from the use or reliance upon any templates, checklists, or sample calculations displayed on this website.</p>

      <h3>6. Changes to Terms</h3>
      <p>These terms may be updated periodically for editorial clarity. Continued browsing constitutes acceptance of the modified demonstration terms.</p>
    </article>
  </div>
</section>
'''
    write_html_page("terms-and-conditions.html", "Terms and Conditions | HR Consulting Company",
                    "Review our terms and conditions covering website usage, consulting engagement scope boundaries, and legal disclaimers.", content)

if __name__ == "__main__":
    build_insights()
    build_article_details()
    build_resources()
    build_pricing()
    build_faq()
    build_careers()
    build_contact()
    build_book_consultation()
    build_privacy_policy()
    build_terms()
    print("Information and compliance pages built successfully.")

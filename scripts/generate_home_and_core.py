"""
Generates Homepage, About, Services Overview, Industries, Methodology, Case Studies, Case Study Details, and Team.
"""

from generator_data import register_img, render_img, get_page_hero, get_demo_disclaimer, get_cta_section, write_html_page

def build_home():
    img_hero = register_img(
        filename="hero-hr-consulting-team.webp",
        page="index.html",
        section="Hero Section",
        desc="Senior HR consultants and corporate leadership discussing workforce growth strategies around an executive boardroom table with digital analytics monitors in the background.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional corporate HR consulting team meeting in an ultra-modern glass-walled executive conference room. A diverse group of senior advisors in tailored business attire analyzing organizational structure charts on a sleek digital display. Bright natural daylight streaming through floor-to-ceiling windows, subtle architectural navy accents, premium minimalist aesthetic, photorealistic, cinematic depth of field, sharp focus, 8k resolution.",
        composition="Medium wide shot, rule of thirds with leadership team engaged in collaborative dialogue on the left and subtle digital dashboard charts on the right",
        camera="50mm prime lens, eye-level angle, f/2.8 aperture",
        lighting="Soft natural daylight balanced with subtle interior architectural recessed LED warm lighting",
        bg="Modern corporate glass office overlooking a subtle city skyline with sleek navy and glass elements",
        subjects="4 professional business professionals in crisp smart-business attire in authentic discussion",
        neg_space="Open upper right quadrant suitable for modern contrast"
    )

    img_challenges = register_img(
        filename="hr-workforce-challenges.webp",
        page="index.html",
        section="HR Challenges",
        desc="Business executives reviewing complex workforce organizational charts and HR operational roadmaps.",
        ratio="4:3",
        res="1200x900",
        orientation="Landscape",
        prompt="A focused business leader and an HR consultant reviewing workforce diagnostics and talent assessment documents on a polished oak meeting table. Minimalist aesthetic, high-end corporate setting, laptops, architectural blueprints of organizational workflow, subtle navy and teal tone accents, authentic non-posed expression.",
        composition="Overhead three-quarter angle focusing on strategy documents and engaged discussion",
        camera="85mm lens, slight overhead angle, f/3.2",
        lighting="Even, soft corporate lighting with gentle fill",
        bg="Clean executive strategy office with acoustic felt panels and subtle greenery",
        subjects="Two business leaders examining documents intently",
        neg_space="Left margin uncluttered"
    )

    img_recruitment = register_img(
        filename="recruitment-strategy-overview.webp",
        page="index.html",
        section="Talent Acquisition",
        desc="Talent acquisition specialists conducting a structured candidate interview and competency evaluation session.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="A structured talent acquisition interview taking place in a bright, modern corporate interview room. Two experienced recruiters in smart business wear conducting a conversational yet rigorous talent assessment with candidate, warm professional atmosphere, glass partitions, natural lighting.",
        composition="Eye-level medium shot showing interviewer and candidate interaction",
        camera="50mm lens, f/2.5",
        lighting="Bright ambient daylight with subtle warm fill",
        bg="Contemporary corporate office interior with glass and wood finishes",
        subjects="Three professionals engaged in professional interview",
        neg_space="Upper area with clean architectural lines"
    )

    img_analytics_home = register_img(
        filename="hr-analytics-executive-review.webp",
        page="index.html",
        section="HR Analytics & Dashboards",
        desc="Corporate leadership reviewing people analytics, employee turnover rates, and retention models on a dashboard display.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="A modern people analytics review session. Human resources director pointing to an interactive workforce retention and talent pipeline visual displayed on a wall-mounted ultra-wide screen. Sleek executive boardroom, ambient blue and teal lighting highlights, high-tech modern corporate feel.",
        composition="Wide angle showcasing executive team and luminous display screen",
        camera="35mm lens, f/4.0",
        lighting="Balanced ambient room lighting with glowing screen accent",
        bg="Dark navy executive meeting room with architectural illumination",
        subjects="Business executives analyzing talent analytics",
        neg_space="Right third open for layout breathing room"
    )

    content = f'''
<!-- Hero Section -->
<section class="hero-section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div class="hero-content">
        <div class="hero-tag">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          Strategic Human Capital Advisory
        </div>
        <h1 class="hero-headline">YOUR PEOPLE ARE YOUR STRENGTH. BUILD THE SYSTEMS THAT HELP THEM THRIVE.</h1>
        <p class="hero-description">We help organizations create stronger HR foundations through strategic people management, talent acquisition, workforce planning, employee development, and HR transformation.</p>
        <div class="btn-group">
          <a href="book-consultation.html" class="btn btn-teal btn-lg">Book an HR Consultation</a>
          <a href="services.html" class="btn btn-outline-white btn-lg">Explore Our Services</a>
        </div>
      </div>
      <div>
        {render_img(img_hero)}
      </div>
    </div>
  </div>
</section>

<!-- HR Challenges Section -->
<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Organizational Reality</span>
      <h2>Common Workforce Challenges Growing Businesses Face</h2>
      <p class="section-subtitle">As organizations scale, informal people practices often struggle to support expanding teams, resulting in operational friction and talent risks.</p>
    </div>

    <div class="grid grid-2 gap-lg items-center">
      <div class="grid gap-md">
        <div class="challenge-card">
          <h4>Ambiguous Roles & Reporting Hierarchies</h4>
          <p>Overlapping duties, unclarified authority levels, and vague job descriptions lead to internal bottlenecks and employee frustration.</p>
        </div>
        <div class="challenge-card">
          <h4>Talent Sourcing & Retention Pressure</h4>
          <p>Recruiting top performers without structured evaluation frameworks often causes costly hiring misalignments and early turnover.</p>
        </div>
        <div class="challenge-card">
          <h4>Subjective Performance Evaluations</h4>
          <p>Annual reviews lacking measurable KPIs, transparent metrics, or continuous feedback mechanisms damage team morale and accountability.</p>
        </div>
        <div class="challenge-card">
          <h4>Outdated Policies & Compliance Gaps</h4>
          <p>Informal guidelines that fail to evolve alongside employment regulations create administrative vulnerability and inconsistent treatment.</p>
        </div>
      </div>
      <div>
        {render_img(img_challenges)}
      </div>
    </div>
  </div>
</section>

<!-- Core HR Services Pillars -->
<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Consulting Capabilities</span>
      <h2>Comprehensive HR Consulting Solutions</h2>
      <p class="section-subtitle">From foundational HR audits to comprehensive enterprise transformation, we structure our advisory into four interconnected domains.</p>
    </div>

    <div class="grid grid-4 gap-md">
      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
        </div>
        <h3 class="card-title">HR Strategy & Org Design</h3>
        <p class="card-text">Align workforce structure, executive accountability, and long-term manpower requirements with corporate business targets.</p>
        <div class="card-footer">
          <a href="hr-strategy.html" class="link-arrow">HR Strategy &rarr;</a>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="7" r="4"></circle><path d="M5.5 21a8.38 8.38 0 0 1 13 0"></path><polyline points="16 3.13 18.5 5.5 22 2"></polyline></svg>
        </div>
        <h3 class="card-title">Talent Acquisition & Sourcing</h3>
        <p class="card-text">Establish structured hiring pipelines, candidate assessment rubrics, and employer branding architectures.</p>
        <div class="card-footer">
          <a href="talent-acquisition.html" class="link-arrow">Talent Sourcing &rarr;</a>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        </div>
        <h3 class="card-title">Performance & Engagement</h3>
        <p class="card-text">Formulate transparent appraisal matrices, measurable KRAs, recognition plans, and culture-strengthening frameworks.</p>
        <div class="card-footer">
          <a href="performance-management.html" class="link-arrow">Performance &rarr;</a>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
        </div>
        <h3 class="card-title">Policies, Tech & Advisory</h3>
        <p class="card-text">Develop comprehensive employee handbooks, POSH awareness programs, HRMS technology integration, and HR compliance roadmaps.</p>
        <div class="card-footer">
          <a href="hr-policies.html" class="link-arrow">HR Policies &rarr;</a>
        </div>
      </div>
    </div>

    <div class="text-center" style="margin-top:2.5rem;">
      <a href="services.html" class="btn btn-primary">Browse All 22 HR Consulting Services</a>
    </div>
  </div>
</section>

<!-- People & Workforce Solutions (Recruitment Pipeline Visual) -->
<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Talent Architecture</span>
        <h2>Structured Recruitment & Lifecycle Systems</h2>
        <p class="lead">Hiring effectively requires more than job postings. It demands an intentional pipeline that evaluates competency, cultural alignment, and operational velocity.</p>
        <p>We consult with management teams to build repeatable hiring workflows that minimize interview bias, clarify role expectations, and improve early retention.</p>
        
        <div class="pipeline-container">
          <div class="pipeline-step">
            <span class="pipeline-step-num">Step 1</span>
            <span class="pipeline-step-title">Role Profiling</span>
          </div>
          <div class="pipeline-step">
            <span class="pipeline-step-num">Step 2</span>
            <span class="pipeline-step-title">Targeted Sourcing</span>
          </div>
          <div class="pipeline-step">
            <span class="pipeline-step-num">Step 3</span>
            <span class="pipeline-step-title">Rubric Screening</span>
          </div>
          <div class="pipeline-step">
            <span class="pipeline-step-num">Step 4</span>
            <span class="pipeline-step-title">Structured Interview</span>
          </div>
          <div class="pipeline-step">
            <span class="pipeline-step-num">Step 5</span>
            <span class="pipeline-step-title">Systematic Onboarding</span>
          </div>
        </div>

        <div style="margin-top:1.5rem;">
          <a href="recruitment-consulting.html" class="btn btn-outline">Explore Recruitment Consulting</a>
        </div>
      </div>
      <div>
        {render_img(img_recruitment)}
      </div>
    </div>
  </div>
</section>

<!-- Performance & Analytics Showcase Section -->
<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Data-Driven Insights</span>
      <h2>Clarity Through Workforce Analytics & Metrics</h2>
      <p class="section-subtitle">Transform ambiguous HR observations into measurable insights that empower senior management decision-making.</p>
    </div>

    <div class="grid grid-2 items-center gap-xl">
      <div>
        {render_img(img_analytics_home)}
      </div>
      <div>
        <div class="hr-dashboard">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <span class="dashboard-title">Workforce Metric Overview</span>
            </div>
            <span class="badge badge-demo">Illustrative Demo Data</span>
          </div>
          <div class="dashboard-body">
            <div class="metric-grid" style="grid-template-columns: repeat(2, 1fr); margin-bottom:1.5rem;">
              <div class="metric-card">
                <div class="metric-label">Headcount Monitored</div>
                <div class="metric-value">482</div>
                <div class="metric-sub">&uarr; Sample Workforce Pool</div>
              </div>
              <div class="metric-card">
                <div class="metric-label">Avg. Review Cadence</div>
                <div class="metric-value">Quarterly</div>
                <div class="metric-sub">Synchronized Cycles</div>
              </div>
            </div>

            <div class="chart-card" style="margin-bottom:0;">
              <div class="chart-title">
                <span>Departmental Allocation Ratio</span>
                <span style="font-size:0.75rem; color:var(--color-secondary-text);">Sample Distribution</span>
              </div>
              <div class="bar-row">
                <span class="bar-label">Product & Eng</span>
                <div class="bar-track"><div class="bar-fill" style="width: 42%;"></div></div>
                <span class="bar-value">42%</span>
              </div>
              <div class="bar-row">
                <span class="bar-label">Client Operations</span>
                <div class="bar-track"><div class="bar-fill" style="width: 28%;"></div></div>
                <span class="bar-value">28%</span>
              </div>
              <div class="bar-row">
                <span class="bar-label">Sales & Marketing</span>
                <div class="bar-track"><div class="bar-fill" style="width: 18%;"></div></div>
                <span class="bar-value">18%</span>
              </div>
              <div class="bar-row">
                <span class="bar-label">General & Admin</span>
                <div class="bar-track"><div class="bar-fill" style="width: 12%;"></div></div>
                <span class="bar-value">12%</span>
              </div>
            </div>
          </div>
        </div>
        {get_demo_disclaimer("Dashboard metrics represent a non-operational sample model demonstrating visual reporting concepts.")}
      </div>
    </div>
  </div>
</section>

<!-- Methodology 5-Stage Preview -->
<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Our Approach</span>
      <h2>The 5-Stage HR Consulting Methodology</h2>
      <p class="section-subtitle">A disciplined advisory framework ensuring interventions address root organizational causes rather than surface symptoms.</p>
    </div>

    <div class="methodology-grid">
      <div class="methodology-col">
        <span class="methodology-stage-num">Stage 1</span>
        <h4 class="methodology-stage-title">Understand</h4>
        <p>Review business goals, existing operational headcount, and specific workplace pain points.</p>
      </div>
      <div class="methodology-col">
        <span class="methodology-stage-num">Stage 2</span>
        <h4 class="methodology-stage-title">Assess</h4>
        <p>Examine current HR documentation, recruitment methods, review cycles, and policy adherence.</p>
      </div>
      <div class="methodology-col stage-active">
        <span class="methodology-stage-num">Stage 3</span>
        <h4 class="methodology-stage-title">Diagnose</h4>
        <p>Isolate structural bottlenecks, role ambiguities, and workflow inefficiencies across departments.</p>
      </div>
      <div class="methodology-col">
        <span class="methodology-stage-num">Stage 4</span>
        <h4 class="methodology-stage-title">Design</h4>
        <p>Formulate tailored policy manuals, performance rubrics, job architectures, and action plans.</p>
      </div>
      <div class="methodology-col">
        <span class="methodology-stage-num">Stage 5</span>
        <h4 class="methodology-stage-title">Support</h4>
        <p>Assist internal managers with implementation, training workshops, and recurring review cadences.</p>
      </div>
    </div>

    <div class="text-center">
      <a href="methodology.html" class="btn btn-outline">Read Full Methodology Breakdown &rarr;</a>
    </div>
  </div>
</section>

<!-- Featured Illustrative Case Studies -->
<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Practical Applications</span>
      <h2>Illustrative HR Engagement Scenarios</h2>
      <p class="section-subtitle">Examine conceptual case studies highlighting common organizational challenges and structured advisory solutions.</p>
    </div>

    <div class="grid grid-3 gap-md">
      <div class="card">
        <span class="badge badge-demo" style="width:fit-content; margin-bottom:0.75rem;">Illustrative Demo Case Study</span>
        <h3 class="card-title">Engineering Scale-Up: Role Architecture & Grading</h3>
        <p class="card-text">A fast-growing technical enterprise required structured job levels, competency definitions, and transparent compensation bands for 150+ staff.</p>
        <div class="card-footer">
          <a href="case-study-details.html" class="link-arrow">View Case Study &rarr;</a>
        </div>
      </div>

      <div class="card">
        <span class="badge badge-demo" style="width:fit-content; margin-bottom:0.75rem;">Illustrative Demo Case Study</span>
        <h3 class="card-title">Manufacturing Plant: Shift & Attendance Policy Standardization</h3>
        <p class="card-text">Consolidating disjointed shop-floor attendance practices into a compliant, fair, and transparent workforce policy manual.</p>
        <div class="card-footer">
          <a href="case-study-details.html" class="link-arrow">View Case Study &rarr;</a>
        </div>
      </div>

      <div class="card">
        <span class="badge badge-demo" style="width:fit-content; margin-bottom:0.75rem;">Illustrative Demo Case Study</span>
        <h3 class="card-title">Corporate Services: KPI & Performance Appraisal Restructure</h3>
        <p class="card-text">Transitioning an organization from subjective annual reviews to objective quarterly performance agreements aligned with departmental goals.</p>
        <div class="card-footer">
          <a href="case-study-details.html" class="link-arrow">View Case Study &rarr;</a>
        </div>
      </div>
    </div>
    
    <div class="text-center" style="margin-top:2rem;">
      <a href="case-studies.html" class="btn btn-primary">Browse All Case Studies</a>
    </div>
  </div>
</section>

{get_cta_section()}
'''
    write_html_page("index.html", "Strategic HR Consulting & Human Capital Advisory",
                    "We help organizations build stronger HR systems, recruit talent, improve employee performance, establish HR policies, and align workforce strategies.", content, "Home")

def build_about():
    img_about_lead = register_img(
        filename="about-consulting-philosophy.webp",
        page="about.html",
        section="Company Philosophy",
        desc="Senior HR management consultants analyzing human capital blueprints in a corporate strategy suite.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional corporate strategy session focusing on workforce architecture. Senior HR consultants reviewing structural organizational frameworks on interactive tablets and architectural planning documents. Bright, clean corporate office, sophisticated navy and natural timber accents, high quality photography, soft directional lighting.",
        composition="Medium wide shot of three advisors in active strategy review",
        camera="50mm lens, f/2.8",
        lighting="Natural ambient morning sunlight",
        bg="Minimalist modern conference room with floor-to-ceiling glass",
        subjects="Three corporate professionals in business attire",
        neg_space="Right third clear for text balance"
    )

    img_mission = register_img(
        filename="about-mission-collaboration.webp",
        page="about.html",
        section="Our Approach & Mission",
        desc="A collaborative discussion between senior workforce advisors and business operations executives.",
        ratio="4:3",
        res="1200x900",
        orientation="Landscape",
        prompt="A collaborative workshop between management consultants and department heads in a corporate breakout room. People working together around a whiteboard with flowcharts illustrating employee lifecycle stages, warm professional atmosphere, candid authentic interaction.",
        composition="Horizontal frame with team standing around discussion whiteboard",
        camera="35mm lens, f/3.5",
        lighting="Even soft corporate lighting",
        bg="Contemporary corporate workshop studio with whiteboards and monitors",
        subjects="Four business professionals collaborating actively",
        neg_space="Upper section balanced"
    )

    content = f'''
{get_page_hero("Helping Organizations Build Stronger People Practices", "Strategic human capital consulting designed to build scalable, compliant, and performance-driven workplace foundations.", [("About Us", "about.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">About The Practice</span>
        <h2>A Professional People-First Approach Grounded in Business Reality</h2>
        <p class="lead">An organization's capacity to execute its strategic objectives depends fundamentally on the quality, clarity, and engagement of its workforce.</p>
        <p>HR CONSULTING COMPANY operates as an independent human resources consulting and human capital advisory firm. We work closely with startup founders, managing directors, and corporate leaders to transition informal, reactive HR operations into structured, scalable organizational systems.</p>
        <p>Our philosophy is grounded in practicality: policies must be understandable, performance metrics must be fair and measurable, and recruitment processes must consistently reflect organizational values.</p>
      </div>
      <div>
        {render_img(img_about_lead)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="grid grid-3 gap-lg">
      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>
        </div>
        <h3 class="card-title">Our Philosophy</h3>
        <p class="card-text">People management is not merely an administrative function—it is a core engine of enterprise value creation. By replacing guesswork with structured frameworks, organizations unlock employee potential and mitigate systemic risks.</p>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
        </div>
        <h3 class="card-title">Our Mission</h3>
        <p class="card-text">To empower growing and established enterprises with tailored HR systems, objective workforce diagnostic tools, structured recruitment methodologies, and legally aligned employee policies.</p>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
        </div>
        <h3 class="card-title">Our Vision</h3>
        <p class="card-text">To be recognized as a benchmark advisory firm for practical workforce excellence, enabling workplaces where accountability, mutual respect, and strategic alignment drive sustainable prosperity.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        {render_img(img_mission)}
      </div>
      <div>
        <span class="section-tag">Core Tenets</span>
        <h2>How We Approach Organizational Effectiveness</h2>
        <div class="deliverables-list">
          <ul>
            <li><strong>Business-Aligned HR Strategy:</strong> Structuring human capital priorities directly around quarterly and multi-year company milestones.</li>
            <li><strong>Practical HR Systems:</strong> Replacing complex bureaucratic procedures with lean, intuitive tools that managers and employees actually use.</li>
            <li><strong>Talent Development & Capability Building:</strong> Creating systematic pathways for continuous professional learning, mentoring, and internal succession.</li>
            <li><strong>Long-Term Workforce Planning:</strong> Analyzing skill trends and headcount costs to ensure organizations recruit ahead of growth bottlenecks.</li>
          </ul>
        </div>
        {get_demo_disclaimer("This overview outlines our generic consulting philosophy. Specific advisory engagements are governed by formal contracts.")}
      </div>
    </div>
  </div>
</section>

{get_cta_section("Discuss Your Workforce Priorities With Us", "Connect with our advisory practice to explore how structured HR consulting can strengthen your leadership team.")}
'''
    write_html_page("about.html", "About Us | Helping Organizations Build Stronger People Practices",
                    "Learn about our generic HR consulting philosophy, mission, vision, and people-first approach to organizational effectiveness.", content, "About")

def build_services_overview():
    services_list = [
        ("HR Strategy", "hr-strategy.html", "Align workforce planning, organizational structure, and operational capability with corporate expansion goals.", "Strategic misalignment, unfocused headcount investments.", "HR Operating Model, Strategic Workforce Roadmap, Executive Scorecard."),
        ("HR Audit", "hr-audit.html", "Systematic review of employee files, compliance records, hiring workflows, and internal procedures.", "Process redundancies, documentation gaps, statutory exposure.", "Comprehensive Audit Scorecard, Gap Analysis Matrix, Remediation Roadmap."),
        ("Talent Acquisition", "talent-acquisition.html", "Design candidate sourcing frameworks, assessment rubrics, and employer branding channels.", "Prolonged vacancies, bad hires, weak candidate experience.", "Recruitment Pipeline Architecture, Interview Rubrics, Sourcing Guide."),
        ("Recruitment Consulting", "recruitment-consulting.html", "Optimize internal hiring workflows, recruiter tracking metrics, and manager interview readiness.", "Inconsistent interview quality, recruiter coordination delays.", "Interview Guides, SLA Templates, Recruiter Training Modules."),
        ("Workforce Planning", "workforce-planning.html", "Forecast future headcount needs, identify critical skill gaps, and model departmental manpower costs.", "Over-hiring, unexpected talent shortages, inflated wage bills.", "Workforce Forecast Model, Skills Gap Matrix, Capacity Plan."),
        ("Organizational Development", "organizational-development.html", "Restructure departments, clarify reporting lines, and establish job architecture bandings.", "Turf wars, duplicated tasks, ambiguous career paths.", "Job Architecture Bands, Organization Charts, Responsibility RACI Matrix."),
        ("HR Policies & Documentation", "hr-policies.html", "Draft clear, modern, and legally referenced workplace policies covering all employment facets.", "Arbitrary manager decisions, outdated rules, workplace friction.", "Custom HR Policy Library, SOP Manuals, Implementation Checklist."),
        ("Employee Handbook", "employee-handbook.html", "Compile an engaging, professional handbook outlining company culture, expectations, and benefits.", "Poor onboarding communication, cultural disconnects.", "Complete Employee Handbook Template, Culture Briefing, Sign-Off Forms."),
        ("Performance Management", "performance-management.html", "Formulate goal-setting frameworks, OKR/KPI structures, and appraisal review cycles.", "Subjective annual evaluations, demotivated top talent.", "Performance Review Framework, KPI Catalogs, Manager Coaching Guide."),
        ("Employee Engagement", "employee-engagement.html", "Design listening surveys, feedback loops, and recognition systems that boost workplace morale.", "High unprompted turnover, low employee enthusiasm, quiet quitting.", "Engagement Survey Instrument, Action Plan Blueprint, Recognition Framework."),
        ("Learning & Development", "learning-development.html", "Conduct training needs assessments and structure customized professional capability paths.", "Skill stagnation, productivity plateaus, lack of development.", "Training Needs Assessment, Annual Training Calendar, L&D Scorecards."),
        ("Leadership Development", "leadership-development.html", "Build manager coaching frameworks, decision-making workshops, and supervisory training.", "First-time manager struggles, poor managerial communication.", "Manager Capability Framework, Supervisory Toolkits, 1-on-1 Guides."),
        ("Compensation & Benefits", "compensation-benefits.html", "Benchmark compensation structures, job grading levels, and performance incentive plans.", "Uncompetitive salaries, wage compression, high compensation attrition.", "Salary Grade Hierarchy, Variable Incentive Plan, Total Rewards Model."),
        ("Payroll Advisory", "payroll-advisory.html", "Assess payroll calculation workflows, statutory coordination, and attendance data pipelines.", "Payroll errors, delayed disbursals, attendance reconciliation lags.", "Payroll Process Flowchart, Reconciliation Checklists, Vendor SLA Guide."),
        ("HR Compliance Advisory", "hr-compliance.html", "Review statutory register requirements, record keeping, and employment law adherence.", "Inspection penalties, missing statutory filings, legal exposure.", "HR Compliance Calendar, Statutory Register Audit, Remediation Plan."),
        ("POSH Consulting", "posh-consulting.html", "Establish Prevention of Sexual Harassment (POSH) awareness programs and IC operational guidance.", "Lack of workplace awareness, improper grievance handling.", "POSH Policy Blueprint, IC Operational Guide, Employee Awareness Module."),
        ("Employee Relations", "employee-relations.html", "Design fair grievance mechanisms, disciplinary protocols, and conflict resolution systems.", "Unresolved employee friction, formal disputes, toxic subcultures.", "Grievance Redressal SOP, Conflict Escalation Matrix, Conduct Protocols."),
        ("Succession Planning", "succession-planning.html", "Map critical roles, identify high-potential successors, and structure talent transition plans.", "Sudden leadership vacancies, institutional memory loss.", "9-Box Talent Matrix, Critical Role Continuity Plan, Mentorship Guide."),
        ("Change Management", "change-management.html", "Guide organizations through restructuring, mergers, leadership transitions, and new HR systems.", "Employee resistance, communication breakdown, dropped productivity.", "Change Impact Assessment, Stakeholder Engagement Plan, Transition Roadmap."),
        ("HR Technology", "hr-technology.html", "Evaluate, select, and configure HRMS, applicant tracking, and performance software tools.", "Manual paperwork, fragmented software tools, low digital adoption.", "HRMS Requirements Matrix, Vendor Evaluation Rubric, Rollout Plan."),
        ("HR Analytics", "hr-analytics.html", "Implement workforce reporting dashboards, turnover predictive metrics, and headcount analytics.", "Lack of people data, inability to measure HR ROI.", "HR KPI Dashboard Specifications, Retention Metrics, Executive Reports."),
        ("HR Outsourcing", "hr-outsourcing.html", "Provide scalable outsourced HR operational support for daily employee lifecycle administration.", "Overburdened founders, administrative burnout, lack of HR bandwidth.", "Managed HR SLA Agreement, Employee Onboarding Coordination, Admin SOPs.")
    ]

    cards_html = ""
    for title, link, desc, challenges, deliv in services_list:
        cards_html += f'''
      <div class="service-full-card">
        <h3 class="card-title" style="margin-bottom:0.5rem;"><a href="{link}">{title}</a></h3>
        <p class="card-text">{desc}</p>
        <div style="margin: 0.75rem 0;">
          <strong style="font-size:0.8125rem; color:var(--color-primary-navy);">Business Challenges Addressed:</strong>
          <p style="font-size:0.84rem; margin-top:0.25rem;">{challenges}</p>
        </div>
        <div style="margin-bottom:1rem;">
          <strong style="font-size:0.8125rem; color:var(--color-primary-navy);">Typical Deliverables:</strong>
          <ul class="deliverables-list" style="margin-top:0.25rem;">
            <li>{deliv}</li>
          </ul>
        </div>
        <div class="card-footer">
          <a href="{link}" class="link-arrow">Detailed Service Scope &rarr;</a>
          <a href="book-consultation.html" class="btn btn-teal btn-sm">Consult on this</a>
        </div>
      </div>'''

    content = f'''
{get_page_hero("Complete HR Consulting Solutions for Growing Organizations", "A full suite of strategic, operational, and technical human capital advisory services tailored to your business scale.", [("Services", "services.html")])}

<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Practices & Capabilities</span>
      <h2>All 22 Human Capital Advisory Services</h2>
      <p class="section-subtitle">Every service is delivered with practical templates, tailored implementation guidance, and rigorous professional standards.</p>
    </div>

    <div class="grid grid-2 gap-lg">
      {cards_html}
    </div>
  </div>
</section>

{get_cta_section()}
'''
    write_html_page("services.html", "Complete HR Consulting Solutions for Growing Organizations",
                    "Browse our comprehensive suite of 22 HR consulting services including HR strategy, audit, talent acquisition, performance management, and compliance.", content, "Services")

def build_industries():
    industries_list = [
        ("IT & Technology", "industries-it-technology.webp", "Rapid headcount scaling, hyper-competitive tech talent sourcing, and high employee turnover in developer teams.", "Technical competency rubrics, sprint-aligned review frameworks, and retention incentives."),
        ("Manufacturing", "industries-manufacturing.webp", "Shift-work management, attendance tracking across factory units, and shop-floor safety compliance.", "Structured shift rosters, disciplinary standard operating procedures, and safety protocol training."),
        ("Healthcare", "industries-healthcare.webp", "24/7 staff scheduling, strict credential verification, clinical burnout, and high nurse attrition.", "Credential tracking workflows, burnout mitigation programs, and rapid-hire clinical pipelines."),
        ("Education", "industries-education.webp", "Academic year recruitment cycles, faculty evaluation frameworks, and institutional accreditation standards.", "Faculty appraisal rubrics, semester onboarding checklists, and academic leadership training."),
        ("Real Estate", "industries-real-estate.webp", "Incentive-heavy compensation models, volatile sales cycles, and decentralized site agent teams.", "Commission structure modeling, regional sales hiring rubrics, and field conduct standards."),
        ("Retail", "industries-retail.webp", "High seasonal store turnover, cash handling compliance, and frontline customer service training.", "Rapid frontline onboarding kits, retail incentive structures, and store manager supervisory toolkits."),
        ("E-commerce", "industries-ecommerce.webp", "Warehouse logistics staffing spikes, fast seasonal ramp-up, and vendor contractor oversight.", "Contractor compliance tracking, warehouse productivity metrics, and rapid-hire pipelines."),
        ("Logistics & Supply Chain", "industries-logistics.webp", "Driver and dispatcher retention, remote fleet coordination, and regional compliance variations.", "Route incentive structures, remote communication frameworks, and safety guidelines."),
        ("Hospitality", "industries-hospitality.webp", "High frontline attrition, guest service standards, seasonal occupancy shifts, and tips coordination.", "Service standard handbooks, hospitality leadership development, and shift management SOPs."),
        ("Construction", "industries-construction.webp", "Project-based workforce mobilization, site safety protocol documentation, and subcontractor coordination.", "Site safety compliance audits, contractor onboarding guides, and project demobilization SOPs."),
        ("Professional Services", "industries-professional-services.webp", "Billable hour utilization tracking, partner track succession planning, and knowledge worker retention.", "Career progression ladders, utilization-linked incentives, and competency assessment frameworks."),
        ("Financial Services", "industries-financial-services.webp", "Strict background check protocols, regulatory oversight, and complex variable bonus schemes.", "Comprehensive background verification protocols, compliance calendars, and bonus plan modeling."),
        ("Startups & Seed Ventures", "industries-startups.webp", "Absence of formal HR policies, first 50 hires chaos, equity compensation, and culture definition.", "Foundational HR kits, scalable offer letter templates, and initial employee handbook development."),
        ("Corporate Organizations", "industries-corporate.webp", "Matrix reporting complexities, legacy HRMS transitions, executive succession, and change resistance.", "Enterprise job architecture bandings, succession planning matrices, and change management roadmaps.")
    ]

    cards_html = ""
    for name, img_name, challenge, sol in industries_list:
        img_item = register_img(
            filename=img_name,
            page="industries.html",
            section=f"Industry: {name}",
            desc=f"Professional workplace environment representing the {name} sector with modern workforce collaboration.",
            ratio="16:9",
            res="1280x720",
            orientation="Landscape",
            prompt=f"Professional, authentic corporate photography depicting the {name} industry workplace. Diverse, engaged team members working in a high-quality modern commercial setting, natural lighting, premium documentary aesthetic, crisp detail.",
            composition="Eye-level medium shot showing industry-specific context and team interaction",
            camera="50mm lens, f/2.8",
            lighting="Natural clean lighting matching modern industry environment",
            bg=f"Authentic modern {name} workplace interior",
            subjects="Industry professionals engaged in focused work",
            neg_space="Upper area clean for visual stability"
        )

        cards_html += f'''
      <div class="card" style="padding:1.5rem;">
        {render_img(img_item, "style='margin-bottom:1.25rem;'")}
        <h3 class="card-title">{name}</h3>
        <div style="margin-bottom:0.75rem;">
          <strong style="font-size:0.8125rem; color:var(--color-primary-navy);">Workforce Challenges:</strong>
          <p style="font-size:0.875rem; margin-top:0.25rem;">{challenge}</p>
        </div>
        <div style="margin-bottom:1.25rem;">
          <strong style="font-size:0.8125rem; color:var(--color-accent-teal);">Targeted HR Solutions:</strong>
          <p style="font-size:0.875rem; margin-top:0.25rem;">{sol}</p>
        </div>
        <div class="card-footer">
          <a href="services.html" class="link-arrow">Explore Sector Solutions &rarr;</a>
        </div>
      </div>'''

    content = f'''
{get_page_hero("Dedicated HR Consulting for Diverse Industry Sectors", "Every sector faces unique workforce dynamics, regulatory considerations, and talent availability patterns.", [("Industries", "industries.html")])}

<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Sector Expertise</span>
      <h2>Tailored Human Capital Solutions Across 14 Industries</h2>
      <p class="section-subtitle">We adapt proven HR frameworks to address the specific regulatory, shift, and talent nuances of your business model.</p>
    </div>

    {get_demo_disclaimer("Industry profiles describe generalized workforce advisory patterns. Client engagements are tailored to individual enterprise operational models.")}

    <div class="grid grid-2 gap-lg" style="margin-top:2rem;">
      {cards_html}
    </div>
  </div>
</section>

{get_cta_section("Schedule an Industry-Focused Consultation", "Our advisors are ready to review your sector-specific workforce requirements.")}
'''
    write_html_page("industries.html", "Industries We Support | Specialized HR Advisory Solutions",
                    "Explore tailored HR consulting and workforce solutions across 14 diverse industries including Technology, Manufacturing, Healthcare, and Retail.", content, "Industries")

def build_methodology():
    img_method_diagram = register_img(
        filename="methodology-consulting-process.webp",
        page="methodology.html",
        section="Consulting Methodology",
        desc="Senior HR management consultants and executive leadership mapping out a structured 5-stage transformation roadmap on an architectural digital strategy board.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="A high-level corporate advisory session in a sleek executive design studio. Strategic HR management consultants and senior corporate clients collaborating around an interactive timeline wall displaying five discrete consulting phases. Sophisticated corporate environment, warm architectural lighting, rich navy palette, premium realistic aesthetic.",
        composition="Wide horizontal framing showing consultants in collaborative analysis",
        camera="35mm lens, f/3.2",
        lighting="Directional soft illumination highlighting the strategic wall map",
        bg="Minimalist executive briefing room with acoustic felt and wood paneling",
        subjects="Three senior consultants and two client executives",
        neg_space="Left upper section uncluttered"
    )

    content = f'''
{get_page_hero("A Practical Approach to Building Stronger HR Systems", "A structured, evidence-based five-stage consulting methodology that ensures sustainable people practices.", [("Our Approach", "methodology.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Disciplined Advisory</span>
        <h2>How We Deliver Measurable Workforce Improvement</h2>
        <p class="lead">Successful HR transformations do not rely on generic templates or isolated fixes. They require an objective assessment of systemic operational causes followed by structured execution.</p>
        <p>Our five-stage methodology provides a predictable, collaborative framework that aligns executive leadership, operational managers, and people practices from inception to long-term adoption.</p>
      </div>
      <div>
        {render_img(img_method_diagram)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Framework Overview</span>
      <h2>The 5 Stages of Our HR Consulting Process</h2>
      <p class="section-subtitle">Each stage delivers transparent milestones, documented artifacts, and actionable managerial clarity.</p>
    </div>

    <div class="grid gap-lg">
      <div class="card" style="border-left: 5px solid var(--color-primary-navy);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
          <span class="badge badge-navy">Stage 1</span>
          <span style="font-size:0.8125rem; font-weight:600; color:var(--color-secondary-text);">Initial Discovery Phase</span>
        </div>
        <h3 class="card-title">Understand: Strategic Alignment & Discovery</h3>
        <p class="card-text">We interview key founders, managing directors, and department leaders to understand overall commercial priorities, historical organizational challenges, and future headcount objectives.</p>
        <div class="grid grid-3 gap-md" style="margin-top:1rem;">
          <div>
            <strong style="font-size:0.8125rem;">Core Objective:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Map business targets directly against current workforce capabilities.</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Key Questions:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">What are the growth bottlenecks? Where are manager friction points?</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Deliverables:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Engagement Charter, Stakeholder Interview Synthesis, Scope Document.</p>
          </div>
        </div>
      </div>

      <div class="card" style="border-left: 5px solid var(--color-secondary-blue);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
          <span class="badge badge-navy">Stage 2</span>
          <span style="font-size:0.8125rem; font-weight:600; color:var(--color-secondary-text);">Operational Assessment</span>
        </div>
        <h3 class="card-title">Assess: Process & Documentation Review</h3>
        <p class="card-text">We inspect employee lifecycle documentation, employment agreements, leave records, appraisal forms, and hiring workflows against industry standards.</p>
        <div class="grid grid-3 gap-md" style="margin-top:1rem;">
          <div>
            <strong style="font-size:0.8125rem;">Core Objective:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Evaluate process rigor, data consistency, and documentation hygiene.</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Key Questions:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Are existing policies applied consistently? Are employee records centralized?</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Deliverables:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">HR Baseline Audit Scorecard, Document Inventory, Risk Heatmap.</p>
          </div>
        </div>
      </div>

      <div class="card" style="border-left: 5px solid var(--color-accent-teal);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
          <span class="badge badge-teal">Stage 3</span>
          <span style="font-size:0.8125rem; font-weight:600; color:var(--color-secondary-text);">Root-Cause Analysis</span>
        </div>
        <h3 class="card-title">Diagnose: Gap Identification & Prioritization</h3>
        <p class="card-text">Our advisors synthesize assessment observations into clear systemic findings, categorizing items by organizational impact and implementation complexity.</p>
        <div class="grid grid-3 gap-md" style="margin-top:1rem;">
          <div>
            <strong style="font-size:0.8125rem;">Core Objective:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Isolate systemic weaknesses rather than treating superficial symptoms.</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Key Questions:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Why is turnover concentrated in specific teams? Why do reviews stall?</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Deliverables:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Comprehensive Diagnostic Report, Priority Matrix, Executive Briefing.</p>
          </div>
        </div>
      </div>

      <div class="card" style="border-left: 5px solid var(--color-muted-gold);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
          <span class="badge badge-demo">Stage 4</span>
          <span style="font-size:0.8125rem; font-weight:600; color:var(--color-secondary-text);">System Architecture</span>
        </div>
        <h3 class="card-title">Design: Framework & Policy Formulation</h3>
        <p class="card-text">We author customized HR policies, job grading bands, recruitment assessment rubrics, employee handbooks, and performance review instruments.</p>
        <div class="grid grid-3 gap-md" style="margin-top:1rem;">
          <div>
            <strong style="font-size:0.8125rem;">Core Objective:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Build custom, scalable, and intuitive people systems for daily operations.</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Key Questions:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Are policies easy for line managers to administer? Are metrics transparent?</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Deliverables:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Employee Handbook, Job Banding Manual, Appraisal Forms, SOP Guides.</p>
          </div>
        </div>
      </div>

      <div class="card" style="border-left: 5px solid var(--color-success);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
          <span class="badge badge-teal">Stage 5</span>
          <span style="font-size:0.8125rem; font-weight:600; color:var(--color-secondary-text);">Execution Enablement</span>
        </div>
        <h3 class="card-title">Support: Implementation & Manager Enablement</h3>
        <p class="card-text">We facilitate managerial training workshops, guide rollout communications, and conduct 30/60/90-day progress checks to ensure adoption.</p>
        <div class="grid grid-3 gap-md" style="margin-top:1rem;">
          <div>
            <strong style="font-size:0.8125rem;">Core Objective:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Embed new behaviors and procedures into daily operational habits.</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Key Questions:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Are teams completing reviews on schedule? Are candidates scored via rubrics?</p>
          </div>
          <div>
            <strong style="font-size:0.8125rem;">Deliverables:</strong>
            <p style="font-size:0.84rem; margin-top:0.25rem;">Manager Training Deck, Rollout Timeline, Post-Implementation Audit.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Experience Our Structured Methodology", "Request an introductory consultation to discuss how our 5-stage process applies to your current business objectives.")}
'''
    write_html_page("methodology.html", "Our Approach | The 5-Stage HR Consulting Methodology",
                    "Learn about our five-stage HR consulting process: Understand, Assess, Diagnose, Design, and Support for building scalable people systems.", content, "Our Approach")

def build_case_studies():
    case_list = [
        ("HR Foundation Development Demo", "hr-strategy", "Mid-sized technology company transitioning from 40 to 120 employees without formal HR infrastructure.", "Established standardized job bands, an employee handbook, and an initial review cycle."),
        ("Recruitment Process Improvement Demo", "recruitment", "High-growth financial services startup experiencing high candidate fallout during technical interviews.", "Redesigned interview scoring rubrics, formalized hiring SLAs, and trained 12 hiring managers."),
        ("Workforce Planning Framework Demo", "workforce-planning", "Multi-site manufacturing firm needing a disciplined 18-month headcount forecasting model.", "Built role capacity spreadsheets, evaluated skill redundancies, and stabilized manpower budgeting."),
        ("Performance Management System Demo", "performance", "Professional advisory practice seeking to replace subjective annual bonuses with quarterly goal scorecards.", "Formulated clear KRA matrices, 360 peer feedback guidelines, and manager evaluation templates."),
        ("Organizational Structure Review Demo", "org-dev", "Enterprise logistics group addressing overlapping authority and ambiguous middle-management reporting lines.", "Redesigned organizational chart, developed RACI accountability matrices, and clarified title bands."),
        ("Employee Engagement Framework Demo", "engagement", "Growing retail chain facing unexpected store manager turnover and declining employee survey sentiment.", "Implemented quarterly pulse listening surveys, store recognition programs, and career milestone paths."),
        ("HR Analytics Dashboard Demo", "analytics", "Corporate holding company needing unified headcount, turnover, and recruitment velocity reporting.", "Defined standardized HR KPI definitions, automated monthly summary dashboards, and trained internal HR."),
        ("HR Policy Documentation Demo", "policies", "Rapidly scaling healthcare provider requiring comprehensive operational SOPs across 4 clinic locations.", "Compiled a compliant HR policy manual, standardized leave protocols, and created onboarding checklists.")
    ]

    cards_html = ""
    for title, cat, challenge, sol in case_list:
        cards_html += f'''
      <div class="card filterable-item" data-category="{cat} all">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.75rem;">
          <span class="badge badge-demo">Illustrative Demo Case Study</span>
          <span class="badge badge-navy" style="font-size:0.7rem;">{cat.upper()}</span>
        </div>
        <h3 class="card-title" style="font-size:1.15rem;"><a href="case-study-details.html">{title}</a></h3>
        <p class="card-text" style="font-size:0.875rem;"><strong>Context:</strong> {challenge}</p>
        <p class="card-text" style="font-size:0.875rem; margin-top:0.25rem;"><strong>Advisory Intervention:</strong> {sol}</p>
        <div class="card-footer">
          <a href="case-study-details.html" class="link-arrow">View Detailed Framework &rarr;</a>
        </div>
      </div>'''

    content = f'''
{get_page_hero("Illustrative HR Consulting Case Studies", "Representative project scenarios showcasing our diagnostic approaches, recommended frameworks, and implementation methods.", [("Case Studies", "case-studies.html")])}

<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Scenario Gallery</span>
      <h2>Explore Conceptual Engagement Blueprints</h2>
      <p class="section-subtitle">Review representative HR challenges across different functional areas and how structured consulting frameworks resolve them.</p>
    </div>

    {get_demo_disclaimer("Case studies presented below are conceptual demonstration scenarios. They do not represent actual client accounts, confidential proprietary data, or guaranteed commercial results.")}

    <div class="filter-bar" data-target-container=".filterable-grid" style="margin-top:2rem;">
      <button class="filter-btn active" data-filter="all">All Practice Areas</button>
      <button class="filter-btn" data-filter="hr-strategy">HR Strategy</button>
      <button class="filter-btn" data-filter="recruitment">Recruitment</button>
      <button class="filter-btn" data-filter="workforce-planning">Workforce Planning</button>
      <button class="filter-btn" data-filter="performance">Performance</button>
      <button class="filter-btn" data-filter="org-dev">Org Development</button>
      <button class="filter-btn" data-filter="analytics">HR Analytics</button>
      <button class="filter-btn" data-filter="policies">HR Policies</button>
    </div>

    <div class="grid grid-3 gap-lg filterable-grid">
      {cards_html}
    </div>
  </div>
</section>

{get_cta_section()}
'''
    write_html_page("case-studies.html", "Illustrative Case Studies | HR Engagement Scenarios",
                    "Browse illustrative HR consulting case studies showing diagnostic methods and implementation roadmaps across core HR functional domains.", content, "Case Studies")

def build_case_study_details():
    img_cs = register_img(
        filename="case-study-engagement-review.webp",
        page="case-study-details.html",
        section="Case Study Overview",
        desc="Corporate HR consultants reviewing implementation roadmaps and organizational diagnostic findings in a modern executive conference room.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional corporate strategy review session. Senior HR management consultants and client executive team analyzing organizational restructuring blueprints in a high-end corporate office. Architectural navy accents, soft cinematic morning light, photorealistic.",
        composition="Medium shot showing collaborative project review",
        camera="50mm lens, f/2.8",
        lighting="Natural ambient morning sunlight",
        bg="Executive corporate boardroom with glass partitions",
        subjects="Three professionals reviewing roadmap diagrams",
        neg_space="Upper lateral section clear"
    )

    content = f'''
{get_page_hero("HR Foundation & Performance Restructure Demo", "An illustrative scenario detailing the transformation of informal people practices into a scalable HR operating model.", [("Case Studies", "case-studies.html"), ("Details", "case-study-details.html")])}

<section class="section">
  <div class="container container-narrow">
    {get_demo_disclaimer("This case study template illustrates the analytical structure, diagnostic criteria, and implementation roadmaps utilized in our consulting practice. All company contexts and figures are conceptual demo data.")}

    <div style="margin: 2rem 0;">
      {render_img(img_cs)}
    </div>

    <div class="grid grid-2 gap-md" style="margin-bottom:2.5rem; background:var(--color-bg-alt); padding:1.5rem; border-radius:var(--radius-md);">
      <div>
        <strong>Industry Focus:</strong> Enterprise Technology Services<br>
        <strong>Organization Scale:</strong> 120 FTE Personnel (Fast Growing)
      </div>
      <div>
        <strong>Engagement Domain:</strong> HR Foundation & Performance Management<br>
        <strong>Engagement Duration:</strong> 14 Weeks (Illustrative Schedule)
      </div>
    </div>

    <article style="line-height:1.75;">
      <h3>1. Organizational Context & Initial State</h3>
      <p>The company had expanded rapidly from a seed-stage team of 25 individuals to over 120 employees across engineering, sales, and client delivery functions. While technical output remained robust, operational leadership identified emerging symptoms of workforce friction: uncoordinated hiring practices, lack of written job bands, absence of formal performance appraisals, and informal leave tracking.</p>

      <h3>2. Core Consulting Objectives</h3>
      <div class="deliverables-list">
        <ul>
          <li>Establish clear job grading architecture and role profiles across all departments.</li>
          <li>Design an objective, transparent quarterly performance evaluation framework.</li>
          <li>Compile a modern, compliant Employee Handbook standardizing workplace policies.</li>
          <li>Enable line managers with structured evaluation rubrics and feedback guidelines.</li>
        </ul>
      </div>

      <h3>3. Assessment Approach & Diagnostic Observations</h3>
      <p>During the initial four-week assessment phase, our advisory team conducted 18 structured stakeholder interviews and reviewed existing personnel documentation. The diagnostic revealed:</p>
      <div class="grid grid-2 gap-md" style="margin:1.5rem 0;">
        <div class="card" style="padding:1.25rem;">
          <h4 style="font-size:1rem; color:var(--color-warning);">Diagnostic Finding A</h4>
          <p style="font-size:0.875rem; margin-bottom:0;">74% of employees lacked written role profiles, leading to recurring task ambiguity between middle managers.</p>
        </div>
        <div class="card" style="padding:1.25rem;">
          <h4 style="font-size:1rem; color:var(--color-warning);">Diagnostic Finding B</h4>
          <p style="font-size:0.875rem; margin-bottom:0;">Performance reviews were conducted once annually with open-ended text fields, producing subjective manager ratings.</p>
        </div>
      </div>

      <h3>4. Recommended HR Framework & Implementation Roadmap</h3>
      <p>Our consulting team engineered a four-tiered job architecture establishing standard titles, competency milestones, and salary bands. Additionally, we formulated an OKR-aligned quarterly review cycle structured around objective performance criteria.</p>

      <div class="table-responsive" style="margin:1.5rem 0;">
        <table class="table-custom">
          <thead>
            <tr>
              <th>Timeline</th>
              <th>Milestone Stage</th>
              <th>Key Implementation Deliverable</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Weeks 1 &ndash; 3</td>
              <td>Discovery & Audit</td>
              <td>Baseline HR Audit Report & Role Clarification Workshops</td>
            </tr>
            <tr>
              <td>Weeks 4 &ndash; 7</td>
              <td>System Design</td>
              <td>Standard Job Architecture Manual & Draft Employee Handbook</td>
            </tr>
            <tr>
              <td>Weeks 8 &ndash; 11</td>
              <td>Manager Enablement</td>
              <td>Manager Coaching Workshops & Objective Performance Rubrics</td>
            </tr>
            <tr>
              <td>Weeks 12 &ndash; 14</td>
              <td>Go-Live & Support</td>
              <td>First Review Cycle Launch & 90-Day Implementation Review</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>5. Expected Process Considerations</h3>
      <p>Successful execution requires active leadership sponsorship, open internal communication regarding why job bands are introduced, and ongoing support for first-time people managers as they conduct structured quarterly reviews.</p>
    </article>

    <div style="margin-top:3rem; padding-top:2rem; border-top:1px solid var(--color-border); display:flex; justify-content:space-between; align-items:center;">
      <a href="case-studies.html" class="btn btn-outline">&larr; Back to All Case Studies</a>
      <a href="book-consultation.html" class="btn btn-teal">Discuss a Similar Engagement</a>
    </div>
  </div>
</section>

{get_cta_section()}
'''
    write_html_page("case-study-details.html", "Illustrative Case Study Details | HR Consulting Engagement",
                    "Detailed case study blueprint outlining organizational context, consulting objectives, diagnostic observations, and implementation roadmaps.", content, "Case Studies")

def build_team():
    team_members = [
        ("HR Strategy & Organization Design Practice", "Lead Advisor & Practice Director", "Focuses on corporate operating models, executive workforce planning, and organizational hierarchy realignment.", "team-lead-hr-strategy.webp"),
        ("Talent Acquisition & Sourcing Practice", "Senior Recruitment Strategist", "Specializes in recruitment pipeline architecture, structured interviewing rubrics, and employer branding.", "team-lead-talent-acquisition.webp"),
        ("Performance & Total Rewards Practice", "Principal Compensation Consultant", "Leads KPI/OKR development, performance appraisal framework restructuring, and job grading bands.", "team-lead-performance-rewards.webp"),
        ("HR Policies, Compliance & Employee Relations", "Senior Compliance & Advisory Lead", "Advises on statutory documentation standards, employee handbooks, POSH awareness, and workplace relations.", "team-lead-compliance-relations.webp"),
        ("Learning, Leadership & Org Development", "Executive Capability Advisor", "Focuses on manager enablement, leadership capability models, succession matrices, and culture assessment.", "team-lead-learning-leadership.webp"),
        ("HR Technology & People Analytics Practice", "HRMS & Workforce Systems Architect", "Specializes in HRMS selection, applicant tracking systems, and people analytics reporting dashboards.", "team-lead-tech-analytics.webp")
    ]

    cards_html = ""
    for name, title, bio, img_name in team_members:
        img_item = register_img(
            filename=img_name,
            page="team.html",
            section=f"Team Profile: {name}",
            desc=f"Abstract professional corporate portrait representing the {name} team lead.",
            ratio="3:4",
            res="900x1200",
            orientation="Portrait",
            prompt="Professional corporate portrait of a seasoned human capital management consultant. Dressed in tailored modern business attire, neutral corporate office background with subtle warm lighting, confident approachable expression, high-end corporate photography.",
            composition="Upper torso portrait, eye level, neutral framing",
            camera="85mm portrait lens, f/2.0",
            lighting="Three-point studio lighting with subtle rim light",
            bg="Neutral softly blurred corporate executive lounge",
            subjects="Corporate professional in business attire",
            neg_space="Even headroom and centered focus"
        )

        cards_html += f'''
      <div class="card" style="padding:1.5rem;">
        {render_img(img_item, "style='margin-bottom:1.25rem;'")}
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.5rem;">
          <h3 class="card-title" style="font-size:1.15rem; margin-bottom:0;">{name}</h3>
          <span class="badge badge-demo" style="font-size:0.65rem;">Demo Profile</span>
        </div>
        <div style="font-size:0.84rem; font-weight:700; color:var(--color-accent-teal); margin-bottom:0.75rem;">{title}</div>
        <p class="card-text" style="font-size:0.875rem;">{bio}</p>
        <div class="card-footer">
          <a href="book-consultation.html" class="link-arrow">Consult With Practice &rarr;</a>
        </div>
      </div>'''

    content = f'''
{get_page_hero("Our Functional Consulting Practice Leaders", "Multi-disciplinary human capital advisors dedicated to organizational effectiveness and workforce excellence.", [("Team", "team.html")])}

<section class="section">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Practice Areas</span>
      <h2>Specialized Consulting Capabilities</h2>
      <p class="section-subtitle">Our practice is organized across dedicated functional domains to ensure deep advisory expertise across all facets of people operations.</p>
    </div>

    {get_demo_disclaimer("Profiles displayed below represent generic functional consulting practice roles and illustrative team configurations. Individual consultant credentials and assignment teams are formalized during engagement scoping.")}

    <div class="grid grid-3 gap-lg" style="margin-top:2rem;">
      {cards_html}
    </div>
  </div>
</section>

{get_cta_section("Engage Our Practice Advisors", "Schedule an initial discovery conversation to explore how our specialized practice leads can support your team.")}
'''
    write_html_page("team.html", "Our Consulting Practice Areas | Human Capital Leaders",
                    "Meet our generic functional consulting practice leaders across HR strategy, talent acquisition, performance management, compliance, and analytics.", content, "Team")

if __name__ == "__main__":
    build_home()
    build_about()
    build_services_overview()
    build_industries()
    build_methodology()
    build_case_studies()
    build_case_study_details()
    build_team()
    print("Core pages built successfully.")

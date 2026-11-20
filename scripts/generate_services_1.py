"""
Generates Services Pages 1 to 11:
- hr-strategy.html
- hr-audit.html
- talent-acquisition.html
- recruitment-consulting.html
- workforce-planning.html
- organizational-development.html
- hr-policies.html
- employee-handbook.html
- performance-management.html
- employee-engagement.html
- learning-development.html
"""

from generator_data import register_img, render_img, get_page_hero, get_demo_disclaimer, get_cta_section, write_html_page

def build_hr_strategy():
    img = register_img(
        filename="hr-strategy-operating-model.webp",
        page="hr-strategy.html",
        section="HR Strategy Framework",
        desc="Senior HR management consultants and executive directors analyzing an HR operating model and human capital roadmap in a boardroom.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Corporate human resources executive strategy session. Business leadership and management consultants evaluating a people strategy blueprint and operating model. Modern glass-walled conference room, warm corporate illumination, professional attire, crisp focus.",
        composition="Wide three-quarter shot showing collaborative discussion around strategic roadmap",
        camera="50mm lens, f/2.8",
        lighting="Natural ambient daylight with warm fill",
        bg="Contemporary corporate boardroom with digital displays",
        subjects="Three senior professionals reviewing strategic charts",
        neg_space="Upper quadrant clean"
    )

    content = f'''
{get_page_hero("Align Your People Strategy With Your Business Goals", "Transform disconnected HR operations into a coherent, business-aligned human capital operating model.", [("Services", "services.html"), ("HR Strategy", "hr-strategy.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Strategic Foundation</span>
        <h2>Workforce Planning Grounded in Commercial Objectives</h2>
        <p class="lead">Without a deliberate people strategy, organizations experience reactive hiring, inconsistent manager practices, and costly talent turnover.</p>
        <p>Our HR strategy consulting service works with executive leadership to evaluate the maturity of the HR function, articulate future talent requirements, and design a scalable people roadmap aligned with corporate milestones.</p>
        <div class="deliverables-list">
          <ul>
            <li><strong>HR Function Assessment:</strong> Comprehensive baseline review of people systems and operational maturity.</li>
            <li><strong>HR Operating Model Design:</strong> Structuring organizational roles, HR business partner interfaces, and operational support.</li>
            <li><strong>Talent Management Strategy:</strong> Defining workforce attraction, succession pipelines, and retention mechanisms.</li>
            <li><strong>Strategic HR Reviews:</strong> Establishing quarterly people scorecards to track talent progress against business targets.</li>
          </ul>
        </div>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Strategic Architecture</span>
      <h2>Illustrative HR Strategy Framework</h2>
      <p class="section-subtitle">How we align commercial objectives with operational people management practices.</p>
    </div>

    <div class="grid grid-3 gap-lg">
      <div class="card">
        <h3 class="card-title">1. Business Intent Alignment</h3>
        <p class="card-text">Evaluating 12-to-36 month business growth targets, new market entries, and revenue projections to determine the required organizational headcount, capabilities, and departmental structures.</p>
      </div>
      <div class="card">
        <h3 class="card-title">2. Workforce Priorities & Capability</h3>
        <p class="card-text">Identifying core organizational competencies, critical leadership roles, and technical skill gaps. Prioritizing interventions across talent acquisition, upskilling, and performance frameworks.</p>
      </div>
      <div class="card">
        <h3 class="card-title">3. HR Roadmap & Scorecard</h3>
        <p class="card-text">Formulating a phased 12-month implementation roadmap complete with executive scorecards, key workforce performance indicators, and governance cadences for continuous review.</p>
      </div>
    </div>

    {get_demo_disclaimer("The strategy framework shown above is an illustrative conceptual model tailored to each client's specific business scale, sector dynamics, and expansion plans.")}
  </div>
</section>

{get_cta_section("Develop a Tailored HR Strategy for Your Business", "Schedule an initial discovery consultation with our human capital advisory team.")}
'''
    write_html_page("hr-strategy.html", "HR Strategy Consulting | Align People Strategy with Business Goals",
                    "Strategic HR consulting to help business leaders design scalable HR operating models, workforce roadmaps, and executive talent frameworks.", content, "Services")

def build_hr_audit():
    img = register_img(
        filename="hr-audit-operational-review.webp",
        page="hr-audit.html",
        section="HR Audit & Assessment",
        desc="Senior HR auditor reviewing compliance checklists, employee lifecycle records, and personnel documentation in a corporate office.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="An HR consultant conducting a rigorous operational human resources audit. Reviewing systematic document binders, digital compliance spreadsheets, and personnel files in a pristine modern corporate conference room. Professional, analytical environment.",
        composition="Medium shot focusing on systematic documentation review and analysis",
        camera="50mm lens, f/2.8",
        lighting="Clean neutral corporate lighting",
        bg="Executive corporate office with organized folders and laptops",
        subjects="Two HR consultants conducting an operational audit",
        neg_space="Clean upper area"
    )

    content = f'''
{get_page_hero("HR Process Audit & Operational Assessment", "Comprehensive operational evaluation of internal HR processes, personnel documentation, and employee lifecycle workflows.", [("Services", "services.html"), ("HR Audit", "hr-audit.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Process Evaluation</span>
        <h2>Identify Inefficiencies, Gaps, and Improvement Priorities</h2>
        <p class="lead">An operational HR audit provides management with an objective snapshot of how effectively everyday people policies and procedures are functioning across the organization.</p>
        <p>Our review examines documentation rigor, recruitment consistency, employee onboarding hygiene, appraisal cadences, and record management systems to identify vulnerabilities before they disrupt operations.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
        <line x1="12" y1="9" x2="12" y2="13"></line>
        <line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
      <div>
        <strong>Important Operational Scope Notice:</strong>
        <p style="margin-top:0.25rem;">This service is an operational and managerial HR process assessment designed to enhance organizational efficiency. It does not constitute a formal statutory, legal, or regulatory audit, nor does it provide legal certification, court representation, or guaranteed regulatory compliance.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Inspection Checklist</span>
      <h2>Illustrative HR Assessment Checklist & Audit Scorecard</h2>
      <p class="section-subtitle">A structured, multi-dimensional review evaluating critical personnel administration domains.</p>
    </div>

    <div class="table-responsive">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Audit Domain</th>
            <th>Sample Evaluation Criteria</th>
            <th>Typical Gaps Identified</th>
            <th>Sample Diagnostic Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Personnel File Documentation</strong></td>
            <td>Signed offer letters, ID proofs, background check verification, address records.</td>
            <td>Missing countersigned appointment letters, uncentralized file storage.</td>
            <td><span class="badge badge-demo">Action Required</span></td>
          </tr>
          <tr>
            <td><strong>Onboarding & Induction</strong></td>
            <td>Structured first-week schedule, asset handover slips, policy briefing sign-offs.</td>
            <td>Informal induction, delayed email/system credentials, undocumented asset allocation.</td>
            <td><span class="badge badge-navy">Satisfactory</span></td>
          </tr>
          <tr>
            <td><strong>Leave & Attendance Controls</strong></td>
            <td>Leave policy documentation, approval workflows, attendance reconciliation logs.</td>
            <td>Discrepancies between physical sign-in logs and monthly payroll input sheets.</td>
            <td><span class="badge badge-demo">Action Required</span></td>
          </tr>
          <tr>
            <td><strong>Performance Management</strong></td>
            <td>Written KRAs, quarterly review forms, documented improvement plans (PIPs).</td>
            <td>Subjective evaluations, lack of documented feedback for low-scoring personnel.</td>
            <td><span class="badge badge-teal">Needs Improvement</span></td>
          </tr>
          <tr>
            <td><strong>Separation & Exit Procedures</strong></td>
            <td>Resignation acceptance records, handover sign-offs, full & final settlement checklists.</td>
            <td>Missing clearance forms from IT/finance, delayed release of experience certificates.</td>
            <td><span class="badge badge-navy">Satisfactory</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

{get_cta_section("Request an Operational HR Process Audit", "Discover practical opportunities to streamline your HR documentation and management controls.")}
'''
    write_html_page("hr-audit.html", "HR Audit Services | Operational HR Process Review",
                    "Operational HR audit services to evaluate personnel documentation, onboarding workflows, leave tracking, and process hygiene.", content, "Services")

def build_talent_acquisition():
    img = register_img(
        filename="talent-acquisition-interview-panel.webp",
        page="talent-acquisition.html",
        section="Talent Acquisition Strategy",
        desc="Talent acquisition specialists and department hiring managers conducting a structured competency interview with a candidate in a modern corporate office.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional talent acquisition panel interview in progress. Two senior interviewers in business casual attire reviewing an evaluation rubric with candidate in a well-lit corporate conference room. Contemporary glass and wood interior, natural morning lighting.",
        composition="Eye-level medium shot of interview panel and candidate",
        camera="50mm lens, f/2.5",
        lighting="Soft ambient daylight",
        bg="Contemporary corporate office with acoustic timber slats",
        subjects="Three professionals engaged in professional dialogue",
        neg_space="Upper section uncluttered"
    )

    content = f'''
{get_page_hero("Find and Attract the Talent Your Business Needs", "Strategic talent acquisition consulting to build structured candidate sourcing, screening, and selection pipelines.", [("Services", "services.html"), ("Talent Acquisition", "talent-acquisition.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Talent Strategy</span>
        <h2>Move Beyond Reactive Hiring to Intentional Talent Sourcing</h2>
        <p class="lead">Hiring the right people requires strategic alignment between role requirements, candidate assessment rubrics, and employer value propositions.</p>
        <p>Our talent acquisition consulting advises companies on how to establish predictable, high-caliber recruitment operations that consistently attract top performers without relying on haphazard hiring practices.</p>
        <div class="deliverables-list">
          <ul>
            <li><strong>Role Profiling & Job Definition:</strong> Translating vague requirements into measurable competency frameworks.</li>
            <li><strong>Candidate Sourcing Strategy:</strong> Identifying direct sourcing channels, niche talent pools, and outbound campaigns.</li>
            <li><strong>Structured Selection Design:</strong> Developing standardized interview question banks and objective scoring scorecards.</li>
            <li><strong>Employer Branding Guidelines:</strong> Articulating authentic company values and workplace culture to prospective talent.</li>
          </ul>
        </div>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      <div>
        <strong>Service Scope Note:</strong> This advisory service focuses on designing talent acquisition methodologies, interview rubrics, and recruitment systems. Operational candidate sourcing and placement execution are scoped separately under defined staffing agreements. We do not claim fabricated candidate databases or guaranteed placement statistics.
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Recruitment Pipeline</span>
      <h2>Illustrative End-to-End Talent Acquisition Pipeline</h2>
      <p class="section-subtitle">A standardized hiring sequence designed to minimize bias, enhance candidate experience, and maximize role alignment.</p>
    </div>

    <div class="pipeline-container">
      <div class="pipeline-step">
        <span class="pipeline-step-num">Stage 1</span>
        <span class="pipeline-step-title">Workforce Need</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Headcount justification & business authorization.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Stage 2</span>
        <span class="pipeline-step-title">Job Definition</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Competency mapping & score rubric creation.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Stage 3</span>
        <span class="pipeline-step-title">Sourcing</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Multi-channel outreach & talent pipelining.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Stage 4</span>
        <span class="pipeline-step-title">Screening</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Structured resume & preliminary phone filter.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Stage 5</span>
        <span class="pipeline-step-title">Interview</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Behavioral & technical rubric assessment.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Stage 6</span>
        <span class="pipeline-step-title">Selection</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Reference checks & standardized offer modeling.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Stage 7</span>
        <span class="pipeline-step-title">Onboarding</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Pre-boarding & 30-day orientation program.</p>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Upgrade Your Talent Acquisition Strategy", "Let us evaluate your recruitment workflows and establish structured candidate evaluation frameworks.")}
'''
    write_html_page("talent-acquisition.html", "Talent Acquisition Consulting | Structured Candidate Sourcing",
                    "Strategic talent acquisition consulting to help businesses build structured recruitment pipelines, interview rubrics, and employer branding.", content, "Services")

def build_recruitment_consulting():
    img = register_img(
        filename="recruitment-consulting-dashboard-session.webp",
        page="recruitment-consulting.html",
        section="Recruitment Process Optimization",
        desc="Recruitment consultants analyzing hiring funnel metrics and candidate evaluation dashboards in a collaborative corporate war room.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Recruitment process consulting workshop. HR consultants and hiring managers reviewing recruiting metrics, time-to-hire pipelines, and candidate experience charts displayed on multiple ultra-thin monitors. Modern corporate office, natural lighting.",
        composition="Wide shot of collaborative team in high-tech corporate meeting room",
        camera="35mm lens, f/3.5",
        lighting="Natural ambient lighting balanced with display glow",
        bg="Corporate glass-fronted project war room with whiteboards",
        subjects="Four business professionals reviewing recruitment data",
        neg_space="Upper lateral section uncluttered"
    )

    content = f'''
{get_page_hero("Optimize Your Hiring Workflows & Recruiter Effectiveness", "Recruitment consulting to streamline hiring funnels, train interviewers, and enhance candidate experience.", [("Services", "services.html"), ("Recruitment Consulting", "recruitment-consulting.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Hiring Operations</span>
        <h2>Transform Recruitment Into an Efficient, Measurable Engine</h2>
        <p class="lead">Long hiring cycles, disengaged candidates, and misaligned manager evaluations directly increase operational recruitment costs.</p>
        <p>Our recruitment consulting services audit internal hiring friction points, develop rigorous job descriptions, equip hiring managers with effective interview techniques, and implement transparent recruitment tracking metrics.</p>
        <div class="deliverables-list">
          <ul>
            <li><strong>Recruitment Process Assessment:</strong> Bottleneck analysis across application, interview, and offer stages.</li>
            <li><strong>Job Description Engineering:</strong> Authoring clear, realistic, and outcome-oriented role specifications.</li>
            <li><strong>Hiring Manager Interview Training:</strong> Coaching leaders on competency questions and unconscious bias reduction.</li>
            <li><strong>Candidate Experience Optimization:</strong> Crafting responsive communication cadences and prompt feedback loops.</li>
          </ul>
        </div>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Illustrative Metrics</span>
      <h2>Illustrative Recruitment Pipeline Dashboard Mockup</h2>
      <p class="section-subtitle">Sample reporting framework illustrating how recruitment stages and velocity can be monitored.</p>
    </div>

    <div class="hr-dashboard">
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <span class="dashboard-title">Recruitment Pipeline Funnel (Sample Demonstration Data)</span>
        </div>
        <span class="badge badge-demo">Illustrative Demo Data</span>
      </div>
      <div class="dashboard-body">
        <div class="metric-grid">
          <div class="metric-card">
            <div class="metric-label">Open Requisitions</div>
            <div class="metric-value">18</div>
            <div class="metric-sub">Active Priority Roles</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Screening Ratio</div>
            <div class="metric-value">24%</div>
            <div class="metric-sub">Application to Screen</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Interview to Offer</div>
            <div class="metric-value">1:4</div>
            <div class="metric-sub">Structured Panel Ratio</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Offer Acceptance Rate</div>
            <div class="metric-value">88%</div>
            <div class="metric-sub">Sample Cohort Avg</div>
          </div>
        </div>

        <div class="chart-card">
          <div class="chart-title">
            <span>Candidate Stage Distribution (Active Pipeline)</span>
            <span style="font-size:0.75rem; color:var(--color-secondary-text);">Demo Cohort of 160 Applicants</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Initial Applications</span>
            <div class="bar-track"><div class="bar-fill" style="width: 100%;"></div></div>
            <span class="bar-value">160</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Resume Filter Passed</span>
            <div class="bar-track"><div class="bar-fill" style="width: 52%;"></div></div>
            <span class="bar-value">84</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Competency Screen</span>
            <div class="bar-track"><div class="bar-fill" style="width: 28%;"></div></div>
            <span class="bar-value">45</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Technical / Panel Round</span>
            <div class="bar-track"><div class="bar-fill" style="width: 15%;"></div></div>
            <span class="bar-value">24</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Final Offer Extended</span>
            <div class="bar-track"><div class="bar-fill fill-gold" style="width: 8%;"></div></div>
            <span class="bar-value">12</span>
          </div>
        </div>
      </div>
    </div>

    {get_demo_disclaimer("Metrics, ratios, and candidate counts shown above represent non-operational demonstration values designed to visualize recruitment analytics concepts.")}
  </div>
</section>

{get_cta_section("Streamline Your Internal Hiring Workflows", "Speak with our recruitment advisory specialists to evaluate your hiring process.")}
'''
    write_html_page("recruitment-consulting.html", "Recruitment Consulting Services | Hiring Process Optimization",
                    "Recruitment consulting to optimize internal hiring workflows, manager interview skills, candidate experience, and recruitment metrics.", content, "Services")

def build_workforce_planning():
    img = register_img(
        filename="workforce-planning-strategy-board.webp",
        page="workforce-planning.html",
        section="Workforce & Headcount Planning",
        desc="Senior HR consultants and financial controllers analyzing workforce forecasting spreadsheets and headcount models on a conference room screen.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Strategic workforce planning session in an executive corporate setting. Finance directors and human resources advisors evaluating headcount capacity models, retirement transitions, and departmental expansion projections on a high-definition wall monitor. Sophisticated office, natural light.",
        composition="Medium shot of leadership team analyzing workforce graphs",
        camera="50mm lens, f/2.8",
        lighting="Natural ambient morning sunlight",
        bg="Executive corporate strategy room",
        subjects="Three business professionals analyzing headcount forecast",
        neg_space="Left upper area clean"
    )

    content = f'''
{get_page_hero("Plan the Workforce Your Organization Needs Next", "Data-driven workforce planning and headcount advisory to anticipate talent demands and optimize manpower costs.", [("Services", "services.html"), ("Workforce Planning", "workforce-planning.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Manpower Optimization</span>
        <h2>Anticipate Headcount Demands Before Capacity Crises Occur</h2>
        <p class="lead">Organizations that fail to forecast workforce requirements swing between emergency hiring sprees and expensive overstaffing cycles.</p>
        <p>Our workforce planning consulting aligns business growth projections with required staffing levels, identifies future skills gaps, models payroll cost trajectories, and builds structured succession contingency buffers.</p>
        <div class="deliverables-list">
          <ul>
            <li><strong>Workforce Capacity Assessment:</strong> Evaluating current employee utilization, workload distribution, and overtime trends.</li>
            <li><strong>Skills Gap Analysis:</strong> Mapping emerging technical, commercial, and operational skill requirements.</li>
            <li><strong>Headcount Forecasting Models:</strong> Multi-scenario headcount projections aligned with revenue forecasts.</li>
            <li><strong>Restructuring Advisory:</strong> Guidance on role consolidation, team realignments, and organizational resizing.</li>
          </ul>
        </div>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Headcount Modeling</span>
      <h2>Illustrative Workforce Planning & Headcount Dashboard</h2>
      <p class="section-subtitle">Conceptual visualization demonstrating departmental headcount tracking, open vacancies, and skill gap allocations.</p>
    </div>

    <div class="hr-dashboard">
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <span class="dashboard-title">Quarterly Headcount Planning Model (Demo Data)</span>
        </div>
        <span class="badge badge-demo">Illustrative Demo Data</span>
      </div>
      <div class="dashboard-body">
        <div class="table-responsive">
          <table class="table-custom">
            <thead>
              <tr>
                <th>Department</th>
                <th>Current FTE</th>
                <th>Projected Q+2 Requirement</th>
                <th>Identified Skills Gap</th>
                <th>Budget Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Engineering & Product</strong></td>
                <td>48</td>
                <td>62 (+14)</td>
                <td>Cloud Architecture, Senior QA</td>
                <td><span class="badge badge-teal">Approved</span></td>
              </tr>
              <tr>
                <td><strong>Client Operations</strong></td>
                <td>35</td>
                <td>40 (+5)</td>
                <td>Bilingual Support, Tier-2 Tech</td>
                <td><span class="badge badge-teal">Approved</span></td>
              </tr>
              <tr>
                <td><strong>Enterprise Sales</strong></td>
                <td>18</td>
                <td>24 (+6)</td>
                <td>Account Execs (Enterprise Tier)</td>
                <td><span class="badge badge-demo">Pending Review</span></td>
              </tr>
              <tr>
                <td><strong>Corporate G&A</strong></td>
                <td>14</td>
                <td>16 (+2)</td>
                <td>Senior Financial Analyst</td>
                <td><span class="badge badge-navy">Funded</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    {get_demo_disclaimer("All headcount numbers, department designations, and budget flags shown above are conceptual figures intended to illustrate strategic workforce planning templates.")}
  </div>
</section>

{get_cta_section("Build a Disciplined Workforce Plan", "Connect with our human capital strategists to model your organization's future headcount requirements.")}
'''
    write_html_page("workforce-planning.html", "Workforce Planning Consulting | Headcount & Skills Gap Advisory",
                    "Strategic workforce planning consulting to help organizations forecast staffing needs, conduct skills gap analyses, and manage manpower costs.", content, "Services")

def build_org_dev():
    img = register_img(
        filename="organizational-development-structure.webp",
        page="organizational-development.html",
        section="Org Structure Design",
        desc="Management consultants and enterprise directors examining organizational charts and reporting hierarchies on an interactive whiteboard.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Corporate organizational development workshop. Senior HR advisors and enterprise executives analyzing structural departmental hierarchy trees and RACI matrices on a sleek modern digital whiteboard. Crisp, high-end corporate setting, tailored business wear.",
        composition="Medium wide shot of executives discussing hierarchy diagram",
        camera="50mm lens, f/2.8",
        lighting="Even balanced corporate interior illumination",
        bg="Executive corporate boardroom with acoustic felt and glass",
        subjects="Three corporate leaders collaborating on structural charts",
        neg_space="Upper lateral area uncluttered"
    )

    content = f'''
{get_page_hero("Design Structures That Foster Clarity, Speed & Accountability", "Organizational development consulting to clarify reporting hierarchies, design job architectures, and strengthen culture.", [("Services", "services.html"), ("Organizational Development", "organizational-development.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Structural Effectiveness</span>
        <h2>Eliminate Organizational Bottlenecks and Ambiguity</h2>
        <p class="lead">As companies expand, informal reporting lines cause territorial overlap, slow decision-making, and frustrated employees.</p>
        <p>Our organizational development advisory helps leadership architect streamlined departmental reporting structures, establish transparent job grading frameworks, define accountability with RACI matrices, and cultivate high-performance workplace cultures.</p>
        <div class="deliverables-list">
          <ul>
            <li><strong>Organizational Structure Redesign:</strong> Optimizing spans of control, reporting chains, and cross-functional interfaces.</li>
            <li><strong>Job Architecture Banding:</strong> Standardizing career bands, role levels, and progression criteria across departments.</li>
            <li><strong>RACI Responsibility Mapping:</strong> Clarifying who is Responsible, Accountable, Consulted, and Informed for key tasks.</li>
            <li><strong>Culture & Capability Assessment:</strong> Evaluating operational friction, collaboration habits, and team dynamics.</li>
          </ul>
        </div>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Job Architecture</span>
      <h2>Illustrative Enterprise Job Architecture & Career Banding</h2>
      <p class="section-subtitle">A standardized leveling model ensuring role parity, transparent promotion paths, and clear compensation anchors.</p>
    </div>

    <div class="table-responsive">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Level Band</th>
            <th>Sample Individual Contributor Track</th>
            <th>Sample People Leadership Track</th>
            <th>Expected Competency Scope</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Band L1 &ndash; Foundation</strong></td>
            <td>Associate / Junior Specialist</td>
            <td>&mdash;</td>
            <td>Task execution under guidance; developing core functional technical skills.</td>
          </tr>
          <tr>
            <td><strong>Band L2 &ndash; Professional</strong></td>
            <td>Specialist / Engineer</td>
            <td>&mdash;</td>
            <td>Independent task delivery, problem solving, and standard workflow execution.</td>
          </tr>
          <tr>
            <td><strong>Band L3 &ndash; Senior</strong></td>
            <td>Senior Specialist / Lead</td>
            <td>Team Lead / Supervisor</td>
            <td>Complex project ownership, peer mentoring, process optimization, workflow reviews.</td>
          </tr>
          <tr>
            <td><strong>Band L4 &ndash; Management</strong></td>
            <td>Principal / Staff Specialist</td>
            <td>Manager / Practice Lead</td>
            <td>Departmental strategy execution, hiring decisions, budget allocation, cross-team alignment.</td>
          </tr>
          <tr>
            <td><strong>Band L5 &ndash; Executive</strong></td>
            <td>Fellow / Advisory Expert</td>
            <td>Director / Head of Function</td>
            <td>Enterprise vision, strategic workforce governance, multi-year business impact.</td>
          </tr>
        </tbody>
      </table>
    </div>

    {get_demo_disclaimer("This job architecture reflects an illustrative demo framework. Exact bands, role titles, and progression criteria are customized to each client's industry structure and operational requirements.")}
  </div>
</section>

{get_cta_section("Streamline Your Organizational Structure", "Schedule an exploratory discussion with our organizational development practice.")}
'''
    write_html_page("organizational-development.html", "Organizational Development Consulting | Structure & Job Architecture",
                    "Organizational development consulting to clarify reporting relationships, design enterprise job architectures, and improve team effectiveness.", content, "Services")

def build_hr_policies():
    img = register_img(
        filename="hr-policies-documentation-library.webp",
        page="hr-policies.html",
        section="Policy Framework Design",
        desc="Corporate HR policy advisors reviewing workplace standard operating procedures and employment documentation folders on a boardroom table.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional corporate HR policy documentation meeting. Senior consultants and business operations directors reviewing structured operational policy manuals, codes of conduct, and employment binders in a modern, brightly lit executive suite.",
        composition="Medium shot of professionals analyzing documentation manuals",
        camera="50mm lens, f/2.8",
        lighting="Crisp bright daylight with soft shadows",
        bg="Modern executive corporate office suite",
        subjects="Two business leaders examining policy binders",
        neg_space="Upper lateral section clean"
    )

    content = f'''
{get_page_hero("Create Clear HR Policies That Support Better Workplace Practices", "Comprehensive policy frameworks, standard operating procedures, and clear workplace guidelines.", [("Services", "services.html"), ("HR Policies", "hr-policies.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Governance & Clarity</span>
        <h2>Transparent Workplace Rules That Protect and Empower Teams</h2>
        <p class="lead">Ambiguous or unwritten policies create manager inconsistency, workplace grievances, and unnecessary regulatory vulnerability.</p>
        <p>We work with growing companies to draft clear, comprehensive, and operationally realistic HR policy manuals covering attendance, leave, remote working, employee conduct, disciplinary processes, and separation procedures.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
        <line x1="12" y1="9" x2="12" y2="13"></line>
        <line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
      <div>
        <strong>Professional Legal Review Advisory:</strong>
        <p style="margin-top:0.25rem;">All policy frameworks, clauses, and manuals developed under this consulting advisory represent management templates and operational guidelines. Before formal adoption, employment policies must be reviewed by qualified legal and compliance counsel against the specific statutory rules, state enactments, and local labor laws of your operating jurisdiction.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Policy Suite</span>
      <h2>Illustrative Workplace Policy Library Interface</h2>
      <p class="section-subtitle">Sample core policies developed for growing corporate and SME workplace environments.</p>
    </div>

    <div class="grid grid-3 gap-md">
      <div class="card">
        <h4 class="card-title">Attendance & Working Hours</h4>
        <p class="card-text">Core operating hours, flexitime rules, shift logging, attendance tracking protocols, and meal break allocations.</p>
        <span class="badge badge-navy">Template Module 01</span>
      </div>
      <div class="card">
        <h4 class="card-title">Leave & Absence Entitlement</h4>
        <p class="card-text">Annual leave, sick leave, casual leave accrual formulas, maternity/paternity support, and compensatory off procedures.</p>
        <span class="badge badge-navy">Template Module 02</span>
      </div>
      <div class="card">
        <h4 class="card-title">Code of Workplace Conduct</h4>
        <p class="card-text">Conflict of interest disclosures, confidentiality safeguards, respectful behavior standards, and asset protection guidelines.</p>
        <span class="badge badge-navy">Template Module 03</span>
      </div>
      <div class="card">
        <h4 class="card-title">Remote & Hybrid Work Protocol</h4>
        <p class="card-text">Work-from-home eligibility criteria, data security requirements, equipment allowances, and connectivity expectations.</p>
        <span class="badge badge-navy">Template Module 04</span>
      </div>
      <div class="card">
        <h4 class="card-title">Disciplinary & Grievance SOP</h4>
        <p class="card-text">Fair inquiry processes, verbal/written warning escalations, investigation guidelines, and dispute escalation matrices.</p>
        <span class="badge badge-navy">Template Module 05</span>
      </div>
      <div class="card">
        <h4 class="card-title">Separation & Exit Process</h4>
        <p class="card-text">Notice period guidelines, buy-out protocols, asset handover checklists, full & final settlement clearance timelines.</p>
        <span class="badge badge-navy">Template Module 06</span>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Establish Clear Workplace Policies Today", "Speak with our HR advisory practice to build a tailored policy library for your organization.")}
'''
    write_html_page("hr-policies.html", "HR Policies & Documentation Consulting | Workplace Guidelines",
                    "HR policy consulting to develop structured, professional workplace policies covering attendance, leave, conduct, remote work, and disciplinary procedures.", content, "Services")

def build_employee_handbook():
    img = register_img(
        filename="employee-handbook-orientation-meeting.webp",
        page="employee-handbook.html",
        section="Handbook Development",
        desc="A newly inducted employee reviewing a corporate employee handbook and onboarding binder with an HR onboarding manager.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional corporate onboarding session. An HR manager presenting a beautifully designed employee handbook booklet and digital welcome portal to an attentive new hire in a modern corporate office. Clean aesthetic, soft morning light.",
        composition="Medium shot showing the handbook guide and welcoming dialogue",
        camera="50mm lens, f/2.5",
        lighting="Soft natural office daylight",
        bg="Contemporary corporate office lounge with subtle plant accents",
        subjects="Two professionals in smart corporate attire",
        neg_space="Upper quadrant clean"
    )

    content = f'''
{get_page_hero("Employee Handbook Development", "Turn dry corporate rules into an engaging, clear, and comprehensive guide for every employee.", [("Services", "services.html"), ("Employee Handbook", "employee-handbook.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Culture & Compliance</span>
        <h2>A Central Source of Truth for Your Entire Team</h2>
        <p class="lead">An effective employee handbook communicates workplace expectations, celebrates company culture, and establishes clear operational boundaries.</p>
        <p>We work with business founders and HR leaders to distill complex HR policies into a clean, accessible, and professionally articulated handbook that simplifies onboarding and reinforces shared values.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      <div>
        <strong>Demonstration Content Disclaimer:</strong> All handbook previews and outlines provided here represent editable demonstration templates. Client handbooks are customized to reflect each organization's specific culture, industry sector, and legally reviewed policies.
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Handbook Anatomy</span>
      <h2>Illustrative Employee Handbook Table of Contents</h2>
      <p class="section-subtitle">A balanced structure combining corporate identity, operating standards, and employee rights.</p>
    </div>

    <div class="grid grid-2 gap-lg">
      <div class="card">
        <h3 class="card-title" style="font-size:1.15rem;">Part I: Welcome & Workplace Culture</h3>
        <ul class="deliverables-list">
          <li><strong>1.1 Welcome Message from Leadership:</strong> Mission, core values, and corporate purpose.</li>
          <li><strong>1.2 About Our Practice & History:</strong> Overview of our services and operational philosophy.</li>
          <li><strong>1.3 Organizational Values in Action:</strong> Mutual respect, professional excellence, and integrity.</li>
          <li><strong>1.4 Equal Opportunity & Anti-Discrimination:</strong> Commitment to fairness and non-bias.</li>
        </ul>
      </div>

      <div class="card">
        <h3 class="card-title" style="font-size:1.15rem;">Part II: Workplace Standards & Attendance</h3>
        <ul class="deliverables-list">
          <li><strong>2.1 Working Hours & Remote Work:</strong> Standard shifts, attendance logging, and remote policies.</li>
          <li><strong>2.2 Leave Entitlements & Holidays:</strong> Paid leave, sick leave, statutory holidays, and applications.</li>
          <li><strong>2.3 Dress Code & Workplace Environment:</strong> Professional attire and clean desk guidelines.</li>
          <li><strong>2.4 Information Security & Asset Care:</strong> Laptops, customer data privacy, and software licenses.</li>
        </ul>
      </div>

      <div class="card">
        <h3 class="card-title" style="font-size:1.15rem;">Part III: Growth, Performance & Rewards</h3>
        <ul class="deliverables-list">
          <li><strong>3.1 Performance Evaluation Cadence:</strong> Quarterly reviews, KPI setting, and feedback.</li>
          <li><strong>3.2 Professional Learning & Development:</strong> Training budgets, certifications, and mentoring.</li>
          <li><strong>3.3 Compensation, Payroll & Incentives:</strong> Payday schedules, reimbursements, and bonuses.</li>
          <li><strong>3.4 Recognition & Milestone Awards:</strong> Service awards and peer recognition schemes.</li>
        </ul>
      </div>

      <div class="card">
        <h3 class="card-title" style="font-size:1.15rem;">Part IV: Resolution & Separation</h3>
        <ul class="deliverables-list">
          <li><strong>4.1 Grievance Redressal Mechanism:</strong> Step-by-step dispute resolution and mediation.</li>
          <li><strong>4.2 POSH & Prevention of Harassment:</strong> Internal Committee procedures and reporting.</li>
          <li><strong>4.3 Disciplinary Process:</strong> Notice of inquiry, formal hearings, and sanction criteria.</li>
          <li><strong>4.4 Resignation & Full & Final Settlement:</strong> Notice periods, handovers, and final clearance.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Develop a Custom Employee Handbook", "Collaborate with our advisory team to craft a handbook tailored to your organization.")}
'''
    write_html_page("employee-handbook.html", "Employee Handbook Consulting | Custom Company Policy Manuals",
                    "Employee handbook development consulting to create clear, modern, and legally reviewed workplace manuals and onboarding guides.", content, "Services")

def build_performance_mgmt():
    img = register_img(
        filename="performance-management-review-session.webp",
        page="performance-management.html",
        section="Performance Framework",
        desc="A department manager and employee reviewing quarterly KPI scorecards and career growth goals during a 1-on-1 performance review.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional performance appraisal review in progress. A manager and an employee reviewing quarterly performance targets and goal scorecards on a laptop screen in a modern meeting pod. Calm, constructive corporate atmosphere.",
        composition="Medium two-shot of manager and team member discussing performance data",
        camera="50mm lens, f/2.8",
        lighting="Natural soft window lighting",
        bg="Modern corporate office interior with glass and timber accents",
        subjects="Two professionals in business casual wear in constructive discussion",
        neg_space="Upper lateral section clear"
    )

    content = f'''
{get_page_hero("Connect Employee Goals With Business Performance", "Design objective performance management systems, OKR/KPI structures, and continuous review cadences.", [("Services", "services.html"), ("Performance Management", "performance-management.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Accountability & Growth</span>
        <h2>Shift From Subjective Annual Reviews to Continuous Alignment</h2>
        <p class="lead">Annual review meetings that rely on subjective impressions often frustrate high performers and fail to correct underperformance.</p>
        <p>Our performance management consulting helps organizations formulate transparent Key Result Areas (KRAs), objective Key Performance Indicators (KPIs), continuous check-in cadences, 360-degree feedback tools, and structured Performance Improvement Plans (PIPs).</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Performance Analytics</span>
      <h2>Illustrative Performance Review Dashboard</h2>
      <p class="section-subtitle">Sample visual interface showing review completion cadences and goal alignment across departments.</p>
    </div>

    <div class="hr-dashboard">
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <span class="dashboard-title">Q3 Performance Cycle Overview (Sample Demo Model)</span>
        </div>
        <span class="badge badge-demo">Illustrative Demo Data</span>
      </div>
      <div class="dashboard-body">
        <div class="metric-grid">
          <div class="metric-card">
            <div class="metric-label">Goal Alignment Rate</div>
            <div class="metric-value">94%</div>
            <div class="metric-sub">KRAs Linked to Objectives</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Review Completion</div>
            <div class="metric-value">88%</div>
            <div class="metric-sub">Self & Manager Evaluations</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">High Performers</div>
            <div class="metric-value">22%</div>
            <div class="metric-sub">Exceeding Targets (Demo)</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">PIPs Monitored</div>
            <div class="metric-value">4</div>
            <div class="metric-sub">Active Mentoring Tracks</div>
          </div>
        </div>

        <div class="chart-card">
          <div class="chart-title">
            <span>Performance Rating Distribution (Normalized Demo Cohort)</span>
            <span style="font-size:0.75rem; color:var(--color-secondary-text);">Sample bell curve distribution</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Exceeds Expectations</span>
            <div class="bar-track"><div class="bar-fill" style="width: 20%;"></div></div>
            <span class="bar-value">20%</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Consistently Meets</span>
            <div class="bar-track"><div class="bar-fill" style="width: 65%;"></div></div>
            <span class="bar-value">65%</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Developing / Needs Support</span>
            <div class="bar-track"><div class="bar-fill fill-gold" style="width: 15%;"></div></div>
            <span class="bar-value">15%</span>
          </div>
        </div>
      </div>
    </div>

    {get_demo_disclaimer("Performance scores, percentages, and metrics shown above are purely illustrative demonstration data and do not represent actual employee records.")}
  </div>
</section>

{get_cta_section("Re-engineer Your Performance Management System", "Consult with our performance strategists to design objective appraisal frameworks.")}
'''
    write_html_page("performance-management.html", "Performance Management Consulting | KPI, KRA & Appraisal Systems",
                    "Performance management consulting to design objective goal-setting, KPI and KRA development, continuous feedback, and review frameworks.", content, "Services")

def build_employee_engagement():
    img = register_img(
        filename="employee-engagement-culture-workshop.webp",
        page="employee-engagement.html",
        section="Engagement Strategy",
        desc="A vibrant cross-functional employee engagement workshop in a creative corporate collaborative space.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional employee engagement workshop. A team of diverse professionals in a brightly illuminated modern corporate collaboration area, engaged in culture-mapping and team feedback exercises with sticky notes and digital boards.",
        composition="Wide shot of engaged employees in active collaborative dialogue",
        camera="35mm lens, f/3.2",
        lighting="Bright ambient natural light",
        bg="Creative modern corporate lounge with collaborative spaces",
        subjects="Diverse team members working collaboratively",
        neg_space="Upper quadrant clean"
    )

    content = f'''
{get_page_hero("Strengthen Workplace Culture & Retention", "Evidence-based employee listening frameworks, pulse surveys, and cultural alignment programs.", [("Services", "services.html"), ("Employee Engagement", "employee-engagement.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">People & Culture</span>
        <h2>Listen, Understand, and Act on Meaningful Employee Feedback</h2>
        <p class="lead">Unresolved workplace dissatisfaction leads to 'quiet quitting', lowered productivity, and unexpected departures of valuable talent.</p>
        <p>Our employee engagement consulting designs anonymous listening frameworks, meaningful pulse surveys, manager action-planning templates, and reward and recognition programs that cultivate organizational loyalty.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Engagement Analytics</span>
      <h2>Illustrative Employee Engagement Survey Dashboard</h2>
      <p class="section-subtitle">Sample visualization illustrating survey participation, sentiment indices, and thematic feedback areas.</p>
    </div>

    <div class="hr-dashboard">
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <span class="dashboard-title">Annual Workplace Sentiment Survey (Illustrative Demo Model)</span>
        </div>
        <span class="badge badge-demo">Illustrative Demo Data</span>
      </div>
      <div class="dashboard-body">
        <div class="metric-grid">
          <div class="metric-card">
            <div class="metric-label">Survey Response Rate</div>
            <div class="metric-value">84%</div>
            <div class="metric-sub">Sample Participation</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Overall Sentiment Index</div>
            <div class="metric-value">4.1 / 5</div>
            <div class="metric-sub">Favorable Response Band</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Manager Communication</div>
            <div class="metric-value">79%</div>
            <div class="metric-sub">Positive Rating</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Growth Opportunity Score</div>
            <div class="metric-value">72%</div>
            <div class="metric-sub">Area for Enhancement</div>
          </div>
        </div>

        <div class="chart-card">
          <div class="chart-title">
            <span>Engagement Themes Favourability (Demo Model)</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Role Clarity & Mission</span>
            <div class="bar-track"><div class="bar-fill" style="width: 86%;"></div></div>
            <span class="bar-value">86%</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Team Collaboration</span>
            <div class="bar-track"><div class="bar-fill" style="width: 82%;"></div></div>
            <span class="bar-value">82%</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Recognition & Appreciation</span>
            <div class="bar-track"><div class="bar-fill" style="width: 74%;"></div></div>
            <span class="bar-value">74%</span>
          </div>
          <div class="bar-row">
            <span class="bar-label">Career Progression Clarity</span>
            <div class="bar-track"><div class="bar-fill fill-gold" style="width: 68%;"></div></div>
            <span class="bar-value">68%</span>
          </div>
        </div>
      </div>
    </div>

    {get_demo_disclaimer("Survey results, scores, and sentiment metrics displayed above represent fictional demonstration data and do not reflect verified employee satisfaction results.")}
  </div>
</section>

{get_cta_section("Enhance Employee Engagement in Your Business", "Connect with our culture advisory practice to design tailored employee listening surveys.")}
'''
    write_html_page("employee-engagement.html", "Employee Engagement Consulting | Workplace Culture & Retention",
                    "Employee engagement consulting to design pulse surveys, employee feedback loops, culture assessments, and retention roadmaps.", content, "Services")

def build_learning_dev():
    img = register_img(
        filename="learning-development-training-session.webp",
        page="learning-development.html",
        section="L&D Framework",
        desc="Corporate trainer and business professionals participating in an executive skills capability training seminar in a corporate theater.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional corporate training seminar. A corporate capability development coach presenting a managerial skill-building module on a wide presentation screen in a modern tiered training auditorium. Focused participants in professional attire.",
        composition="Medium wide shot of training instructor and engaged corporate audience",
        camera="50mm lens, f/2.8",
        lighting="Ambient warm theater illumination balanced with screen projection",
        bg="Executive corporate training amphitheater",
        subjects="Corporate instructor and attentive professionals",
        neg_space="Left upper section uncluttered"
    )

    content = f'''
{get_page_hero("Build Skills. Strengthen Capabilities. Develop People.", "Structured Learning & Development strategies, training needs assessments, and capability roadmaps.", [("Services", "services.html"), ("Learning & Development", "learning-development.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Workforce Capability</span>
        <h2>Align Professional Development With Strategic Business Needs</h2>
        <p class="lead">Ad-hoc, uncoordinated training sessions rarely result in measurable workplace productivity improvements.</p>
        <p>Our learning and development consulting conducts thorough Training Needs Assessments (TNA), crafts role-specific learning paths, structures annual training calendars, and designs objective Kirkpatrick-level training evaluation frameworks.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      <div>
        <strong>Professional Scope Disclaimer:</strong> Our L&D advisory focuses on organizational learning strategy, competency modeling, and training program architecture. We do not claim external academic accreditations, formal university degrees, or certified statutory credentials.
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Capability Matrix</span>
      <h2>Illustrative Annual Training Calendar & Capability Program</h2>
      <p class="section-subtitle">Sample structured learning roadmap categorized by competency tier and participant groups.</p>
    </div>

    <div class="table-responsive">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Training Program</th>
            <th>Target Audience</th>
            <th>Competency Focus</th>
            <th>Duration & Format</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Supervisory Foundations</strong></td>
            <td>New People Managers</td>
            <td>1-on-1s, delegation, feedback delivery, conflict de-escalation</td>
            <td>4 Half-Days &bull; Interactive Workshop</td>
          </tr>
          <tr>
            <td><strong>Structured Interviewing & Sourcing</strong></td>
            <td>Hiring Managers & Recruiter Leads</td>
            <td>Competency rubrics, bias reduction, candidate experience</td>
            <td>2 Half-Days &bull; Case Simulation</td>
          </tr>
          <tr>
            <td><strong>Effective Workplace Communication</strong></td>
            <td>Cross-Functional Teams</td>
            <td>Interpersonal alignment, active listening, executive email etiquette</td>
            <td>1 Full Day &bull; Experiential Lab</td>
          </tr>
          <tr>
            <td><strong>OKR & Goal-Setting Masterclass</strong></td>
            <td>Department Heads & Leads</td>
            <td>Measurable KRA design, metric tracking, alignment cadences</td>
            <td>Half-Day &bull; Strategic Clinic</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

{get_cta_section("Design an Actionable L&D Roadmap", "Speak with our talent development specialists to structure a tailored capability strategy.")}
'''
    write_html_page("learning-development.html", "Learning & Development Consulting | Workforce Capability Strategy",
                    "Learning and development consulting to design training needs assessments, annual learning calendars, and organizational capability roadmaps.", content, "Services")

if __name__ == "__main__":
    build_hr_strategy()
    build_hr_audit()
    build_talent_acquisition()
    build_recruitment_consulting()
    build_workforce_planning()
    build_org_dev()
    build_hr_policies()
    build_employee_handbook()
    build_performance_mgmt()
    build_employee_engagement()
    build_learning_dev()
    print("Services 1 to 11 built successfully.")

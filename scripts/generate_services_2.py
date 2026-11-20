"""
Generates Services Pages 12 to 22:
- leadership-development.html
- compensation-benefits.html
- payroll-advisory.html
- hr-compliance.html
- posh-consulting.html
- employee-relations.html
- succession-planning.html
- change-management.html
- hr-technology.html
- hr-analytics.html
- hr-outsourcing.html
"""

from generator_data import register_img, render_img, get_page_hero, get_demo_disclaimer, get_cta_section, write_html_page

def build_leadership_dev():
    img = register_img(
        filename="leadership-development-executive-coaching.webp",
        page="leadership-development.html",
        section="Leadership Capability",
        desc="Senior corporate leadership coach conducting an executive strategy and decision-making clinic with corporate division leaders.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Executive leadership development coaching session. A seasoned corporate leadership advisor mentoring two department directors in an executive conference room. Authentic dialogue, high-end corporate setting, tailored business attire, warm natural lighting.",
        composition="Medium shot of leadership mentoring session",
        camera="50mm lens, f/2.8",
        lighting="Natural ambient morning lighting",
        bg="Minimalist executive boardroom with glass walls",
        subjects="Three corporate leaders in strategic discussion",
        neg_space="Upper quadrant clean"
    )

    content = f'''
{get_page_hero("Equip Leaders With Capability, Clarity, and Confidence", "Leadership development frameworks, managerial capability assessments, and executive succession advisory.", [("Services", "services.html"), ("Leadership Development", "leadership-development.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Executive Capability</span>
        <h2>Cultivate Leaders Who Drive Accountability and Culture</h2>
        <p class="lead">Great individual contributors often struggle when promoted into managerial roles without structured leadership training.</p>
        <p>Our leadership development advisory assesses managerial capability, designs practical coaching frameworks, and equips managers with critical decision-making, conflict resolution, and strategic delegation toolkits.</p>
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
        <strong>Advisory Scope Disclaimer:</strong> Leadership development programs represent organizational managerial training concepts. We do not claim certified psychological counseling credentials, accredited clinical coaching designations, or guaranteed executive career outcomes.
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Competency Architecture</span>
      <h2>Managerial Capability Framework Pillars</h2>
      <p class="section-subtitle">Core dimensions evaluated and developed across management tiers.</p>
    </div>

    <div class="grid grid-4 gap-md">
      <div class="card">
        <h4 class="card-title">1. Strategic Direction</h4>
        <p class="card-text">Translating overarching corporate vision into weekly operational goals, prioritizing resources, and setting clear team objectives.</p>
      </div>
      <div class="card">
        <h4 class="card-title">2. Team Enablement</h4>
        <p class="card-text">Conducting effective 1-on-1s, providing constructive performance feedback, and removing execution impediments for direct reports.</p>
      </div>
      <div class="card">
        <h4 class="card-title">3. Decision Making</h4>
        <p class="card-text">Navigating ambiguity, weighing trade-offs under pressure, and balancing long-term organizational health with short-term demands.</p>
      </div>
      <div class="card">
        <h4 class="card-title">4. Conflict Resolution</h4>
        <p class="card-text">De-escalating interpersonal tensions, aligning divergent departmental incentives, and fostering psychological safety.</p>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Strengthen Your Organization's Leadership Bench", "Speak with our leadership advisory team to formulate a manager enablement plan.")}
'''
    write_html_page("leadership-development.html", "Leadership Development Consulting | Executive Capability Frameworks",
                    "Leadership development consulting to assess manager capability, structure coaching frameworks, and build effective leadership pipelines.", content, "Services")

def build_compensation_benefits():
    img = register_img(
        filename="compensation-benefits-market-benchmarking.webp",
        page="compensation-benefits.html",
        section="Compensation Structuring",
        desc="Total rewards consultants reviewing salary grade models, pay equity distributions, and compensation structures on a digital dashboard.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Corporate compensation and benefits review meeting. Senior total rewards consultants and financial analysts evaluating salary grade bands, variable incentive formulas, and job leveling charts in a clean modern executive boardroom.",
        composition="Medium shot of compensation analysts reviewing reward models",
        camera="50mm lens, f/2.8",
        lighting="Even balanced corporate interior illumination",
        bg="Executive corporate office with sleek presentation displays",
        subjects="Two total rewards analysts in business attire",
        neg_space="Upper lateral section clean"
    )

    content = f'''
{get_page_hero("Competitive, Fair, and Transparent Reward Structures", "Design salary structures, job grade bandings, and performance-linked incentive frameworks.", [("Services", "services.html"), ("Compensation & Benefits", "compensation-benefits.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Total Rewards</span>
        <h2>Reward High Performance While Maintaining Fiscal Discipline</h2>
        <p class="lead">Disorganized pay structures create internal wage compression, demotivate top performers, and strain operating budgets.</p>
        <p>Our compensation and benefits consulting helps organizations engineer structured pay scales, transparent job grading systems, variable performance bonus schemes, and attractive non-monetary benefit portfolios.</p>
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
        <strong>Demonstration Notice:</strong> All compensation structures, salary bands, and benchmarking methodologies shown below represent illustrative demonstration templates. We do not publish proprietary third-party market salary survey databases or claim access to verified statutory wage data without independent client licensing.
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Salary Architecture</span>
      <h2>Illustrative Salary Grade & Compensation Structure</h2>
      <p class="section-subtitle">Sample framework illustrating fixed pay, variable ratios, and spread across organizational tiers.</p>
    </div>

    <div class="table-responsive">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Grade Level</th>
            <th>Sample Role Categories</th>
            <th>Fixed / Variable Split</th>
            <th>Sample Band Spread</th>
            <th>Key Reward Drivers</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Grade G1</strong></td>
            <td>Associates & Specialists</td>
            <td>90% Fixed / 10% Variable</td>
            <td>&plusmn; 15% Midpoint Spread</td>
            <td>Task accuracy, skill milestones, operational reliability.</td>
          </tr>
          <tr>
            <td><strong>Grade G2</strong></td>
            <td>Senior Specialists & Team Leads</td>
            <td>80% Fixed / 20% Variable</td>
            <td>&plusmn; 20% Midpoint Spread</td>
            <td>Project delivery, quality metrics, peer enablement.</td>
          </tr>
          <tr>
            <td><strong>Grade G3</strong></td>
            <td>Managers & Practice Leads</td>
            <td>70% Fixed / 30% Variable</td>
            <td>&plusmn; 25% Midpoint Spread</td>
            <td>Departmental goals, client retention, team retention.</td>
          </tr>
          <tr>
            <td><strong>Grade G4</strong></td>
            <td>Executive Directors & VPs</td>
            <td>55% Fixed / 45% Variable</td>
            <td>&plusmn; 30% Midpoint Spread</td>
            <td>Enterprise profitability, multi-year business growth.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

{get_cta_section("Review Your Organization's Compensation Structure", "Speak with our compensation consultants to design structured salary bands.")}
'''
    write_html_page("compensation-benefits.html", "Compensation & Benefits Consulting | Salary Grading & Total Rewards",
                    "Compensation and benefits consulting to structure salary grades, job evaluation frameworks, variable bonus plans, and total rewards models.", content, "Services")

def build_payroll_advisory():
    img = register_img(
        filename="payroll-advisory-workflow-review.webp",
        page="payroll-advisory.html",
        section="Payroll Process Advisory",
        desc="Payroll process consultants and financial controllers reviewing attendance reconciliation data and payroll workflows in an office.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Corporate payroll process advisory meeting. Finance controller and HR operations consultants reviewing attendance reconciliation workflows, leave deduction formulas, and payroll disbursement spreadsheets on a tablet and laptop. Professional corporate setting.",
        composition="Medium shot showing detailed process review and reconciliation sheets",
        camera="50mm lens, f/2.8",
        lighting="Clear balanced daylight",
        bg="Corporate finance and HR operations office",
        subjects="Two business professionals in professional attire",
        neg_space="Upper quadrant clean"
    )

    content = f'''
{get_page_hero("Payroll Process Assessment & Workflow Advisory", "Optimize payroll calculation workflows, attendance coordination, and vendor SLA management.", [("Services", "services.html"), ("Payroll Advisory", "payroll-advisory.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Process Hygiene</span>
        <h2>Ensure Accurate, On-Time, and Friction-Free Payroll Operations</h2>
        <p class="lead">Discrepancies in attendance data, delayed reimbursement approvals, and manual calculation errors damage employee trust and waste hours.</p>
        <p>Our payroll advisory service evaluates end-to-end payroll data collection, optimizes attendance integration pipelines, establishes clear reconciliation checklists, and evaluates third-party payroll software or outsourced processing vendors.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
        <line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
      <div>
        <strong>Critical Operational Scope Distinction:</strong>
        <p style="margin-top:0.25rem;">This service provides managerial process advisory and operational workflow design. We do not act as an outsourced payroll bureau, nor do we directly execute fund transfers, statutory tax filings (TDS, PF, ESI), or financial banking operations. Actual disbursement and filings remain the responsibility of the organization's designated finance team or authorized statutory processors.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Workflow Timeline</span>
      <h2>Illustrative Monthly Payroll Operational Workflow</h2>
      <p class="section-subtitle">A disciplined timeline designed to eliminate month-end panic and ensure accurate disbursals.</p>
    </div>

    <div class="pipeline-container">
      <div class="pipeline-step">
        <span class="pipeline-step-num">Day 20 &ndash; 22</span>
        <span class="pipeline-step-title">Attendance Cutoff</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Lock biometric data & leave approvals.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Day 23 &ndash; 24</span>
        <span class="pipeline-step-title">Variable Inputs</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Reimbursements, incentives & new joiners.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Day 25 &ndash; 26</span>
        <span class="pipeline-step-title">Reconciliation</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Variance audit vs previous payroll cycle.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Day 27 &ndash; 28</span>
        <span class="pipeline-step-title">Management Sign-Off</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Finance authorization & disbursement file.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Payday</span>
        <span class="pipeline-step-title">Disbursal & Payslips</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Bank upload & automated payslip delivery.</p>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Improve Your Payroll Process Efficiency", "Request a process review consultation with our payroll operations team.")}
'''
    write_html_page("payroll-advisory.html", "Payroll Advisory Services | Workflow & Process Optimization",
                    "Payroll advisory services to assess payroll workflows, attendance data pipelines, reconciliation checklists, and vendor coordination.", content, "Services")

def build_hr_compliance():
    img = register_img(
        filename="hr-compliance-statutory-calendar.webp",
        page="hr-compliance.html",
        section="Compliance Advisory",
        desc="HR compliance advisors reviewing statutory calendars, labor record registers, and compliance checklists in a corporate legal suite.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional HR compliance advisory meeting. Senior human capital compliance consultants examining statutory filing calendars, regulatory checklists, and personnel record registers in a modern legal library corporate office. Calm, rigorous atmosphere.",
        composition="Medium shot of advisors analyzing regulatory calendars",
        camera="50mm lens, f/2.8",
        lighting="Even balanced corporate office light",
        bg="Corporate legal and compliance boardroom",
        subjects="Two compliance consultants in smart business wear",
        neg_space="Upper lateral section clean"
    )

    content = f'''
{get_page_hero("HR Compliance Advisory & Documentation Hygiene", "Review internal employment records, statutory documentation calendars, and process governance.", [("Services", "services.html"), ("HR Compliance", "hr-compliance.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Governance & Hygiene</span>
        <h2>Establish Rigorous HR Record Management and Filing Calendars</h2>
        <p class="lead">Non-compliance with employment record maintenance causes unexpected regulatory penalties and administrative headaches during inspections.</p>
        <p>Our HR compliance advisory helps organizations organize employee personnel files, maintain required statutory registers, establish annual compliance calendars, and verify that standard employment agreements align with current operating norms.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
        <line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
      <div>
        <strong>Crucial Compliance & Legal Safeguard Notice:</strong>
        <p style="margin-top:0.25rem;">This website and our advisory services provide operational HR management guidance and documentation hygiene assistance. We do NOT provide formal legal advice, court representation, statutory certifications, or guaranteed governmental approvals.</p>
        <p style="margin-top:0.5rem; font-size:0.8125rem;">For Indian employment matters, statutory requirements (e.g. Shops & Establishments Acts, EPF, ESI, Payment of Gratuity, POSH) vary strictly based on company state of registration, physical establishment locations, headcount thresholds, and worker categories. All internal policies, contracts, and filings must be formally reviewed by qualified legal counsel or practicing statutory specialists using current official government notifications.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Compliance Calendar</span>
      <h2>Illustrative Annual HR Compliance Framework</h2>
      <p class="section-subtitle">Sample periodic operational checks to maintain administrative readiness.</p>
    </div>

    <div class="grid grid-3 gap-lg">
      <div class="card">
        <h4 class="card-title">Monthly Hygiene Checks</h4>
        <ul class="deliverables-list">
          <li>Attendance & overtime record reconciliations.</li>
          <li>New joiner statutory declaration collections (PF Form 11, etc.).</li>
          <li>Monthly wage slip generation and employee acknowledgment.</li>
        </ul>
      </div>

      <div class="card">
        <h4 class="card-title">Quarterly Governance Audits</h4>
        <ul class="deliverables-list">
          <li>Internal Committee (IC) POSH meeting records.</li>
          <li>Contract labor attendance and vendor compliance certificates.</li>
          <li>Personnel file physical/digital completeness audits.</li>
        </ul>
      </div>

      <div class="card">
        <h4 class="card-title">Annual Filings & Policy Reviews</h4>
        <ul class="deliverables-list">
          <li>Annual POSH report submission to the District Officer.</li>
          <li>Leave balance carry-forward and encashment calculations.</li>
          <li>Annual update of workplace policy manuals & employee handbooks.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Assess Your HR Compliance Hygiene", "Connect with our advisory practice to review your internal HR record management systems.")}
'''
    write_html_page("hr-compliance.html", "HR Compliance Advisory | Employment Record Hygiene & Calendars",
                    "HR compliance advisory services to assess personnel documentation, establish compliance calendars, and improve administrative hygiene.", content, "Services")

def build_posh_consulting():
    img = register_img(
        filename="posh-consulting-workplace-awareness.webp",
        page="posh-consulting.html",
        section="POSH Advisory",
        desc="A corporate POSH awareness seminar in progress with employees attending a workplace dignity and respect session in an auditorium.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional corporate workplace conduct and POSH awareness seminar. An experienced human resources advisor leading a presentation on respectful workplace practices, employee dignity, and grievance redressing in a brightly lit corporate auditorium. Attentive professionals listening.",
        composition="Medium wide shot of presenter and attentive corporate audience",
        camera="50mm lens, f/2.8",
        lighting="Natural ambient daylight with warm fill",
        bg="Contemporary corporate amphitheater with presentation screen",
        subjects="Professional speaker and corporate employees",
        neg_space="Upper lateral area uncluttered"
    )

    content = f'''
{get_page_hero("Support a Safer, More Respectful Workplace", "POSH policy guidance, employee awareness program design, and Internal Committee procedural advisory.", [("Services", "services.html"), ("POSH Consulting", "posh-consulting.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Workplace Dignity</span>
        <h2>Fostering an Inclusive, Respectful, and Harassment-Free Culture</h2>
        <p class="lead">Under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 (POSH) in India, organizations are mandated to maintain safe, harassment-free working environments.</p>
        <p>Our consulting practice assists organizations in drafting clear POSH policies, designing engaging employee awareness sessions, guiding the administrative establishment of Internal Committees (IC), and setting up procedural documentation for timely grievance handling.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
        <line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line>
      </svg>
      <div>
        <strong>Mandatory India-Specific Legal & Ethical Notice:</strong>
        <p style="margin-top:0.25rem;">This service provides procedural guidance, educational program structuring, and managerial documentation assistance. We are NOT a legal body, judicial tribunal, or court of law, and we do NOT provide legal representation.</p>
        <p style="margin-top:0.5rem; font-size:0.8125rem;">We do not invent Internal Committee members, make claims of guaranteed statutory immunity, or display fabricated complaint records. All organizations must ensure their Internal Committee composition, inquiry processes, and annual district reporting are formally validated against current Indian statutory rules and confirmed by qualified legal counsel.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">POSH Architecture</span>
      <h2>Core Components of Our POSH Advisory Framework</h2>
      <p class="section-subtitle">Structured enablement covering policy drafting, workforce education, and committee readiness.</p>
    </div>

    <div class="grid grid-3 gap-lg">
      <div class="card">
        <h4 class="card-title">1. Policy & Notice Drafting</h4>
        <p class="card-text">Developing comprehensive, accessible POSH policy documents, employee sign-off acknowledgments, and prominent statutory display notices for office premises.</p>
      </div>
      <div class="card">
        <h4 class="card-title">2. Workforce Awareness Programs</h4>
        <p class="card-text">Designing role-specific training modules that define appropriate workplace conduct, clarify reporting channels, and reinforce zero-tolerance principles.</p>
      </div>
      <div class="card">
        <h4 class="card-title">3. IC Procedural Guidance</h4>
        <p class="card-text">Orienting Internal Committee members on principles of natural justice, confidential inquiry protocols, documentation templates, and annual report formatting.</p>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Schedule a POSH Advisory Consultation", "Contact our advisory practice to discuss workplace awareness programs and IC enablement.")}
'''
    write_html_page("posh-consulting.html", "POSH Consulting Services | Workplace Awareness & IC Guidance",
                    "POSH consulting services for Indian workplaces covering policy drafting, employee awareness workshops, and Internal Committee procedural guidance.", content, "Services")

def build_employee_relations():
    img = register_img(
        filename="employee-relations-conflict-resolution.webp",
        page="employee-relations.html",
        section="Workplace Relations",
        desc="Senior HR relations advisor mediating a constructive conversation between departmental managers in a calm meeting suite.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional workplace mediation and employee relations discussion. A neutral senior HR consultant facilitating a calm, constructive dialogue between two business leaders in a private modern corporate suite. Respectful body language, soft ambient daylight.",
        composition="Medium shot showing constructive facilitated discussion",
        camera="50mm lens, f/2.8",
        lighting="Soft natural window lighting",
        bg="Minimalist modern meeting room with warm wooden details",
        subjects="Three professionals engaged in thoughtful conversation",
        neg_space="Upper lateral section clear"
    )

    content = f'''
{get_page_hero("Build Trust Through Transparent Employee Relations", "Fair grievance mechanisms, conflict resolution processes, and objective disciplinary procedures.", [("Services", "services.html"), ("Employee Relations", "employee-relations.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Workplace Harmony</span>
        <h2>Resolve Friction Early Before It Escalates Into Formal Disputes</h2>
        <p class="lead">Unresolved interpersonal friction, perceived manager bias, and unfair disciplinary handling erode team morale and create organizational toxicity.</p>
        <p>Our employee relations consulting helps management build fair, documented dispute escalation ladders, train line managers in active listening, draft transparent disciplinary standard operating procedures, and create a culture of mutual respect.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    {get_demo_disclaimer("Dispute escalation models and grievance frameworks presented on this page are procedural templates designed for operational management.")}
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Dispute Resolution</span>
      <h2>Illustrative 4-Tier Workplace Grievance Escalation SOP</h2>
      <p class="section-subtitle">A balanced, step-by-step mechanism protecting employee rights while resolving issues promptly.</p>
    </div>

    <div class="pipeline-container">
      <div class="pipeline-step">
        <span class="pipeline-step-num">Tier 1</span>
        <span class="pipeline-step-title">Informal Dialogue</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Facilitated direct 1-on-1 between parties within 3 business days.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Tier 2</span>
        <span class="pipeline-step-title">Department Review</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Written submission to Department Head & designated HR Business Partner.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Tier 3</span>
        <span class="pipeline-step-title">Formal Hearing</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Internal Grievance Committee review with documented findings.</p>
      </div>
      <div class="pipeline-step">
        <span class="pipeline-step-num">Tier 4</span>
        <span class="pipeline-step-title">Executive Appeal</span>
        <p style="font-size:0.75rem; color:var(--color-secondary-text); margin-top:0.35rem;">Final appeal to Managing Director / Executive Leadership.</p>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Strengthen Your Employee Relations Framework", "Consult with our workplace relations advisors to establish clear dispute mechanisms.")}
'''
    write_html_page("employee-relations.html", "Employee Relations Consulting | Conflict Resolution & Grievance Systems",
                    "Employee relations consulting to establish fair workplace grievance procedures, conflict resolution frameworks, and disciplinary protocols.", content, "Services")

def build_succession_planning():
    img = register_img(
        filename="succession-planning-talent-matrix.webp",
        page="succession-planning.html",
        section="Succession & Leadership Pipeline",
        desc="Corporate executive board analyzing a 9-box talent matrix and critical role continuity blueprints in an executive boardroom.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Executive succession planning meeting. Corporate leadership team examining a 9-box performance and potential talent matrix on an interactive display wall. Sophisticated corporate environment, rich navy accents, tailored business suits, high-end photography.",
        composition="Medium wide shot of board members evaluating succession chart",
        camera="50mm lens, f/2.8",
        lighting="Architectural recessed lighting balanced with screen glow",
        bg="High-end corporate boardroom with acoustic felt and wood paneling",
        subjects="Three senior executives reviewing talent pipeline",
        neg_space="Left upper section uncluttered"
    )

    content = f'''
{get_page_hero("Safeguard Organizational Continuity With Succession Planning", "Identify critical enterprise roles, assess high-potential successors, and structure transition plans.", [("Services", "services.html"), ("Succession Planning", "succession-planning.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Talent Continuity</span>
        <h2>Protect Your Business From Sudden Leadership Vacancies</h2>
        <p class="lead">The unexpected departure of key executive or specialized technical talent can stall strategic projects and compromise client relationships.</p>
        <p>Our succession planning consulting identifies single-point-of-failure roles, deploys 9-box talent potential matrices, formulates personalized readiness development tracks, and ensures knowledge transfer protocols are embedded before leadership transitions occur.</p>
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
      <span class="section-tag">Talent Matrix</span>
      <h2>Illustrative 9-Box Talent Assessment Grid Mockup</h2>
      <p class="section-subtitle">A proven methodology for evaluating employee performance alongside future growth potential.</p>
    </div>

    <div class="hr-dashboard">
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <span class="dashboard-title">9-Box Succession Readiness Matrix (Sample Demonstration Data)</span>
        </div>
        <span class="badge badge-demo">Illustrative Demo Data</span>
      </div>
      <div class="dashboard-body">
        <div class="grid grid-3 gap-md">
          <div class="card" style="background:#F0FDF4; border-color:#86EFAC;">
            <h4 style="color:#166534; font-size:1rem;">High Potential &bull; High Performance</h4>
            <p style="font-size:0.84rem; margin-bottom:0.5rem;"><strong>Future Enterprise Leaders (12% Demo Pool)</strong></p>
            <p style="font-size:0.8125rem;">Accelerated executive mentorship, cross-functional assignments, board exposure.</p>
          </div>
          <div class="card" style="background:#F8FAFC;">
            <h4 style="color:var(--color-dark-navy); font-size:1rem;">Moderate Potential &bull; High Performance</h4>
            <p style="font-size:0.84rem; margin-bottom:0.5rem;"><strong>Core Functional Pillars (28% Demo Pool)</strong></p>
            <p style="font-size:0.8125rem;">Deep subject matter expertise, specialized training, role retention bonuses.</p>
          </div>
          <div class="card" style="background:#FEF3C7; border-color:#FCD34D;">
            <h4 style="color:#92400E; font-size:1rem;">High Potential &bull; Developing Performance</h4>
            <p style="font-size:0.84rem; margin-bottom:0.5rem;"><strong>Emerging Stars (14% Demo Pool)</strong></p>
            <p style="font-size:0.8125rem;">Targeted skill coaching, pairing with senior mentors, clear milestone targets.</p>
          </div>
        </div>
      </div>
    </div>

    {get_demo_disclaimer("Talent ratings, percentages, and matrix categories displayed above are non-operational demonstration models.")}
  </div>
</section>

{get_cta_section("Build Your Executive Succession Pipeline", "Connect with our succession planning practice to identify and prepare future leadership talent.")}
'''
    write_html_page("succession-planning.html", "Succession Planning Consulting | 9-Box Talent Matrix & Continuity",
                    "Succession planning consulting to identify critical roles, deploy 9-box talent matrices, and design leadership continuity transition plans.", content, "Services")

def build_change_mgmt():
    img = register_img(
        filename="change-management-transformation-roadmap.webp",
        page="change-management.html",
        section="Transformation Strategy",
        desc="Change management consultants conducting a transformation readiness workshop with department heads around an interactive roadmap.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Corporate change management and workforce transformation workshop. Senior change management consultants presenting an organizational transition roadmap on an interactive whiteboard to attentive department leaders. Collaborative, professional atmosphere.",
        composition="Wide shot of executives and consultants mapping transformation phases",
        camera="35mm lens, f/3.2",
        lighting="Natural ambient morning lighting",
        bg="Contemporary corporate workshop studio with whiteboards",
        subjects="Four business leaders collaborating actively",
        neg_space="Upper lateral area uncluttered"
    )

    content = f'''
{get_page_hero("Navigate Workforce Change With Confidence", "Strategic change management consulting for restructuring, mergers, leadership changes, and system rollouts.", [("Services", "services.html"), ("Change Management", "change-management.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Transformation Support</span>
        <h2>Minimize Employee Anxiety and Accelerate Adoption During Transitions</h2>
        <p class="lead">Over 70% of organizational restructuring initiatives stumble not because of technical flaws, but due to unaddressed workforce resistance.</p>
        <p>Our change management consulting guides leadership through complex organizational shifts. We conduct change readiness assessments, craft empathetic multi-channel communication plans, align middle managers as change ambassadors, and track team sentiment through adoption metrics.</p>
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
      <span class="section-tag">Change Framework</span>
      <h2>Illustrative 4-Phase Organizational Change Framework</h2>
      <p class="section-subtitle">A proven methodology ensuring workforce stability throughout organizational evolutions.</p>
    </div>

    <div class="grid grid-4 gap-md">
      <div class="card">
        <h4 class="card-title">Phase 1: Assess</h4>
        <p class="card-text">Conducting stakeholder impact analyses, identifying resistance pockets, and measuring baseline cultural readiness.</p>
      </div>
      <div class="card">
        <h4 class="card-title">Phase 2: Engage</h4>
        <p class="card-text">Formulating executive messaging, briefing people managers, and conducting all-hands briefings to communicate 'why'.</p>
      </div>
      <div class="card">
        <h4 class="card-title">Phase 3: Transition</h4>
        <p class="card-text">Delivering role-specific training workshops, launching peer coaching networks, and establishing live feedback desks.</p>
      </div>
      <div class="card">
        <h4 class="card-title">Phase 4: Sustain</h4>
        <p class="card-text">Monitoring adoption KPIs, celebrating early transition milestones, and embedding new behaviors into review criteria.</p>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Lead Your Next Transformation Successfully", "Speak with our change management practice to evaluate transition readiness.")}
'''
    write_html_page("change-management.html", "Change Management Consulting | Organizational Transformation Strategy",
                    "Change management consulting to evaluate workforce change readiness, design stakeholder communications, and drive system adoption.", content, "Services")

def build_hr_technology():
    img = register_img(
        filename="hr-technology-hrms-evaluation.webp",
        page="hr-technology.html",
        section="HR Technology Selection",
        desc="HR technology consultants and IT directors evaluating cloud HRMS software solutions and automated onboarding workflows on laptops.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="HR technology consulting meeting. Enterprise IT directors and HR tech advisors evaluating human capital software interfaces and cloud HRMS modules on a high-definition monitor in a modern corporate boardroom.",
        composition="Medium shot of technology advisors reviewing software workflows",
        camera="50mm lens, f/2.8",
        lighting="Clear crisp daylight balanced with screen glow",
        bg="Modern high-tech corporate conference room",
        subjects="Three business professionals analyzing software platforms",
        neg_space="Upper quadrant clean"
    )

    content = f'''
{get_page_hero("Use the Right HR Technology to Simplify People Management", "Independent HRMS evaluation, software requirements planning, and digital HR roadmap design.", [("Services", "services.html"), ("HR Technology", "hr-technology.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Digital Enablement</span>
        <h2>Select and Implement the Right Tools Without Vendor Bias</h2>
        <p class="lead">Organizations frequently waste significant capital investing in bloated software that employees find cumbersome and refuse to adopt.</p>
        <p>Our HR technology advisory acts as an independent partner. We map your specific workflows, author rigorous RFP requirement matrices, objectively evaluate commercial HRMS vendors, and oversee configuration and user adoption.</p>
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
        <strong>Demonstration Notice:</strong> The HRMS interface shown below is an illustrative conceptual mockup for demonstration purposes. It is not connected to a live production database or any proprietary software vendor.
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Interface Mockup</span>
      <h2>Illustrative Cloud HRMS Dashboard Architecture</h2>
      <p class="section-subtitle">Sample unified portal architecture integrating employee self-service, leave, and review modules.</p>
    </div>

    <div class="hr-dashboard">
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <span class="dashboard-title">Centralized HRMS Portal Mockup</span>
        </div>
        <span class="badge badge-demo">Illustrative Demo Interface</span>
      </div>
      <div class="dashboard-body">
        <div class="grid grid-3 gap-md">
          <div class="card">
            <h4 class="card-title" style="font-size:1rem;">Employee Self-Service (ESS)</h4>
            <p class="card-text" style="font-size:0.84rem;">Digital leave requests, profile updates, tax declaration uploads, and payslip downloads.</p>
            <span class="badge badge-teal">Integrated Module</span>
          </div>
          <div class="card">
            <h4 class="card-title" style="font-size:1rem;">Applicant Tracking (ATS)</h4>
            <p class="card-text" style="font-size:0.84rem;">Centralized candidate resume parsing, interview scheduling, and feedback scorecard logging.</p>
            <span class="badge badge-teal">Integrated Module</span>
          </div>
          <div class="card">
            <h4 class="card-title" style="font-size:1rem;">Continuous Performance</h4>
            <p class="card-text" style="font-size:0.84rem;">Quarterly OKR tracking, peer 360 recognition badges, and automated review reminders.</p>
            <span class="badge badge-teal">Integrated Module</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Modernize Your HR Technology Stack", "Schedule an independent HR software selection consultation with our systems advisors.")}
'''
    write_html_page("hr-technology.html", "HR Technology Consulting | HRMS Selection & Software Advisory",
                    "Independent HR technology consulting to evaluate HRMS software, author RFP requirements, and guide system implementation.", content, "Services")

def build_hr_analytics():
    img = register_img(
        filename="hr-analytics-dashboard-interactive.webp",
        page="hr-analytics.html",
        section="People Analytics",
        desc="Human capital data analysts and corporate HR directors reviewing headcount velocity, turnover rates, and retention models on a dashboard.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="People analytics and HR data science presentation. A data consultant explaining predictive employee turnover charts and workforce retention models on a massive ultra-wide screen in a sleek corporate war room. Professional, analytical setting.",
        composition="Wide shot of analysts collaborating around luminous dashboard screen",
        camera="35mm lens, f/3.5",
        lighting="Ambient corporate lighting with screen radiance",
        bg="High-tech corporate analytics suite",
        subjects="Three professionals reviewing workforce data charts",
        neg_space="Upper lateral section clear"
    )

    content = f'''
{get_page_hero("Make Informed People Decisions With HR Analytics", "Transform workforce data into executive insight with structured reporting dashboards and KPI scorecards.", [("Services", "services.html"), ("HR Analytics", "hr-analytics.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Evidence-Based HR</span>
        <h2>Replace Guesswork With Clear Workforce Intelligence</h2>
        <p class="lead">Most organizations sit on treasure troves of unanalyzed people data: attendance logs, interview notes, exit surveys, and review scores.</p>
        <p>Our HR analytics consulting helps management clean, structure, and visualize critical people metrics. We establish executive KPI dashboards, track voluntary turnover patterns, analyze recruitment bottlenecks, and evaluate the ROI of training investments.</p>
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
      <span class="section-tag">Interactive Analytics</span>
      <h2>Interactive Workforce Analytics Dashboard (Demo Model)</h2>
      <p class="section-subtitle">Use the department filter below to examine illustrative demonstration metrics.</p>
    </div>

    <div class="hr-dashboard">
      <div class="dashboard-header">
        <div class="dashboard-title-group">
          <span class="dashboard-title">Executive Workforce Intelligence Suite</span>
        </div>
        <div style="display:flex; align-items:center; gap:0.75rem;">
          <select id="analyticsDeptFilter" class="form-select" style="padding:0.35rem 0.75rem; font-size:0.8125rem; background:white; color:var(--color-dark-navy);">
            <option value="all">All Departments</option>
            <option value="engineering">Engineering & Product</option>
            <option value="sales">Sales & Commercial</option>
            <option value="operations">Client Operations</option>
            <option value="support">Customer Support</option>
          </select>
          <span class="badge badge-demo">Illustrative Demo Data</span>
        </div>
      </div>
      <div class="dashboard-body">
        <div class="metric-grid">
          <div class="metric-card">
            <div class="metric-label">Total Headcount</div>
            <div class="metric-value" id="analyticsHeadcountVal">482</div>
            <div class="metric-sub">Active Full-Time Staff</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Annualized Turnover</div>
            <div class="metric-value" id="analyticsTurnoverVal">7.8%</div>
            <div class="metric-sub">Target: Below 10.0%</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Retention Rate</div>
            <div class="metric-value" id="analyticsRetentionVal">92.2%</div>
            <div class="metric-sub">Rolling 12 Months</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">Open Requisitions</div>
            <div class="metric-value" id="analyticsOpenRolesVal">24</div>
            <div class="metric-sub">Avg 32 Days to Fill</div>
          </div>
        </div>

        <div class="grid grid-2 gap-md">
          <div class="chart-card">
            <div class="chart-title">
              <span>Departmental Headcount Allocation</span>
              <span style="font-size:0.75rem; color:var(--color-secondary-text);">Current Pool</span>
            </div>
            <div class="bar-row">
              <span class="bar-label">Product & Engineering</span>
              <div class="bar-track"><div class="bar-fill" style="width: 38%;"></div></div>
              <span class="bar-value">185</span>
            </div>
            <div class="bar-row">
              <span class="bar-label">Sales & Marketing</span>
              <div class="bar-track"><div class="bar-fill" style="width: 23%;"></div></div>
              <span class="bar-value">112</span>
            </div>
            <div class="bar-row">
              <span class="bar-label">Client Operations</span>
              <div class="bar-track"><div class="bar-fill" style="width: 20%;"></div></div>
              <span class="bar-value">95</span>
            </div>
            <div class="bar-row">
              <span class="bar-label">Customer Support</span>
              <div class="bar-track"><div class="bar-fill" style="width: 19%;"></div></div>
              <span class="bar-value">90</span>
            </div>
          </div>

          <div class="chart-card">
            <div class="chart-title">
              <span>Performance Band Distribution</span>
              <span style="font-size:0.75rem; color:var(--color-secondary-text);">Latest Evaluation Cycle</span>
            </div>
            <div class="bar-row">
              <span class="bar-label">Top Quartile (L4/L5)</span>
              <div class="bar-track"><div class="bar-fill" style="width: 24%;"></div></div>
              <span class="bar-value">24%</span>
            </div>
            <div class="bar-row">
              <span class="bar-label">Solid Performers (L3)</span>
              <div class="bar-track"><div class="bar-fill" style="width: 63%;"></div></div>
              <span class="bar-value">63%</span>
            </div>
            <div class="bar-row">
              <span class="bar-label">Performance Watch (L1/L2)</span>
              <div class="bar-track"><div class="bar-fill fill-gold" style="width: 13%;"></div></div>
              <span class="bar-value">13%</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    {get_demo_disclaimer("Illustrative Demo Data &mdash; Not Actual Employee Information. Charts and metrics displayed above are fictional demonstration models.")}
  </div>
</section>

{get_cta_section("Implement Executive People Analytics", "Connect with our workforce data specialists to structure customized HR reporting dashboards.")}
'''
    write_html_page("hr-analytics.html", "HR Analytics Consulting | Workforce Reporting & People Dashboards",
                    "HR analytics consulting to design executive workforce dashboards, turnover predictive metrics, and headcount analytics scorecards.", content, "Services")

def build_hr_outsourcing():
    img = register_img(
        filename="hr-outsourcing-managed-operations.webp",
        page="hr-outsourcing.html",
        section="Managed HR Operations",
        desc="Dedicated HR operations specialists managing daily onboarding documentation, employee tickets, and administrative records in a corporate office.",
        ratio="16:9",
        res="1920x1080",
        orientation="Landscape",
        prompt="Professional managed HR operations and outsourcing center. Experienced human resources administrators managing employee onboarding files, digital records, and personnel support tickets in a bright, modern corporate support center.",
        composition="Medium wide shot of professionals managing HR operations",
        camera="50mm lens, f/2.8",
        lighting="Bright natural ambient office lighting",
        bg="Contemporary corporate operational facility",
        subjects="Three professionals engaged in HR administration",
        neg_space="Upper lateral section clear"
    )

    content = f'''
{get_page_hero("Scalable HR Operations & Administration Support", "Reliable managed HR support to handle day-to-day employee lifecycle administration and operational tasks.", [("Services", "services.html"), ("HR Outsourcing", "hr-outsourcing.html")])}

<section class="section">
  <div class="container">
    <div class="grid grid-2 items-center gap-xl">
      <div>
        <span class="section-tag">Operational Support</span>
        <h2>Free Your Leadership From Daily Administrative Overload</h2>
        <p class="lead">Managing offer letters, employee file archiving, leave queries, and asset tracking consumes disproportionate founder and managerial time.</p>
        <p>Our managed HR outsourcing support acts as your extended virtual HR department. We handle routine employee lifecycle documentation, new joiner onboarding logistics, leave reconciliation, and internal HR query coordination under strictly agreed service levels.</p>
      </div>
      <div>
        {render_img(img)}
      </div>
    </div>

    <div class="demo-banner" style="margin-top:2.5rem;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      <div>
        <strong>Contractual Scope & Service Boundary Distinction:</strong>
        <p style="margin-top:0.25rem;">We clearly distinguish strategic HR consulting from operational HR outsourcing and payroll processing. All outsourcing engagements require formal service-level agreements (SLAs), confidentiality protocols, data privacy safeguards, and clearly defined operational authority boundaries.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-bg-alt">
  <div class="container">
    <div class="section-header text-center">
      <span class="section-tag">Service Scope</span>
      <h2>Core Outsourced HR Operational Capabilities</h2>
      <p class="section-subtitle">Flexible support models tailored for startups, expanding SMEs, and decentralized teams.</p>
    </div>

    <div class="grid grid-3 gap-lg">
      <div class="card">
        <h4 class="card-title">Onboarding Coordination</h4>
        <p class="card-text">Sending welcome kits, gathering employee documentation, initiating background verification checks, and scheduling orientation.</p>
      </div>
      <div class="card">
        <h4 class="card-title">Employee Query Helpdesk</h4>
        <p class="card-text">Responding to staff questions regarding leave balances, policy clarifications, insurance claims, and employment letters.</p>
      </div>
      <div class="card">
        <h4 class="card-title">Exit Administration</h4>
        <p class="card-text">Coordinating asset return clearances with IT/finance, scheduling exit interviews, and generating service certificates.</p>
      </div>
    </div>
  </div>
</section>

{get_cta_section("Explore Scalable Outsourced HR Support", "Contact our advisory practice to design a customized managed HR support agreement.")}
'''
    write_html_page("hr-outsourcing.html", "HR Outsourcing Services | Managed People Operations & Administration",
                    "Managed HR outsourcing solutions providing reliable support for employee onboarding, documentation, leave management, and lifecycle administration.", content, "Services")

if __name__ == "__main__":
    build_leadership_dev()
    build_compensation_benefits()
    build_payroll_advisory()
    build_hr_compliance()
    build_posh_consulting()
    build_employee_relations()
    build_succession_planning()
    build_change_mgmt()
    build_hr_technology()
    build_hr_analytics()
    build_hr_outsourcing()
    print("Services 12 to 22 built successfully.")

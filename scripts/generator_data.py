"""
HR CONSULTING COMPANY — Shared Data & Helpers
"""

import json
import os

IMAGE_CATALOG = []

def register_img(filename, page, section, desc, ratio="16:9", res="1920x1080", orientation="Landscape",
                 prompt="", composition="", camera="", lighting="", bg="", style="Premium Corporate Photography",
                 subjects="", neg_space="Clean upper or lateral area for text overlay"):
    img_id = f"IMG-{len(IMAGE_CATALOG)+1:02d}"
    item = {
        "id": img_id,
        "num": len(IMAGE_CATALOG)+1,
        "filename": filename,
        "page": page,
        "section": section,
        "desc": desc,
        "ratio": ratio,
        "res": res,
        "orientation": orientation,
        "prompt": prompt,
        "composition": composition,
        "camera": camera,
        "lighting": lighting,
        "bg": bg,
        "style": style,
        "subjects": subjects,
        "neg_space": neg_space
    }
    IMAGE_CATALOG.append(item)
    return item

def render_img(item, extra_class=""):
    ratio_class = "ratio-16-9"
    if item["ratio"] == "4:3":
        ratio_class = "ratio-4-3"
    elif item["ratio"] == "1:1":
        ratio_class = "ratio-1-1"
    elif item["ratio"] == "21:9":
        ratio_class = "ratio-21-9"
    elif item["ratio"] == "3:4":
        ratio_class = "ratio-3-4"

    res_parts = item["res"].split("x")
    width = res_parts[0] if len(res_parts) == 2 else "1920"
    height = res_parts[1] if len(res_parts) == 2 else "1080"

    base_name = os.path.splitext(item["filename"])[0]
    img_src = f"images/{base_name}.jpeg"

    style_attr = ""
    classes = f"site-img {ratio_class}"
    if extra_class.strip().startswith("style="):
        style_attr = " " + extra_class.strip()
    elif extra_class:
        classes += f" {extra_class.strip()}"

    if item["filename"] == "hero-hr-consulting-team.webp":
        loading_attr = 'loading="eager" fetchpriority="high"'
    else:
        loading_attr = 'loading="lazy"'

    return f'''<img src="{img_src}" alt="{item['desc']}" class="{classes}" width="{width}" height="{height}" {loading_attr}{style_attr}>'''

def get_page_hero(title, subtitle, crumbs):
    crumb_html = '<a href="index.html">Home</a> <span>/</span> '
    for c_title, c_link in crumbs[:-1]:
        crumb_html += f'<a href="{c_link}">{c_title}</a> <span>/</span> '
    last_title, _ = crumbs[-1]
    crumb_html += f'<span class="breadcrumb-active">{last_title}</span>'

    return f'''<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
      {crumb_html}
    </nav>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-desc">{subtitle}</p>
  </div>
</section>'''

def get_demo_disclaimer(custom_text=""):
    text = custom_text or "This section and associated metrics represent an illustrative demonstration framework for professional human capital advisory. Specific client requirements, statutory compliance, and contractual scopes are established through tailored agreements."
    return f'''<div class="demo-banner">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" style="flex-shrink:0;">
    <circle cx="12" cy="12" r="10"></circle>
    <line x1="12" y1="8" x2="12" y2="12"></line>
    <line x1="12" y1="16" x2="12.01" y2="16"></line>
  </svg>
  <p><strong>Demonstration Notice:</strong> {text}</p>
</div>'''

def get_cta_section(title="Ready to Build a High-Performing Workforce?", desc="Let us evaluate your existing people management systems and identify practical opportunities for organizational improvement."):
    return f'''<section class="section section-bg-alt">
  <div class="container">
    <div class="cta-box text-center">
      <h2>{title}</h2>
      <p style="margin-left:auto;margin-right:auto;">{desc}</p>
      <div class="btn-group justify-center">
        <a href="book-consultation.html" class="btn btn-teal btn-lg">Book an HR Consultation</a>
        <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Team</a>
      </div>
    </div>
  </div>
</section>'''

def write_html_page(filename, title, meta_desc, content, active_nav=""):
    from build_site import wrap_page
    full_html = wrap_page(title, meta_desc, content, active_nav)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Written: {filename}")

def save_catalog():
    with open('image_catalog.json', 'w', encoding='utf-8') as f:
        json.dump(IMAGE_CATALOG, f, indent=2)
    print(f"Catalog saved with {len(IMAGE_CATALOG)} items.")

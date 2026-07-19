# make_samples.py
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def initialize_data_environment():
    """Ensures the target data directory exists before generation."""
    os.makedirs("data", exist_ok=True)
    print("📁 Target 'data/' directory verified.")

def make_pdf(filename: str, title: str, content: str):
    """Generates a standardized, structurally valid PDF asset."""
    file_path = os.path.join("data", filename)
    
    # Establish document layout framework
    doc = SimpleDocTemplate(
        file_path, 
        pagesize=letter,
        rightMargin=54, leftMargin=54,
        topMargin=54, bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    story = []
    
    # Append Title structure
    story.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    story.append(Spacer(1, 18))
    
    # Process text chunks into flowing paragraphs
    for line in content.split('\n'):
        if line.strip():
            story.append(Paragraph(line, styles['Normal']))
            story.append(Spacer(1, 10))
            
    try:
        doc.build(story)
        print(f"✅ Successfully compiled: {file_path}")
    except Exception as e:
        print(f"❌ Failed to build {filename}: {str(e)}")

if __name__ == "__main__":
    print("🚀 Initializing local PDF document generation engine...")
    initialize_data_environment()
    
    # 1. Compile medical_guidelines.pdf
    guidelines_text = (
        "Guideline Ref 402: Daily dosage of drug XYZ exceeding 50mg exhibits severe cardiotoxicity in phase II trials. "
        "Any exploratory protocols pushing bounds beyond this baseline threshold must include continuous telemetry monitoring.\n\n"
        "FDA Rule 2026: Clinical protocols involving mRNA tracking or sequencing platforms must include strict baseline biomarkers "
        "logged at Day 0 (pre-injection) and Day 14 (post-injection).\n\n"
        "Standard Protocol 88: All oncology interventions tracking advanced cellular toxicity profiles are required to log "
        "complete liver enzyme panels (AST/ALT) on a weekly schedule."
    )
    make_pdf("medical_guidelines.pdf", "Global Medical Guidelines & Protocol Standards", guidelines_text)

    # 2. Compile drug_safety.pdf
    safety_text = (
        "Lancet Study 2025: Combination therapy of Alpha-1 and Beta-2 inhibitors shows a 30% increase in patient adverse events "
        "compared to monotherapy regimes.\n\n"
        "Contraindication Notification: Co-administration of high-concentration Beta-2 inhibitors with common second-generation "
        "antihistamines creates an elevated risk of acute respiratory distress in patients with underlying asthma conditions."
    )
    make_pdf("drug_safety.pdf", "Pharmaceutical Drug Safety & Interactions Index", safety_text)

    # 3. Compile clinical_trial.pdf
    trial_text = (
        "Standard Core Methodology: Phase II exploratory cohorts require a rigorous double-blind framework. Control groups "
        "must receive an identical placebo delivery mechanism.\n\n"
        "Regulatory Mandated Review Clause: Any clinical trial outline or protocol abstract submitted to the review matrix "
        "without an explicit patient safety monitoring clause or independent audit trail will be automatically flagged for administrative review."
    )
    make_pdf("clinical_trial.pdf", "Clinical Trial Framework & Baseline Blueprint Templates", trial_text)
    
    print("\n🎉 All reference PDFs are written and ready for vector database synchronization.")
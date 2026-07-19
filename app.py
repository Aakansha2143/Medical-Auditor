import os
import sys
import warnings

# ==========================================
# 1. STRICT ENVIRONMENT SUPPRESSION
# ==========================================
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["GROQ_API_KEY"] = "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"

warnings.filterwarnings("ignore", category=UserWarning)
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

# ==========================================
# 2. SYSTEM IMPORTS
# ==========================================
import streamlit as st
from utils.vector_db import get_vector_db
from utils.llm import get_llm
from agents.graph import create_compliance_graph

# ==========================================
# 3. STREAMLIT APPLICATION STATE INITIALIZATION
# ==========================================
st.set_page_config(
    page_title="Multi-Agent Medical Compliance Engine",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Multi-Agent Medical Literature Review & Compliance Engine")
st.subheader("Enterprise Protocol Graph Auditing Framework")

# Initialize shared components
db = get_vector_db()
llm = get_llm()
graph_app = create_compliance_graph(llm)

# ==========================================
# 4. USER INTERFACE ARCHITECTURE
# ==========================================
# ==========================================
# 4. USER INTERFACE ARCHITECTURE
# ==========================================
st.markdown("### 📥 Document Ingestion Interface")
tab1, tab2 = st.tabs(["📄 Direct PDF Upload Profile", "✍️ Raw Text Extraction Input"])

user_input = ""

with tab1:
    uploaded_file = st.file_uploader("Upload target trial protocol document (PDF format)", type=["pdf"])
    if uploaded_file is not None:
        try:
            import pypdf
            pdf_reader = pypdf.PdfReader(uploaded_file)
            extracted_text = []
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text.append(text)
            user_input = "\n".join(extracted_text)
            if user_input.strip():
                st.success(f"Extracted {len(pdf_reader.pages)} pages from {uploaded_file.name}")
        except Exception as e:
            st.error(f"Failed to parse document pipeline: {str(e)}")

with tab2:
    pasted_text = st.text_area(
        label="Input Trial Core Specification Rules:",
        placeholder="Example: Protocol 402 dosage index profile execution guidelines...",
        height=200
    )
    if pasted_text.strip():
        user_input = pasted_text

# ==========================================
# 5. MULTI-AGENT GRAPH EXECUTION ENGINE
# ==========================================
if st.button("Execute Multi-Agent Protocol Audit", type="primary"):
    if not user_input.strip():
        st.warning("Please supply an input protocol structure using either file submission or text inputs.")
    else:
        # 1. Fetch relevant vector database literature fragments
        retriever = db.as_retriever(search_kwargs={"k": 3})
        relevant_docs = retriever.invoke(user_input)
        context_text = "\n\n".join([doc.page_content for doc in relevant_docs])
        
        # 2. Build UI containers to show active graph node loops in real-time
        st.markdown("---")
        st.markdown("### ⚙️ Live Agent Graph Execution Pipeline")
        
        status_box = st.empty()
        
        # Initialize graph state input dict
        initial_state = {
            "protocol": user_input,
            "context": context_text if context_text.strip() else "No matching guidelines found.",
            "audit_findings": "",
            "safety_critique": "",
            "final_report": "",
            "critical_flag": False
        }
        
        try:
            # 3. Run execution iterations across nodes
            status_box.info("🤖 Task assigned: Activating Regulatory Auditor Agent...")
            final_output = graph_app.invoke(initial_state)
            
            status_box.info("🔬 Compliance checking finished. Swapping to Safety Critic validation loop...")
            
            # 4. Render conditional metrics and indicators based on internal agent state
            if final_output.get("critical_flag", False):
                st.error("🚨 CRITICAL HAZARD ALERT DETECTED BY SAFETY CRITIC NODE")
            else:
                st.success("🛡️ Safety parameters validated by supervisor graph modules.")
                
            status_box.empty()
            
            # 5. Output compiled report findings
            st.markdown("### 📋 Automated Executive Audit Findings Report")
            st.markdown(final_output["final_report"])
            
            with st.expander("🛠️ View Raw Multi-Agent Workgroup Logs"):
                st.markdown("**1. Regulatory Auditor Assessment:**")
                st.info(final_output["audit_findings"])
                st.markdown("**2. Safety Critic Evaluation Summary:**")
                st.warning(final_output["safety_critique"])
                
        except Exception as e:
            status_box.empty()
            st.error(f"Multi-agent graph runtime failed during processing loop: {str(e)}")
import streamlit as st
from components.header import show_header
from utils.data import roadmap
from utils.config import PRIVATE_KEY

show_header()

# If not unlocked, ask for key and stop
if not st.session_state.get("unlocked"):
    entered = st.text_input("Enter passkey to view this page", type="password")
    if entered == PRIVATE_KEY:
        st.session_state["unlocked"] = True
        st.rerun()
    else:
        st.error("🔒 You must unlock first on Private Access page.")
        st.stop()
        
# Private deep‑strategy content
st.header("🔐 Private Deep‑Strategy Playbook")

st.subheader("1. Two‑Year Gantt Chart")
st.markdown("""
| Element → Quarter ↓ | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 | Q1 2027 | Q2 2027 |
|---------------------|---------|---------|---------|---------|---------|---------|---------|---------|
| **H – Hydrogen**    | Pilot curriculum build<br>Mobile‑app MVP | Rural rollout (3 prov.)<br>Offline mode dev | Scale to 5 prov.<br>Local partnerships | UX refinement<br>Monitoring & eval | National expansion plan | Sustainability model | H→C integration | Continuous improvement |
| **C – Carbon**      | Platform redesign<br>Vendor onboarding | First cohort launch<br>Micro‑loan pilot | Scale‑up marketplace | Mobile‑money integration | New sectors expansion | B2B partnerships | Revenue‑share test | Full ops |
| **O – Oxygen**      | ML model dev | Clinical pilot (200 users) | Tele‑consult integration | Health‑worker training | Scale to 5 clinics | Analytics & reporting | Maternal‑health module | Regional expansion |
| **Fe – Iron**       | Energy prototype | Govt pilot (smart grids) | Scale infra tools | Resource API | City expansion | Integrate with Carbon | KPI automation | Cross‑element bundle |
| **Au – Gold**       | Recruit mentors | Cohort #1 | Demo day & seed fund | Alumni network | Sponsorships | Cohort #2 | Investor roadshow | Franchise design |
| **Si – Silicon**    | Tech‑hub design | Bootcamp #1 | Placement deals | Hub #2 setup | Bootcamp #2 | Hub #3 plan | Hiring pipeline | Silicon‑as‑SaaS |
| **U – Uranium**     | Accelerator design | Cohort #1 | Seed deploy | Demo day | Cohort #2 | Scale ops | Spin‑outs | Exit & reinvest |
""", unsafe_allow_html=True)

st.subheader("2. Risk Register & Mitigation")
st.markdown("""
| Risk Category      | Risk                                               | Likelihood | Impact | Mitigation                                           |
|--------------------|----------------------------------------------------|------------|--------|------------------------------------------------------|
| Connectivity       | Rural areas lack reliable internet                 | High       | High   | Offline‑first; partner with local telcos             |
| Funding            | Seed funding delays                                | Medium     | High   | Bridge loans; early revenue pilots                   |
| Regulatory         | Telemedicine licensing                             | Medium     | Medium | MoU with Health Ministry                             |
| Adoption           | Low pilot engagement                               | Medium     | Medium | Incentives; local champions                          |
| Technical          | API scaling under load                             | Low        | High   | Auto‑scaling infra; caching                          |
| Talent            | Hiring qualified mentors                           | Medium     | Medium | University partnerships                              |
| Security & Privacy | Data breaches                                      | Low        | High   | Encryption; compliance audits                        |
| Cultural           | “Element” theme too academic                       | Low        | Low    | Local language overlays; focus‑group testing         |
""", unsafe_allow_html=True)

st.subheader("3. High‑Level Financial Model (Y1 & Y2)")
st.markdown("""
| Element  | Revenue Streams                   | Y1 Rev  | Y2 Rev   | Y1 Cost  | Y2 Cost  | EBITDA Y2 |
|----------|-----------------------------------|--------:|---------:|---------:|---------:|----------:|
| Hydrogen | Subscriptions, grants             | $12,000 | $48,000  | $20,000  | $25,000  | $23,000   |
| Carbon   | Transaction fees, micro‑loan int. | $8,000  | $40,000  | $15,000  | $20,000  | $20,000   |
| Oxygen   | Consult fees, data services       | $5,000  | $30,000  | $18,000  | $22,000  | $8,000    |
| Iron     | Licensing, subscriptions          | $0      | $20,000  | $25,000  | $30,000  | -$10,000  |
| Gold     | Program fees, sponsorships        | $10,000 | $50,000  | $15,000  | $20,000  | $30,000   |
| Silicon  | Bootcamp tuition, contracts       | $6,000  | $36,000  | $12,000  | $18,000  | $6,000    |
| Uranium  | Equity stakes, accelerator fees   | $0      | $60,000  | $10,000  | $15,000  | $45,000   |
| **Total**|                                   |**$41k** |**$284k** |**$115k** |**$150k** |**$112k** |
""", unsafe_allow_html=True)

st.subheader("4. Key Partnerships & MoU Outlines")
st.markdown("""
| Partner Type   | Organization         | Purpose                             | Status          |
|----------------|----------------------|-------------------------------------|-----------------|
| Telco          | MTN DRC / Airtel     | Connectivity hotspots               | MoU drafted     |
| University     | AUCA, UNikin         | Instructor pipeline, research       | Negotiating     |
| Health Ministry| DRC Ministry of Health| Telemedicine authorization          | MoU signed      |
| NGOs           | UNICEF, WHO          | Grants for education & health       | Proposal sent   |
| Investors      | TLcom, EchoVC        | Seed & Series A funding             | Intro meetings  |
| Local Govt     | Kinshasa Province    | Infrastructure pilot (Iron)         | Pilot agreement |
""", unsafe_allow_html=True)

st.subheader("5. Sample MoU: Telco Partnership")
st.markdown("""
1. **Parties**: Kiregha Corp & MTN DRC  
2. **Scope**: 4G hotspots in 5 rural schools; zero‑rated data for Hydrogen app  
3. **Duration**: 24 months, renewable  
4. **KPIs**: 80% uptime; 300 active learners/month; joint branding  
5. **Financials**: MTN funds hardware; Kiregha pays $500/mo operational fee  
6. **Termination**: 60‑day notice; data migration support  
""", unsafe_allow_html=True)
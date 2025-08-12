import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# -----------------------
# APP TITLE
# -----------------------
st.set_page_config(page_title="Cloud Architecture Skills Portfolio", layout="wide")
st.title("☁️ Cloud Architecture Skills Portfolio")
st.markdown("### Showcase of GCP & AWS Architect Skills using Free, Open Source, and Serverless Design")

st.write("""
This app demonstrates **Cloud Architecture Design** concepts without requiring paid services.
It uses interactive diagrams to show how different architectures work in a **real enterprise setup**.
""")

# -----------------------
# DEFINE ARCHITECTURE NODES
# -----------------------
nodes = [
    Node(id="User", label="User", size=30, color="#4CAF50"),
    Node(id="API Gateway", label="API Gateway", size=30, color="#2196F3"),
    Node(id="Microservice 1", label="Microservice 1", size=25, color="#FF9800"),
    Node(id="Microservice 2", label="Microservice 2", size=25, color="#FF9800"),
    Node(id="Database", label="Database (SQL/NoSQL)", size=30, color="#9C27B0"),
    Node(id="Serverless Function", label="Serverless Function", size=25, color="#E91E63"),
    Node(id="Cloud Storage", label="Cloud Storage", size=25, color="#00BCD4"),
    Node(id="Zero Trust Security", label="Zero Trust Security Layer", size=25, color="#F44336")
]

# -----------------------
# DEFINE ARCHITECTURE EDGES
# -----------------------
edges = [
    Edge(source="User", target="API Gateway"),
    Edge(source="API Gateway", target="Microservice 1"),
    Edge(source="API Gateway", target="Microservice 2"),
    Edge(source="Microservice 1", target="Database"),
    Edge(source="Microservice 2", target="Serverless Function"),
    Edge(source="Serverless Function", target="Cloud Storage"),
    Edge(source="User", target="Zero Trust Security"),
    Edge(source="Zero Trust Security", target="API Gateway")
]

# -----------------------
# DIAGRAM CONFIG
# -----------------------
config = Config(width=900, height=500, directed=True, nodeHighlightBehavior=True,
                highlightColor="#F7A7A6", collapsible=True)

# -----------------------
# DISPLAY ARCHITECTURE DIAGRAM
# -----------------------
st.subheader("Interactive Cloud Architecture Diagram")
agraph(nodes=nodes, edges=edges, config=config)

# -----------------------
# EXPLANATION SECTION
# -----------------------
st.subheader("💡 Explanation of Architectures")
st.markdown("""
**1. Data Architecture** — Data flows from users via APIs, stored in SQL/NoSQL DB, processed by microservices.  
**2. Database Architecture** — Can support transactional + analytics workloads.  
**3. Zero Trust Security** — Every request is authenticated, even inside the network.  
**4. Serverless Architecture** — Auto-scales, cost-efficient, and event-driven.  
**5. API Architecture** — Uses API Gateway for routing, throttling, and security.  
**6. Microservices Architecture** — Small, independent services for scalability.  
**7. Cloud-Native Architecture** — Fully containerized, portable, and CI/CD ready.
""")

# -----------------------
# HOW TO USE (LAYMAN FRIENDLY)
# -----------------------
st.markdown("---")
st.markdown("## 📘 How to Use This Tool (Simple Steps for Everyone)")
instructions = [
    "1️⃣ Open this page — no login needed.",
    "2️⃣ Look at the diagram above. Each **circle** is a cloud service.",
    "3️⃣ **Green** = end users, **Blue** = networking/API, **Orange** = processing, **Purple** = database, **Cyan** = storage, **Red** = security.",
    "4️⃣ Click and drag nodes to rearrange and understand flow.",
    "5️⃣ See how **Zero Trust** protects every connection.",
    "6️⃣ This is a simulation — no real servers are running, so it's 100% free.",
    "7️⃣ You can imagine replacing each block with actual GCP or AWS services.",
    "8️⃣ This diagram is useful for explaining cloud architecture to **non-technical people**."
]

for step in instructions:
    st.markdown(f"<span style='color:#2E86C1; font-size:18px;'>{step}</span>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("**✅ All components shown here can be built using Free-tier cloud services and open-source tools.**")

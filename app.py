"""
Streamlit Web Interface for AI Research Agents
"""
import streamlit as st
import asyncio
import json
from src.agent_manager import AgentManager
from src.utils import format_report

# Initialize session state
if 'agent_manager' not in st.session_state:
    st.session_state.agent_manager = AgentManager()

if 'research_results' not in st.session_state:
    st.session_state.research_results = None

# Page config
st.set_page_config(
    page_title="AI Research Agents",
    page_icon="🔍",
    layout="wide"
)

# Title
st.title("🔍 AI Research Agents")
st.markdown("""
This multi-agent system conducts deep research on any topic, analyzes findings, 
verifies facts, and generates comprehensive reports.
""")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Agent status
    st.subheader("Agent Status")
    agent_status = st.session_state.agent_manager.get_agent_status()
    for agent, status in agent_status.items():
        st.markdown(f"**{agent.capitalize()}**: {status}")

# Main interface
st.header("📚 Research Topic")

# Research input
research_topic = st.text_input("Enter a research topic:", 
                              placeholder="e.g., Impact of AI on healthcare")

# Research button
if st.button("Conduct Research", type="primary") and research_topic:
    with st.spinner("Research agents are working... This may take a few minutes."):
        try:
            # Run research
            research_results = asyncio.run(
                st.session_state.agent_manager.conduct_research(research_topic)
            )
            
            # Store results
            st.session_state.research_results = research_results
            
            st.success("Research completed successfully!")
        except Exception as e:
            st.error(f"Error conducting research: {str(e)}")

# Display results
if st.session_state.research_results:
    results = st.session_state.research_results
    
    # Summary metrics
    st.header("📊 Research Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Sources", results['analysis']['metrics']['source_count'])
    
    with col2:
        st.metric("Key Points", results['analysis']['metrics']['key_point_count'])
    
    with col3:
        st.metric("Quality Score", f"{results['analysis']['metrics']['quality_score']:.2f}")
    
    with col4:
        st.metric("Fact Check", f"{results['fact_check']['fact_score']:.2f}")
    
    # Key findings
    st.header("🔍 Key Findings")
    key_points = results['research_data']['key_points']
    for i, point in enumerate(key_points, 1):
        st.markdown(f"{i}. {point}")
    
    # Detailed report
    st.header("📖 Detailed Report")
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "Executive Summary", "Full Report", "Fact Check", "Sources"
    ])
    
    with tab1:
        st.markdown(results['report']['executive_summary'])
    
    with tab2:
        # Display full formatted report
        formatted_report = format_report(results['report'])
        st.markdown(formatted_report)
        
        # Download button
        st.download_button(
            label="Download Full Report (JSON)",
            data=json.dumps(results, indent=2),
            file_name=f"{research_topic.replace(' ', '_')}_report.json",
            mime="application/json"
        )
        
        st.download_button(
            label="Download Full Report (TXT)",
            data=formatted_report,
            file_name=f"{research_topic.replace(' ', '_')}_report.txt",
            mime="text/plain"
        )
    
    with tab3:
        st.markdown(results['report']['fact_check_results'])
        
        # Fact check details
        st.subheader("Verified Claims")
        for claim in results['fact_check']['verified_claims']:
            if claim['verified']:
                st.markdown(f"**Claim**: {claim['claim']}")
                st.markdown(f"*Confidence*: {claim['confidence']:.2f}")
                st.markdown(f"*Evidence*: {claim['evidence']}")
                st.markdown("---")
    
    with tab4:
        st.subheader("Research Sources")
        sources = results['report']['references']
        for i, source in enumerate(sources, 1):
            st.markdown(f"**{i}. [{source['title']}]({source['url']})**")
            st.markdown(f"> {source.get('description', 'No description available')}")
            st.markdown("---")

# Information section
st.markdown("---")
st.markdown("""
### 🤖 About AI Research Agents

This system uses multiple specialized AI agents to conduct comprehensive research:

1. **Researcher Agent**: Gathers information from diverse sources
2. **Analyzer Agent**: Processes and analyzes collected data
3. **Fact Checker Agent**: Verifies the accuracy of findings
4. **Writer Agent**: Synthesizes results into comprehensive reports

### 🚀 Features
- Multi-agent coordination for parallel processing
- Automated fact checking and verification
- Comprehensive report generation
- Web-based interface for easy interaction
- Exportable research results in multiple formats
""")
# 14 AI Agents for Deep Research

## Overview

This project implements a multi-agent system for deep research that can perform comprehensive analysis tasks, coordinate between specialized agents, and generate detailed research reports with fact-checking and source verification.

## Dataset

- **Primary**: FEVER Dataset - https://fever.ai/
- **Secondary**: Fact Verification Datasets
- **Research Sources**: Academic papers, news articles, Wikipedia
- **Size**: Variable based on research topics

## Novel Approach

Our implementation includes:
1. Multi-agent framework with specialized roles (Researcher, Analyzer, Fact-Checker, Writer)
2. Task decomposition and coordination between agents
3. Web scraping and information gathering capabilities
4. Cross-reference verification and fact-checking
5. Automated report generation with citations
6. Research planning and execution management
7. Quality assessment and confidence scoring

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

To run a specific research task:
```bash
python main.py --task "impact of climate change on agriculture"
```

To run the web interface:
```bash
streamlit run app.py
```

## Project Structure

```
14-ai-research-agents/
├── main.py                 # Main entry point
├── app.py                  # Streamlit web interface
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── src/
    ├── agent_manager.py    # Agent coordination and management
    ├── researcher_agent.py # Information gathering agent
    ├── analyzer_agent.py   # Data analysis agent
    ├── fact_checker_agent.py  # Fact verification agent
    ├── writer_agent.py     # Report generation agent
    ├── scraper.py          # Web scraping utilities
    └── utils.py            # Utility functions
```

## Results

The AI research agents can perform complex research tasks with high accuracy, providing comprehensive reports with proper citations and fact verification. The multi-agent approach allows for parallel processing and specialized expertise in different areas.
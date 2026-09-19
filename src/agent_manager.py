"""
Agent Manager for AI Research Agents
"""
from typing import Dict, Any, List
import asyncio
from .researcher_agent import ResearcherAgent
from .analyzer_agent import AnalyzerAgent
from .fact_checker_agent import FactCheckerAgent
from .writer_agent import WriterAgent

class AgentManager:
    def __init__(self):
        """Initialize agent manager with all specialized agents"""
        self.researcher = ResearcherAgent()
        self.analyzer = AnalyzerAgent()
        self.fact_checker = FactCheckerAgent()
        self.writer = WriterAgent()
    
    async def conduct_research(self, research_topic: str) -> Dict[str, Any]:
        """
        Conduct comprehensive research on a topic using multiple agents
        
        Parameters:
        research_topic (str): Topic to research
        
        Returns:
        dict: Research results with analysis and report
        """
        print(f"Starting research on: {research_topic}")
        
        # Step 1: Researcher agent gathers information
        print("Step 1: Gathering information...")
        research_data = await self.researcher.gather_information(research_topic)
        
        # Step 2: Analyzer agent processes data
        print("Step 2: Analyzing data...")
        analysis_results = await self.analyzer.analyze_data(research_data)
        
        # Step 3: Fact checker verifies information
        print("Step 3: Verifying facts...")
        fact_check_results = await self.fact_checker.verify_facts(analysis_results)
        
        # Step 4: Writer agent generates report
        print("Step 4: Generating report...")
        report = await self.writer.generate_report(
            research_topic, 
            research_data, 
            analysis_results, 
            fact_check_results
        )
        
        return {
            "topic": research_topic,
            "research_data": research_data,
            "analysis": analysis_results,
            "fact_check": fact_check_results,
            "report": report
        }
    
    def get_agent_status(self) -> Dict[str, str]:
        """
        Get status of all agents
        
        Returns:
        dict: Status of each agent
        """
        return {
            "researcher": "active",
            "analyzer": "active",
            "fact_checker": "active",
            "writer": "active"
        }
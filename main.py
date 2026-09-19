"""Main script for 14-ai-research-agents"""

import argparse
import asyncio
import json
from src.agent_manager import AgentManager
from src.utils import format_report, save_json

async def main():
    parser = argparse.ArgumentParser(description="AI Agents for Deep Research")
    parser.add_argument("--task", type=str, help="Research task/topic")
    parser.add_argument("--output", type=str, default="research_report.json", 
                       help="Output file for research report")
    
    args = parser.parse_args()
    
    # Initialize agent manager
    agent_manager = AgentManager()
    
    if args.task:
        # Conduct research on specified task
        print(f"Starting research on: {args.task}")
        
        # Run research
        research_results = await agent_manager.conduct_research(args.task)
        
        # Save results
        save_json(research_results, args.output)
        print(f"Research report saved to {args.output}")
        
        # Also save as formatted text
        formatted_report = format_report(research_results["report"])
        txt_output = args.output.replace(".json", ".txt")
        with open(txt_output, "w", encoding="utf-8") as f:
            f.write(formatted_report)
        print(f"Formatted report saved to {txt_output}")
        
        # Print summary
        print("\nResearch Summary:")
        print(f"Topic: {research_results['topic']}")
        print(f"Sources analyzed: {research_results['analysis']['metrics']['source_count']}")
        print(f"Fact check score: {research_results['fact_check']['fact_score']:.2f}")
        
    else:
        # Interactive mode
        print("AI Research Agents - Interactive Mode")
        print("Enter a research topic or 'quit' to exit")
        
        while True:
            topic = input("\nResearch topic: ").strip()
            
            if topic.lower() in ['quit', 'exit', '']:
                print("Goodbye!")
                break
            
            if not topic:
                continue
            
            # Conduct research
            print(f"\nResearching: {topic}")
            research_results = await agent_manager.conduct_research(topic)
            
            # Display summary
            print("\n" + "="*50)
            print("RESEARCH SUMMARY")
            print("="*50)
            print(f"Topic: {research_results['topic']}")
            print(f"Sources: {research_results['analysis']['metrics']['source_count']}")
            print(f"Key Points: {research_results['analysis']['metrics']['key_point_count']}")
            print(f"Quality Score: {research_results['analysis']['metrics']['quality_score']:.2f}")
            print(f"Fact Check Score: {research_results['fact_check']['fact_score']:.2f}")
            
            # Show key findings
            print("\nKey Findings:")
            for i, point in enumerate(research_results['research_data']['key_points'][:3], 1):
                print(f"  {i}. {point}")
            
            # Save option
            save_option = input("\nSave detailed report? (y/n): ").strip().lower()
            if save_option == 'y':
                filename = f"{topic.replace(' ', '_')}_report.json"
                save_json(research_results, filename)
                print(f"Report saved to {filename}")

if __name__ == "__main__":
    asyncio.run(main())
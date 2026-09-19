"""
Utility Functions for AI Research Agents
"""
from typing import Dict, Any, List
import json
import os

def save_json(data: Any, filepath: str) -> None:
    """
    Save data to JSON file
    
    Parameters:
    data (any): Data to save
    filepath (str): Path to save file
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(filepath: str) -> Any:
    """
    Load data from JSON file
    
    Parameters:
    filepath (str): Path to load file
    
    Returns:
    any: Loaded data
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def format_report(report: Dict[str, Any]) -> str:
    """
    Format research report as string
    
    Parameters:
    report (dict): Research report
    
    Returns:
    str: Formatted report
    """
    formatted = f"# {report.get('title', 'Research Report')}\n\n"
    
    sections = [
        ("Executive Summary", report.get("executive_summary", "")),
        ("Introduction", report.get("introduction", "")),
        ("Methodology", report.get("methodology", "")),
        ("Findings", report.get("findings", "")),
        ("Analysis", report.get("analysis", "")),
        ("Fact Check Results", report.get("fact_check_results", "")),
        ("Conclusions", report.get("conclusions", "")),
        ("Recommendations", report.get("recommendations", ""))
    ]
    
    for section_title, section_content in sections:
        if section_content:
            formatted += f"\n## {section_title}\n\n{section_content}\n"
    
    # Add references
    references = report.get("references", [])
    if references:
        formatted += "\n## References\n\n"
        for i, ref in enumerate(references, 1):
            formatted += f"{i}. [{ref.get('title', 'Source')}]({ref.get('url', '#')})\n"
            if ref.get('description'):
                formatted += f"   {ref.get('description')}\n"
    
    return formatted

def calculate_confidence_score(analysis_results: Dict[str, Any], 
                             fact_check_results: Dict[str, Any]) -> float:
    """
    Calculate overall confidence score for research
    
    Parameters:
    analysis_results (dict): Analysis results
    fact_check_results (dict): Fact check results
    
    Returns:
    float: Confidence score between 0 and 1
    """
    # Extract relevant scores
    quality_score = analysis_results.get("metrics", {}).get("quality_score", 0)
    fact_score = fact_check_results.get("fact_score", 0)
    
    # Weighted average (70% quality, 30% fact checking)
    confidence = 0.7 * quality_score + 0.3 * fact_score
    return confidence

def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
    """
    Extract keywords from text
    
    Parameters:
    text (str): Text to extract keywords from
    max_keywords (int): Maximum number of keywords
    
    Returns:
    list: Extracted keywords
    """
    # Simple keyword extraction (in practice, use NLP libraries)
    words = text.lower().split()
    # Remove common stop words
    stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by"}
    keywords = [word for word in words if word not in stop_words and len(word) > 3]
    
    # Return unique keywords
    return list(set(keywords))[:max_keywords]
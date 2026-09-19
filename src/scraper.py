"""
Web Scraper Utility for AI Research Agents
"""
from typing import Dict, Any, List
import requests
from bs4 import BeautifulSoup
import asyncio
import time

class WebScraper:
    def __init__(self, delay: float = 1.0):
        """
        Initialize web scraper
        
        Parameters:
        delay (float): Delay between requests in seconds
        """
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
    
    async def scrape_url(self, url: str) -> Dict[str, Any]:
        """
        Scrape content from a URL
        
        Parameters:
        url (str): URL to scrape
        
        Returns:
        dict: Scraped content
        """
        try:
            # Add delay to be respectful to servers
            await asyncio.sleep(self.delay)
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "No title"
            
            # Extract main content (simplified)
            # Try common content selectors
            content_selectors = ['article', '.content', '.post', 'main', 'p']
            content = ""
            
            for selector in content_selectors:
                elements = soup.select(selector)
                if elements:
                    content = ' '.join([elem.get_text().strip() for elem in elements])
                    break
            
            # If no content found, get all paragraphs
            if not content:
                paragraphs = soup.find_all('p')
                content = ' '.join([p.get_text().strip() for p in paragraphs])
            
            # Limit content length
            content = content[:2000] + "..." if len(content) > 2000 else content
            
            return {
                "url": url,
                "title": title_text,
                "content": content,
                "status": "success"
            }
        except Exception as e:
            return {
                "url": url,
                "error": str(e),
                "status": "error"
            }
    
    async def scrape_multiple_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Scrape content from multiple URLs concurrently
        
        Parameters:
        urls (list): List of URLs to scrape
        
        Returns:
        list: Scraped content from all URLs
        """
        tasks = [self.scrape_url(url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

class SearchEngine:
    def __init__(self):
        """Initialize search engine interface"""
        pass
    
    async def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Search for results based on a query
        
        Parameters:
        query (str): Search query
        max_results (int): Maximum number of results
        
        Returns:
        list: Search results
        """
        # This is a simplified example
        # In practice, this would connect to real search APIs
        sample_results = [
            {
                "title": f"Introduction to {query}",
                "url": f"https://example.com/{query.replace(' ', '-')}-intro",
                "description": f"A comprehensive introduction to {query} and its applications."
            },
            {
                "title": f"Latest research on {query}",
                "url": f"https://example.com/{query.replace(' ', '-')}-research",
                "description": f"Recent findings and developments in {query} research."
            },
            {
                "title": f"{query} applications",
                "url": f"https://example.com/{query.replace(' ', '-')}-applications",
                "description": f"Practical applications and use cases of {query}."
            }
        ]
        
        return sample_results[:max_results]
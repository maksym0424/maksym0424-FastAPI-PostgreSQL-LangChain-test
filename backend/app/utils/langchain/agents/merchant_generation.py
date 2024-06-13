from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_tool_calling_agent, AgentExecutor
from .basc_agent import BasicAgent
from app.utils.logging import AppLogger

logger = AppLogger().get_logger()

class MerchantGenerationAgent(BasicAgent):
    
    def __init__(self):
        super().__init__()
        
        self.tools = [TavilySearchResults()]
        self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, return_intermediate_steps=True)
        
    async def generate(self, deal: dict):
        result = await self.agent_executor.ainvoke(
            {"input": f"Generate brief description about `{deal['merchant_name']}` including what it sells. Homepage url is {deal['homepage_url']}"}
        )
        return result
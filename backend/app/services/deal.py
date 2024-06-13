

from app.models.deal import Deal
from app.config import settings
from app.utils.logging import AppLogger
from app.utils.langchain.agents.merchant_generation import MerchantGenerationAgent
import app.constants as constants

logger = AppLogger().get_logger()

class DealService:
    
    def __init__(self, db_session):
        self.db_session = db_session
    
    async def generate_merchant_info(self, deal: Deal) -> dict:
        """
        Generate Merchant Information with Tavily LangChain Tool
        """
        logger.info(f"generating merchant information for {deal.merchant_name}")
        
        agent = MerchantGenerationAgent()
        result = await agent.generate(deal.__dict__)
        evaluation_result = await agent.evaluate_trajectory(result)
        
        return {
            "output": result['output'],
            "evaluation_result": evaluation_result
        }
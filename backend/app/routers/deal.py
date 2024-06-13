import asyncio
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.deal import Deal
from app.schemas.deal import GenerateMerchantInfoRequestSchema
from app.services.deal import DealService
from app.database import get_db
from app.exceptions.http_exceptions import *

router = APIRouter(prefix="/deal")

@router.get("/{merchant_id}")
async def get_deal(merchant_id: int, db_session: AsyncSession = Depends(get_db)):
    """
    Return merchant_about for a given merchant id.
    """
    deal_model = await Deal.find_by_merchant_id(merchant_id=merchant_id, db_session=db_session)
    if not deal_model:
        raise NotFoundHTTPException("Merchant not found")
    return deal_model.merchant_about

@router.post("/generate-merchant-info")
async def generate_merchant_info(model: GenerateMerchantInfoRequestSchema, db_session: AsyncSession = Depends(get_db)):
    """
    Generate merchant information with Tavily LangChain Tool for a given merchant.
    It generates information, and update merchant_about field as response.
    
    Args:
    
        merchant_name (str): name of merchant to generate description for
        
    Response:
    
        merchant information str
    """
    deal_model = await Deal.find_by_merchant_name(db_session, merchant_name=model.merchant_name)    
    if not deal_model:
        raise NotFoundHTTPException("Merchant not found")
    
    deal_service = DealService(db_session=db_session)
    info_result = await deal_service.generate_merchant_info(deal_model)
    
    await deal_model.update(db_session, merchant_about=info_result['output'])
    
    return info_result
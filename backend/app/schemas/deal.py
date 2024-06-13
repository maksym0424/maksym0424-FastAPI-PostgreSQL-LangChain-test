from pydantic import BaseModel

class GenerateMerchantInfoRequestSchema(BaseModel):
    merchant_name: str
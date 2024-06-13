from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.evaluation import load_evaluator
import app.constants as constants

class BasicAgent:

    def __init__(self):
        self.llm = ChatOpenAI(model=constants.OPENAI_MODEL_NAME, temperature=0)        
        self.prompt = hub.pull("hwchase17/openai-functions-agent")
        self.evaluator = load_evaluator("trajectory", llm=self.llm)
        
    async def evaluate_trajectory(self, result):
        evaluation_result = self.evaluator.evaluate_agent_trajectory(
            prediction=result["output"],
            input=result["input"],
            agent_trajectory=result["intermediate_steps"],
        )
        
        return evaluation_result
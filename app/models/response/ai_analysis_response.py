from pydantic import BaseModel


class AIAnalysisResponse(BaseModel):

    rootCause: str

    solution: str

    confidence: float
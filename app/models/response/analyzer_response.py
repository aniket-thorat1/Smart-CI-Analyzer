from pydantic import BaseModel

class AnalysisResultResponse(BaseModel):

    stepName: str

    rootCause: str

    solution: str

    source: str

    confidence: float


class AnalyzeResponse(BaseModel):

    pipelineId: str

    results: list[AnalysisResultResponse]
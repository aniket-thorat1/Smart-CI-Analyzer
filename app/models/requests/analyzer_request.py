from pydantic import BaseModel
from pydantic import Field

class FailedStepRequest(BaseModel):

    stepName: str = Field(
        min_length=1
    )

    logs: list[str]


class AnalyzeRequest(BaseModel):

    pipelineId: str = Field(
        min_length=1
    )

    failedSteps: list[FailedStepRequest]
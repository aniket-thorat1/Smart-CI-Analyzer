from app.models.response.analyzer_response import (
    AnalysisResultResponse,
    AnalyzeResponse
)
from app.services.rule_engine import RuleEngine

class AnalyzerService:

    @staticmethod
    def analyze(request):

        results = []

        for step in request.failedSteps:

            logs = "\n".join(
                step.logs
            )

            match = RuleEngine.find_match(
                logs
            )

            if match["matched"]:

                results.append(
                    AnalysisResultResponse(
                        stepName=step.stepName,
                        rootCause=match["rootCause"],
                        solution=match["solution"],
                        source="RULE_ENGINE"
                    )
                )

        return AnalyzeResponse(
            pipelineId=request.pipelineId,
            results=results
        )
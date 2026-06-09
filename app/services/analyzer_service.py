from app.models.response.analyzer_response import (
    AnalysisResultResponse,
    AnalyzeResponse
)
from app.services.rule_engine import RuleEngine
from app.services.history_service import HistoryService
from app.services.ai_service import AIService
from app.repositories.failure_repository import (
    FailureRepository
)

class AnalyzerService:

    @staticmethod
    def analyze(request):

        results = []

        history_service = HistoryService()
        ai_service = AIService()
        failure_repository = FailureRepository()

        for step in request.failedSteps:

            logs = "\n".join(step.logs)

            # Phase 1 - Rule Engine
            match = RuleEngine.find_match(logs)

            if match["matched"]:

                results.append(
                    AnalysisResultResponse(
                        stepName=step.stepName,
                        rootCause=match["rootCause"],
                        solution=match["solution"],
                        source="RULE_ENGINE",
                        confidence = 0
                    )
                )

                continue

            # Phase 2 - History Search
            history_match = history_service.find_match(logs)

            if history_match["matched"]:

                results.append(
                    AnalysisResultResponse(
                        stepName=step.stepName,
                        rootCause=history_match["rootCause"],
                        solution=history_match["solution"],
                        source="HISTORY",
                        confidence=history_match["confidence"]
                    )
                )

                continue
            
            ai_result = (
                ai_service.analyze_failure(
                    step.stepName,
                    logs
                )
            )
            failure_repository.save(
                signature= logs,
                root_cause=ai_result.rootCause,
                solution=ai_result.solution
            )
            results.append(
                AnalysisResultResponse(
                    stepName=step.stepName,
                    rootCause=ai_result.rootCause,
                    solution=ai_result.solution,
                    source="AI",
                    confidence=ai_result.confidence
                )
            )

        return AnalyzeResponse(
            pipelineId=request.pipelineId,
            results=results
        )
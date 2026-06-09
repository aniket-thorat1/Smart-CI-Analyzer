import os
import json

from openai import OpenAI

from app.models.response.ai_analysis_response import (
    AIAnalysisResponse
)


class AIService:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

        self.model = os.getenv(
            "OPENAI_MODEL",
            "gpt-5"
        )

    def analyze_failure(
        self,
        step_name,
        logs
    ):

        prompt = f"""
You are a Senior DevOps Engineer.

Analyze this pipeline failure.

Step:
{step_name}

Logs:
{logs}

Return ONLY valid JSON.

{{
  "rootCause": "",
  "solution": "",
  "confidence": 0
}}
"""

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        content = response.output_text

        data = json.loads(content)

        return AIAnalysisResponse(
            rootCause=data["rootCause"],
            solution=data["solution"],
            confidence=data["confidence"]
        )
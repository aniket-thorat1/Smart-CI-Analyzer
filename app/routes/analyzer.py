from flask import Blueprint
from flask import request
from flask import jsonify
from app.services.analyzer_service import AnalyzerService
from app.models.requests.analyzer_request import AnalyzeRequest
from pydantic import ValidationError

analyzer_bp = Blueprint(
    "analyzer",
    __name__
)

@analyzer_bp.route(
    "/api/v1/analyze",
    methods=["POST"]
)
def analyze():

    try:

        request_model = AnalyzeRequest(
            **request.get_json()
        )

        response_model = (
            AnalyzerService.analyze(
                request_model
            )
        )

        return jsonify(
            response_model.model_dump()
        )

    except ValidationError as ex:

        return jsonify({
            "message": "Validation Failed",
            "errors": ex.errors()
        }), 400
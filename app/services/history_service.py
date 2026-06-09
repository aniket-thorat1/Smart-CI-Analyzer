from difflib import SequenceMatcher

from app.repositories.failure_repository import (
    FailureRepository
)


class HistoryService:

    def __init__(self):

        self.repository = (
            FailureRepository()
        )

    def similarity(
        self,
        a,
        b
    ):

        return SequenceMatcher(
            None,
            a.lower(),
            b.lower()
        ).ratio()

    def find_match(
        self,
        logs
    ):

        records = (
            self.repository.get_all()
        )

        best_score = 0

        best_match = None

        for record in records:

            score = self.similarity(
                logs,
                record.signature
            )

            if score > best_score:

                best_score = score
                best_match = record

        if best_score > 0.80:

            return {
                "matched": True,
                "rootCause": best_match.root_cause,
                "solution": best_match.solution,
                "confidence": round(
                    best_score * 100,
                    2
                )
            }

        return {
            "matched": False
        }
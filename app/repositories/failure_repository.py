from app.database.db import SessionLocal
from app.database.models import FailureHistory


class FailureRepository:

    def get_all(self):

        session = SessionLocal()

        try:
            return session.query(
                FailureHistory
            ).all()

        finally:
            session.close()

    def save(
        self,
        signature,
        root_cause,
        solution
    ):

        session = SessionLocal()

        try:

            existing = (
                session.query(FailureHistory)
                .filter(
                    FailureHistory.signature == signature
                )
                .first()
            )

            if existing:
                return existing

            item = FailureHistory(
                signature=signature,
                root_cause=root_cause,
                solution=solution
            )

            session.add(item)

            session.commit()

            return item

        finally:
            session.close()
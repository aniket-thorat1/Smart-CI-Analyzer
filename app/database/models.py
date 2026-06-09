from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FailureHistory(Base):

    __tablename__ = "failure_history"

    id = Column(
        Integer,
        primary_key=True
    )

    signature = Column(
        String,
        nullable=False
    )

    root_cause = Column(
        String,
        nullable=False
    )

    solution = Column(
        String,
        nullable=False
    )
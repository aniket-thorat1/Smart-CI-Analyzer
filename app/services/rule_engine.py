import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PATTERN_FILE = os.path.join(
    BASE_DIR,
    "data",
    "failure_patterns.json"
)

with open(PATTERN_FILE, "r") as file:
    FAILURE_PATTERNS = json.load(file)


class RuleEngine:

    @staticmethod
    def find_match(log_text):

        for pattern, metadata in FAILURE_PATTERNS.items():

            if pattern.lower() in log_text.lower():

                return {
                    "matched": True,
                    "rootCause": metadata["cause"],
                    "solution": metadata["solution"]
                }

        return {
            "matched": False
        }
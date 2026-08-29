"""Best-score persistence isolated from pygame and the game loop."""

from __future__ import annotations

import json
from pathlib import Path


class HighScoreStore:
    """Persist one non-negative integer score in a user-provided file.

    Corrupt, missing or unreadable files are treated as an empty score so a
    local preference file can never prevent the game from starting.
    """

    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> int:
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
            score = int(payload.get("best_score", 0))
            return max(score, 0)
        except (OSError, ValueError, TypeError, AttributeError, json.JSONDecodeError):
            return 0

    def save_if_new_record(self, score: int) -> int:
        best = max(self.load(), int(score), 0)
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            temporary = self.path.with_suffix(self.path.suffix + ".tmp")
            temporary.write_text(json.dumps({"best_score": best}, indent=2) + "\n", encoding="utf-8")
            temporary.replace(self.path)
        except OSError:
            # A read-only home directory should not break the game.
            pass
        return best

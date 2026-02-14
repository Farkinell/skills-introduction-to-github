from datetime import date
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="BorgCal API", version="0.1.0")


class MoodEntry(BaseModel):
    day: date
    quick: Literal["up", "down"]
    mood_score: int | None = Field(default=None, ge=1, le=10)
    note_markdown: str | None = None


MOODS: dict[str, MoodEntry] = {}


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "borgcal-api"}


@app.get("/api/moods")
def list_moods() -> list[MoodEntry]:
    return list(MOODS.values())


@app.put("/api/moods/{day}")
def upsert_mood(day: date, payload: MoodEntry) -> MoodEntry:
    # MVP rule: one entry per day, editable
    MOODS[day.isoformat()] = payload
    return payload

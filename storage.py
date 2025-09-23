import json
import os
from pathlib import Path
from datetime import datetime

HISTORY_PATH = "history.json"

def _corrupted_backup_name (p: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")

    return p.with_name(f"{p.stem}.corrupted-{ts}{p.suffix}")

def load_history(path: str = HISTORY_PATH) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []

    try:
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("history root is not a list")
        return data

    except Exception:

        try:
            backup = _corrupted_backup_name(p)
            os.replace(p, backup)

        except Exception:

            pass

        return []

def save_history(history: list[dict], path: str = HISTORY_PATH) -> None:
    p = Path(path)
    tmp = p.with_name(f"{p.stem}.tmp")

    if not p.parent.exists():
        p.parent.mkdir(parents=True, exist_ok=True)

    with tmp.open("w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())

    os.replace(tmp, p)

import json
from datetime import datetime


class MailLogger:
    def __init__(self):
        self.logs = []

        self.stats = {
            "total": 0
        }

    def log_email(self, filename, category):
        record = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "file": filename,
            "category": category
        }

        self.logs.append(record)

        self.stats["total"] += 1

        if category not in self.stats:
            self.stats[category] = 0

        self.stats[category] += 1

    def save_logs(self, filename="process_log.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                self.logs,
                f,
                ensure_ascii=False,
                indent=4
            )

    def save_stats(self, filename="stats.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                self.stats,
                f,
                ensure_ascii=False,
                indent=4
            )

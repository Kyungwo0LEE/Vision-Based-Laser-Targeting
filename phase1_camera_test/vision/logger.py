#tracking data csv 저장코드

import csv
import os
from datetime import datetime


class TrackingLogger:
    def __init__(self):
        os.makedirs("logs/tracking", exist_ok=True)

        self.filename = (
            "logs/tracking/"
            f"tracking_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        )

        self.file = open(self.filename, "w", newline="", encoding="utf-8")
        self.writer = csv.writer(self.file)

        
        self.writer.writerow([
            "time",
            "entity_id",
            "x", "y", "z",
            "width", "height"
        ])

        print(f"[LOGGER] tracking log file created: {self.filename}")

    def log(self, entities):
        ts = datetime.now().isoformat()
        for i, e in enumerate(entities):
            self.writer.writerow([
                ts,
                i,
                e.x,
                e.y,
                e.z,
                e.width,
                e.height
            ])

    def close(self):
        self.file.close()
        print("[LOGGER] tracking log file closed")

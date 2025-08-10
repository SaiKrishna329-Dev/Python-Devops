# You want to periodically clean up /tmp files > 100MB using Python

import os
import time
from datetime import datetime

# Configuration
DIR_TO_CLEAN = "/tmp"
SIZE_THRESHOLD_MB = 100
CHECK_INTERVAL_SECONDS = 3600  # Run every hour

def cleanup_tmp():
    now = datetime.now()
    print(f"[{now}] Starting cleanup in {DIR_TO_CLEAN}...")

    for root, dirs, files in os.walk(DIR_TO_CLEAN):
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                size_bytes = os.path.getsize(file_path)
                size_mb = size_bytes / (1024 * 1024)

                if size_mb > SIZE_THRESHOLD_MB:
                    os.remove(file_path)
                    print(f"🗑 Deleted: {file_path} ({size_mb:.2f} MB)")

            except Exception as e:
                print(f"⚠ Error deleting {file_path}: {e}")

    print(f"[{datetime.now()}] Cleanup completed.\n")


if __name__ == "__main__":
    while True:
        cleanup_tmp()
        time.sleep(CHECK_INTERVAL_SECONDS)

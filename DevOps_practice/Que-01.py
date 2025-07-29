# Check All Files in a Directory for Size > 100MB

import os
import glob

directories = ["/var/log/*", "/tmp/*"]
threshold = 100 * 1024 * 1024  # 100MB in bytes

for i in directories:
    for file_path in glob.glob(i):
        if os.path.isfile(file_path):
            try:
                size_bytes = os.path.getsize(file_path)
                if size_bytes >= threshold:
                    size_mb = size_bytes / (1024 * 1024)
                    print(f"File over 100MB: {file_path} ({size_mb:.2f} MB)")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

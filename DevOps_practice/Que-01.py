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



# * glob module:
# The glob module in Python is used to search for files and directories whose names match a specified pattern (with wildcards like *, ?, [], etc.).

# It returns a list of matching file paths.

# ✅ pattern:
# In your code, pattern comes from the list:
# directories = ["/var/log/*", "/tmp/*"]
# So, for example, pattern = "/var/log/*"

# ✅ glob.glob(pattern):
# This expands the wildcard pattern like a shell would.

# Example:

# glob.glob("/var/log/*")

# might return:

# [
#   '/var/log/syslog',
#   '/var/log/auth.log',
#   '/var/log/dpkg.log',
#   '/var/log/private',
#   ...
# ]

## 1. System & File Management
| Module        | Purpose                                                                                      | Example Use Case                           |
| ------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **`os`**      | Interact with the operating system — environment variables, paths, file/directory operations | Get `$PATH`, create folders, check OS type |
| **`shutil`**  | High-level file operations                                                                   | Copy/move/delete files, get disk usage     |
| **`glob`**    | File pattern matching (wildcards)                                                            | Find all `.log` files in a directory       |
| **`pathlib`** | Object-oriented file path handling                                                           | Create platform-independent paths          |


## 2. System Monitoring

| Module         | Purpose                                       | Example Use Case                            |
| -------------- | --------------------------------------------- | ------------------------------------------- |
| **`psutil`**   | Monitor CPU, memory, disk, processes, network | Build resource monitoring alerts            |
| **`platform`** | Get system information                        | Detect OS type for cross-platform scripts   |
| **`socket`**   | Low-level networking                          | Check port availability, build TCP services |


## 3. Process & Command Execution

| Module           | Purpose                        | Example Use Case                        |
| ---------------- | ------------------------------ | --------------------------------------- |
| **`subprocess`** | Run shell commands from Python | Deploy scripts, call `kubectl`          |
| **`signal`**     | Handle OS signals              | Graceful shutdown of automation scripts |

## 4. Networking & APIs

| Module            | Purpose                   | Example Use Case                            |
| ----------------- | ------------------------- | ------------------------------------------- |
| **`requests`**    | Make HTTP/HTTPS API calls | Call REST APIs (AWS, Jenkins, GitLab, etc.) |
| **`http.server`** | Lightweight web server    | Serve logs or health checks locally         |
| **`urllib`**      | URL handling              | Download files, encode query params         |


## 5. Data Handling & Formats

| Module                    | Purpose                  | Example Use Case                             |
| ------------------------- | ------------------------ | -------------------------------------------- |
| **`json`**                | Read/write JSON data     | Parse API responses                          |
| **`yaml`** (via `PyYAML`) | Read/write YAML          | Manage Kubernetes manifests, Ansible configs |
| **`csv`**                 | Work with CSV data       | Export server inventory reports              |
| **`configparser`**        | Read `.ini` config files | Manage tool configurations                   |

## 6. Date & Time Utilities

| Module         | Purpose                              | Example Use Case                  |
| -------------- | ------------------------------------ | --------------------------------- |
| **`datetime`** | Work with dates/times                | Timestamp logs, schedule jobs     |
| **`time`**     | Delay execution, measure performance | Retry logic, backoff in API calls |


## 7. Automation & Scheduling

| Module                              | Purpose                       | Example Use Case                 |
| ----------------------------------- | ----------------------------- | -------------------------------- |
| **`sched`**                         | Simple scheduler              | Run cleanup scripts periodically |
| **`threading` / `multiprocessing`** | Run parallel tasks            | Monitor multiple servers at once |
| **`schedule`** (third-party)        | Human-friendly job scheduling | Run jobs every 5 minutes         |


## 8. Cloud & Infrastructur

| Module             | Purpose            | Example Use Case              |
| ------------------ | ------------------ | ----------------------------- |
| **`boto3`**        | AWS SDK for Python | Create EC2, manage S3, Lambda |
| **`azure-mgmt`**   | Azure SDK          | Manage Azure VMs and storage  |
| **`google-cloud`** | GCP SDK            | Automate GCP deployments      |


## 9. Security & Encryption

| Module             | Purpose                          | Example Use Case                 |
| ------------------ | -------------------------------- | -------------------------------- |
| **`hashlib`**      | Hashing                          | File integrity checks            |
| **`cryptography`** | Encryption/decryption            | Secure credentials in automation |
| **`secrets`**      | Generate secure tokens/passwords | Create random API keys           |


## 10. Testing & Validation

| Module                    | Purpose           | Example Use Case                  |
| ------------------------- | ----------------- | --------------------------------- |
| **`unittest` / `pytest`** | Automated testing | Test deployment scripts           |
| **`re`**                  | Regex matching    | Parse logs, validate config files |

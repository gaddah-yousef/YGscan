<h1 align="center">YGscan</h1>

> YGscan is an open-source Web Vulnerability Discovery Tool based on Python3. It supports both active scanning and passive proxy scanning, and runs across Windows, Linux, and Mac OS.

##  Presentation

YGscan is a powerful auditing tool completely repackaged and customized by **yousef_ZEX22**.

It features a rich set of automated detection plugins:
- **XSS Scanning** (Semantic-based reflective XSS scanning with high accuracy)
- **JSONP Information Leakage**
- **SQL Injection** (Error-based, Boolean-based, Time-based)
- **HTTP Smuggling Attacks**
- **Fastjson Detection and Exploitation**
- **.Net Cross-Site Scripting**
- **IIS Parsing Vulnerabilities**
- **Sensitive File / Information Leaks** (Backups, directories, git/svn, phpinfo, etc.)
- **Deserialization vulnerabilities**
- **Command / Code Injection** (OS Command, PHP, ASP)
- **Path Traversal Vulnerabilities**
- **Struts2 Vulnerabilities** (s2-016, s2-032, s2-045)
- **Webpack Source File Leakage**
- **Unauthorized Access Plugins**

##  Installation

To use YGscan via Docker (Recommended):
```bash
git clone <repository>
cd scanning/ygscan

# Build the docker container locally
docker build -t ygscan .
```

Alternatively, you can run it manually with Python 3.6+:
```bash
pip3 install -r requirements.txt
cd YGSCAN
python3 ygscan.py -h
```

##  Usage

### Active Scan
To run a direct vulnerability scan against an endpoint:
```bash
docker run --rm --entrypoint python3 ygscan ygscan.py -u http://testphp.vulnweb.com
```

You can also use a file with a list of URLs using the `-f` flag:
```bash
docker run --rm -v $(pwd):/data --entrypoint python3 ygscan ygscan.py -f /data/targets.txt
```

### Passive Scan (Proxy Mode)
To capture traffic and perform scanning in real-time acting as an HTTP/HTTPS proxy on port `7778`:
```bash
docker run -it --rm -p 7778:7778 --entrypoint python3 ygscan ygscan.py -s 0.0.0.0:7778 --html
```
*Note: Once started, you can configure your browser's HTTP proxy to `127.0.0.1:7778`. YGscan will automatically scan any traffic that passes through and will generate a real-time HTML report.*

### Customizing Plugins
Use `--able` to force load only specific modules and `--disable` to ignore others:
```bash
# Disable SQLi error plugins
docker run --rm --entrypoint python3 ygscan ygscan.py -u http://example.com --disable sqli_error
```

## Editor & Credits
- **Editor**: yousef_ZEX22
- Based on the open-source community edition ygscan.

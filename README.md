<div align="center">

# 🕸️ YGscan
### Web Vulnerability Scanning · Plugin-Based Security Research · Python

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Scope-Authorized%20Testing-0B7285)
![Origin](https://img.shields.io/badge/Origin-Community%20Project-6C757D)

**A customized, community-derived web security scanning toolkit with active scanning and proxy-oriented modules.**

[Overview](#-capabilities) · [Getting started](#-getting-started) · [Attribution](#-upstream-attribution) · [Portfolio](https://github.com/gaddah-yousef/SOC-LAB/blob/main/docs/portfolio/github-projects.md)

</div>

---

## 🎯 Capabilities

The source tree contains modular implementations for:

- Web server and framework fingerprinting
- XSS, SQL injection and injection-related checks
- Information exposure and path-traversal checks
- Request parsing and proxy-based analysis
- Multiple vulnerability-specific detection plugins

> **Status:** this is a research/learning adaptation of existing community code, **not an independently validated scanner**. Module coverage does not imply a guaranteed ability to detect or exploit any particular vulnerability.

## 🧩 How it is organized

| Path | Purpose |
| --- | --- |
| [`YGscan/ygscan.py`](YGscan/ygscan.py) | Python entry point |
| [`YGscan/`](YGscan/) | Scanner implementation and modules |
| [`YGscan/fingprints/`](YGscan/fingprints/) | Fingerprinting logic |
| [`requirements.txt`](requirements.txt) | Python dependencies |
| [`Dockerfile`](Dockerfile) | Legacy container packaging |
| [`CONTRIBUTORS.md`](CONTRIBUTORS.md) | Original contributor information |

## ⚙️ Getting started

Use an isolated Python virtual environment:

```bash
git clone https://github.com/gaddah-yousef/YGscan.git
cd YGscan

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

# The actual entry point is inside the YGscan/ directory.
cd YGscan
python3 ygscan.py -h
```

**Note:** dependency compatibility may require adjustment on modern Python versions. This setup is provided as a starting point, **not as a verified end-to-end installation**.

The current `Dockerfile` uses a legacy working-directory path and should be reviewed before treating Docker usage as supported. A separate [improvement PR](https://github.com/gaddah-yousef/YGscan/pull/1) has been proposed but is **not assumed merged**.

## 🔐 Safe usage

- Use only against web applications and endpoints for which you have **explicit authorization**.
- Work in a laboratory or a scoped penetration-testing engagement.
- Avoid automatic testing against real websites without permission.
- Treat scanner findings as leads: reproduce and verify them manually before reporting.

## 🤝 Upstream attribution

**YGscan is derived from an earlier open-source community scanner.** This repository showcases adaptation and study; it must not be represented as a wholly original codebase.

See [`CONTRIBUTORS.md`](CONTRIBUTORS.md) and [`LICENSE`](LICENSE) for contributor and licensing information. Follow the original project's license and attribution requirements.

## 👤 Maintainer

**Yousef Gaddah** · [GitHub](https://github.com/gaddah-yousef) · [Other cybersecurity projects](https://github.com/gaddah-yousef/SOC-LAB/blob/main/docs/portfolio/github-projects.md)

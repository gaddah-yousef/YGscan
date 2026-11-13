# Isolated educational scanner image. Use only on authorized lab targets.
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /opt/ygscan
COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt && \
    groupadd --system ygscan && \
    useradd --system --gid ygscan --home-dir /opt/ygscan ygscan

COPY --chown=ygscan:ygscan YGscan ./YGscan
USER ygscan
WORKDIR /opt/ygscan/YGscan

# Demonstrate help by default; actual scans require explicit user arguments.
ENTRYPOINT ["python", "ygscan.py"]
CMD ["--help"]

FROM python:3.12.3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV XTRACE_API_KEY=""
ENV ORGANIZATION_ID=""
ENV KNOWLEDGE_BASE_ID=""
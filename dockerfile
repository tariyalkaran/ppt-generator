
# -----------------------------
# Base image
# -----------------------------
FROM python:3.12-slim
# -----------------------------
# Set working directory
# -----------------------------
WORKDIR /app/frontend
# -----------------------------
# Install system dependencies
# - build tools
# - LibreOffice (PPT → PDF)
# - poppler-utils (PDF → PNG)
# - ODBC (MS SQL)
# -----------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
   build-essential \
   curl \
   gnupg \
   unixodbc-dev \
   libreoffice \
   poppler-utils \
&& curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg \
&& curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
&& apt-get update \
&& ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
# -----------------------------
# Copy requirements first (cache-friendly)
# -----------------------------
COPY requirements.txt .
# -----------------------------
# Install Python dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt
# -----------------------------
# Copy project files
# -----------------------------
COPY . .
# -----------------------------
# Expose Streamlit port
# -----------------------------
EXPOSE 9403
# -----------------------------
# Streamlit environment variables
# -----------------------------
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=9403
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV PYTHONPATH=/app
# -----------------------------
# Start Streamlit app
# IMPORTANT: run frontend/app.py
# -----------------------------
CMD ["streamlit", "run", "AI PPT Generator.py"]

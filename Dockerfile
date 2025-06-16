FROM quay.io/astronomer/astro-runtime:9.3.0

# Skip ONBUILD by doing everything explicitly
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /usr/local/airflow/dags/

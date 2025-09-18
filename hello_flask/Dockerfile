FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    pip install --no-cache-dir flask mysqlclient && \
    apt-get remove -y gcc pkg-config && \
    apt-get autoremove -y && \
    apt-get clean
EXPOSE 5000
CMD ["python", "app.py"]
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY heart_predict.pkl /app
COPY main.py /app
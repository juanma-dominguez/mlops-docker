FROM python:3.7

WORKDIR /app

RUN pip install pandas scikit-learn

ADD predict.py .

CMD ["python", "predict.py"]
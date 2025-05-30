FROM python:3.13.3
# RUN pip install mysql-connector-python
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY Flask .

EXPOSE 5000

# CMD ["python", "app.py"]
# CMD ["flask", "run", "--host=0.0.0.0"],
CMD flask run -h 0.0.0.0 -p 5000
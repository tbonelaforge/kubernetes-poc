FROM python:2
COPY app.py .
COPY database.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
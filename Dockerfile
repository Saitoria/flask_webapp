FROM python:3.12-alpine3.19
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python","main.py"]

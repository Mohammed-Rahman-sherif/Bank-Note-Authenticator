FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 8000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
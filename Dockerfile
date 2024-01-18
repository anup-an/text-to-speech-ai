FROM python:3.11

WORKDIR /app

COPY requirements requirements

COPY Makefile .

RUN pip install pip-tools

RUN make install

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
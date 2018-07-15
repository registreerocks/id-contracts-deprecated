FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./package /usr/src/app

RUN mkdir /usr/src/app/contracts
COPY ./build/contracts /usr/src/app/contracts

RUN pip3 install -e .

EXPOSE 8080

CMD ["python3", "-m", "swagger_server"]
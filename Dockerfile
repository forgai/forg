FROM python:3.8-slim-bullseye as py38

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y curl \
    && apt-get install -y libpq-dev \
    && apt-get install -y libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /repository/requirements.txt
RUN python3 -m pip install -r /repository/requirements.txt

ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

ENV PYTHONPATH="/repository/src:$PYTHONPATH"

WORKDIR /repository

ENTRYPOINT ["tail", "-f", "/dev/null"]


FROM python:3.9-slim-bullseye as py39

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y curl \
    && apt-get install -y libpq-dev \
    && apt-get install -y libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /repository/requirements.txt
RUN python3 -m pip install -r /repository/requirements.txt

ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

ENV PYTHONPATH="/repository/src:$PYTHONPATH"

WORKDIR /repository

ENTRYPOINT ["tail", "-f", "/dev/null"]


FROM python:3.10-slim-bullseye as py310

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y curl \
    && apt-get install -y libpq-dev \
    && apt-get install -y libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /repository/requirements.txt
RUN python3 -m pip install -r /repository/requirements.txt

ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

ENV PYTHONPATH="/repository/src:$PYTHONPATH"

WORKDIR /repository

ENTRYPOINT ["tail", "-f", "/dev/null"]


FROM python:3.11-slim-bullseye as py311

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y curl \
    && apt-get install -y libpq-dev \
    && apt-get install -y libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /repository/requirements.txt
RUN python3 -m pip install -r /repository/requirements.txt

ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

ENV PYTHONPATH="/repository/src:$PYTHONPATH"

WORKDIR /repository

ENTRYPOINT ["tail", "-f", "/dev/null"]


FROM python:3.12-slim-bullseye as py312

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y curl \
    && apt-get install -y libpq-dev \
    && apt-get install -y libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /repository/requirements.txt
RUN python3 -m pip install -r /repository/requirements.txt

ARG USER_ID=1000
ARG GROUP_ID=1000
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

ENV PYTHONPATH="/repository/src:$PYTHONPATH"

WORKDIR /repository

ENTRYPOINT ["tail", "-f", "/dev/null"]
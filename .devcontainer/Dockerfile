# Use the minimal Ubuntu image
FROM ubuntu:22.04

ENV IMAGE_VERSION="0.1.2"

ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    libpq-dev \
    && apt-get clean

# Install pyenv
RUN curl https://pyenv.run | bash

# Set environment variables for pyenv
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"

# Initialize pyenv for non-interactive shell
RUN eval "$(pyenv init --path)" && \
    eval "$(pyenv init -)"

# Install the latest Python versions
RUN pyenv install 3.9.22 && \
    pyenv install 3.10.17 && \
    pyenv install 3.11.12 && \
    pyenv install 3.12.6 && \
    pyenv install 3.13.2

RUN pyenv global 3.11.12

# Install dev dependencies
RUN pip install ruff==0.11.8 mypy==1.15.0

ENV HOME="/root"

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set Poetry config
ENV PATH="$HOME/.local/bin:$PATH"

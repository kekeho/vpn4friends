FROM python:3.7.2
ENV PYTHONNUNBUFFERED 1

# Init dirs
RUN mkdir /code
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy source codes
COPY . /code/

CMD ./migrate-runserver.sh
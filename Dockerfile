FROM python:3.10

RUN apt-get update && apt-get install -y

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN apt-get install antiword

CMD ["/bin/bash"]

FROM ubuntu:latest

WORKDIR /app
COPY . /app

RUN apt update
RUN apt install -y python3
# RUN apt install -y python3-pip
# RUN apt install -y python3-venv
# RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENV PORT 8080

RUN apt install -y python3-uvicorn python3-fastapi

EXPOSE 8080

# CMD cron && tail -f /var/log/cron.log
CMD uvicorn adaptable_needs:app --host 0.0.0.0 --port 8080
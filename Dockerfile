FROM ubuntu:latest

WORKDIR /app
COPY . /app

RUN apt update

ENV PORT 80
EXPOSE 80
EXPOSE 5432

RUN apt install -y cron
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt

COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN touch /var/log/cron.log

RUN crontab /etc/cron.d/cron

CMD ["bash", "run_all.sh"]

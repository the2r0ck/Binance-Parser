FROM ubuntu:latest

WORKDIR /app
COPY . /app

RUN apt update
RUN apt install -y cron
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV TRADINGBOT_DATABASE_HOST="user-prod-us-east-2-1.cluster-cfi5vnucvv3w.us-east-2.rds.amazonaws.com"
ENV TRADINGBOT_DATABASE_USER="my-test-app-with-db-main-db-09717c4760f867026"
ENV TRADINGBOT_DATABASE_PORT="5432"
ENV TRADINGBOT_DATABASE_PASSWORD="P7nWQ6eFc6bzVMeuFAsF5FFMe3ePNP"
ENV TRADINGBOT_DATABASE_NAME="my-test-app-with-db-main-db-09717c4760f867026"

ENV BINANCE_API_KEY="gCtgLLqdsYdx1tnppXE6Kj8lFJUaGcRCU2WbUMFdUHG6SdG2kWuOlU3oM2Lnj7Fc"
ENV BINANCE_API_SECRET="9BBlEfa03IMEcMWxVevdDXyG0fr1PZ4hjL1DU665kVr0itJ1Wcv5COyhwJl7tbzo"

ENV TELEGRAM_ALERT_BOT_TOKEN="7241377415:AAGuQCcRc7JwBcoYt6f5QQwtGNJUx0ukkho"
ENV TELEGRAM_INFO_BOT_TOKEN="7279065863:AAF_U-fehbQfFlzzfBX666l_pJIol1LxxFM"
ENV TELEGRAM_SUPPORT_USER_ID="1037555181"

RUN pip install -r requirements.txt

COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN touch /var/log/cron.log

RUN crontab /etc/cron.d/cron

EXPOSE 5432

CMD cron && tail -f /var/log/cron.log

FROM ubuntu:latest

WORKDIR /app
COPY . /app

RUN apt update

ENV PORT 80
EXPOSE 80

RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install uvicorn fastapi

# CMD cron && tail -f /var/log/cron.log
CMD ["uvicorn", "adaptable_needs:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:latest

RUN adduser -D appuser
USER appuser

WORKDIR /python-demo

COPY --chown=appuser:appuser requirements.txt requirements.txt

ENV TZ=Asia/Singapore
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --user -r requirements.txt

ENV PATH="/home/appuser/.local/bin:${PATH}"

COPY --chown=appuser:appuser . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=8080"]

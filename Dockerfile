FROM python:3.9

WORKDIR /home/web/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]

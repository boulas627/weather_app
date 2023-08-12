FROM python:3

WORKDIR /Python_Projects/weather_app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
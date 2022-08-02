FROM python:slim
ENV TOKEN='place_your_token_here'
COPY . .
RUN pip install -r req.txt
CMD python bot.py
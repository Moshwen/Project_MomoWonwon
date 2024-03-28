# Основной код приложения для определения тональности текста на английском языке
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
# Получаем готового модель машинного обучения из библиотеки Hugging Face
pipe = pipeline('text-classification', model='SamLowe/roberta-base-go_emotions', top_k=None)


@app.get("/")
def root():
    return {"Определение тональности текста на английском языке"}


@app.post("/predict/")
def predict(item: Item):
    if item.text == '': # Если в поле не введен никакого текста то программа выдаст это сообщение
        return 'Текст не введен'
    else:
        return pipe(item.text)[0] # Если все таки текст введен на русском языке, программа определит ее тональность и выдаст результат

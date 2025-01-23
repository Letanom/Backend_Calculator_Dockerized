#Dockerize
#slim kullanıcam çünkü daha az yer kaplar python versiyonum 3.12
FROM python:3.12-slim
#Çalışma dizini
WORKDIR /app
#Gerekli kütüphaneler
COPY requirements.txt .
RUN pip install -r requirements.txt
#Uygulamayı kopyalama
COPY . .
#Uygulamayı çalıştırma venv de çalıştırıyorum expose 7000 ona göre

EXPOSE 7000
#Uygulamayı sanalda çalıştırıyorum venvde 

# Use uvicorn to run the FastAPI app

#host niye var çünkü

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]

##konsla docker build -t  .yaparak docker image oluşturulur  


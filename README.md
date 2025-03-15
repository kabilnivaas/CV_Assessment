
### CV_Assessment  
A Computer Vision assessment project that trains a deep learning model for image classification and serves predictions using a FastAPI-based REST API. The application supports image uploads, performs inference using a trained model, and is containerized with Docker.

---

## Features 
✅ Train a CNN-based model using **PyTorch**  
✅ Save and load the trained model  
✅ Serve predictions via **FastAPI**  
✅ Implement basic authentication for API access  
✅ Test the API with **Postman** or **CURL**  
✅ Deploy using **Docker**  

---

## **Setup Instructions**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/kabilnivaas/CV_Assessment.git
cd CV_Assessment
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Train the Model**  
Run the training script to train and save the model:  
```bash
python train.py
```
This will save the model as `fast_model.pth`.

### **4. Start the FastAPI Server**  
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at:  
🔗 `http://127.0.0.1:8000`

---

## **API Usage**  

### **1. Predict an Image**
#### **Endpoint:** `/predict`
- **Method:** `POST`
- **Headers:** `Content-Type: multipart/form-data`
- **Authentication:** API key (`api_key=secretkey123`)
- **Body:** Upload an image file  

#### **Example Request (CURL)**  
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict?api_key=secretkey123' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@image.png'
```

#### **Example Response**
```json
{
  "class": "cat",
  "confidence": 0.92
}
```

---

## **Docker Deployment**  
### **1. Build the Docker Image**
```bash
docker build -t cv_assessment .
```

### **2. Run the Docker Container**
```bash
docker run -p 8000:8000 cv_assessment
```
The API will be accessible at `http://localhost:8000`.

---

## **Testing with Ngrok** *(For Google Colab or Cloud VM)*
```python
!pip install pyngrok
from pyngrok import ngrok

ngrok_tunnel = ngrok.connect(8000)
print("Public URL:", ngrok_tunnel.public_url)
```
Use the **Ngrok URL** in API requests instead of `127.0.0.1:8000`.

---

## **Contributors**  
👤 **Kabil Nivaas**  

---

## **License**  
This project is licensed under the **MIT License**.

---

Let me know if you need modifications! 🚀

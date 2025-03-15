from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from PIL import Image
import torch
import torchvision.transforms as transforms
from torch.nn import functional as F
import io

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
class SimpleNN(torch.nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = torch.nn.Linear(28 * 28, 128)
        self.fc2 = torch.nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(x.shape[0], -1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleNN().to(device)
model.load_state_dict(torch.load("fast_model.pth", map_location=device))
model.eval()

# Define the transformation for input images
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Basic Authentication
API_KEY = "secretkey123"

def authenticate(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

# Prediction endpoint
@app.post("/predict")
async def predict(api_key: str = Depends(authenticate), file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("L")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        probabilities = F.softmax(outputs, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()

    return {"predicted_class": predicted_class, "confidence": probabilities[0][predicted_class].item()}

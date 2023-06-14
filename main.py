import torch
import clip
from PIL import Image
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
choice = ["It is duck neck.", "It is a mouse"]

image = preprocess(Image.open("food.png")).unsqueeze(0).to(device)
text = clip.tokenize(choice).to(device)

with torch.no_grad():
    logits_per_image, logits_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

print(choice[int(np.argmax(probs[0]))])
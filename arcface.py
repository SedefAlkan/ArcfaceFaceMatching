import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from deepface import DeepFace


dataset_path = "dataset"
csv_file = "master1.csv"


df = pd.read_csv(csv_file)


fig, axes = plt.subplots(len(df), 3, figsize=(10, len(df) * 3))

for index, row in df.iterrows():
    file_x = os.path.join(dataset_path, row["file_x"])
    file_y = os.path.join(dataset_path, row["file_y"])
    
    try:
       
        result = DeepFace.verify(img1_path=file_x, img2_path=file_y, model_name="ArcFace")
        predicted_decision = "Yes" if result["verified"] else "No"
        similarity_score = result["distance"]
        
       
        img1 = cv2.imread(file_x)
        img2 = cv2.imread(file_y)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        
        
        axes[index, 0].imshow(img1)
        axes[index, 0].axis("off")
        
        axes[index, 1].imshow(img2)
        axes[index, 1].axis("off")

        
        actual = row["Decision"]
        axes[index, 2].text(0.1, 0.5, f"Actual: {actual}\nPredicted: {predicted_decision}\nScore: {similarity_score:.4f}",
                            fontsize=12, verticalalignment="center")
        axes[index, 2].axis("off")

        print(f"Processed: {row['file_x']} vs {row['file_y']} - Predicted: {predicted_decision} - Score: {similarity_score:.4f}")
    
    except Exception as e:
        print(f"Error processing {row['file_x']} vs {row['file_y']}: {e}")

# Sonuçları göster
plt.tight_layout()
plt.show()

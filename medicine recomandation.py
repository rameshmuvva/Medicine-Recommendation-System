import tkinter as tk
from tkinter import messagebox

# Sample data for diseases and medicines
disease_medicine_dict = {
    "cold": "Paracetamol, Rest, Sudafed, D'Cold Total, Benadryl  and Hydration",
    "fever": "Ibuprofen, Paracetamol",
    "headache": "Aspirin, Ibuprofen",
    "diabetes": "Metformin, Insulin",
    "hypertension": "Amlodipine, Lisinopril",
    "pain":"ibuprofen, ibuprofen",
    "asthma": "Albuterol, Inhaled Corticosteroids",
    "allergy": "Antihistamines, Decongestants"
}

# Function to fetch medicine recommendation
def get_recommendation():
    disease = entry_disease.get().lower()
    if disease in disease_medicine_dict:
        recommendation = disease_medicine_dict[disease]
        text_output.config(state=tk.NORMAL)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, f"Recommended medicines for {disease}:\n{recommendation}")
        text_output.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Information", "Disease not found in the database.")

# Setting up the main window
root = tk.Tk()
root.title("Medicine Recommendation Chatbot")
root.geometry("400x300")

# User input for disease
label_disease = tk.Label(root, text="Enter Disease:")
label_disease.pack(pady=10)

entry_disease = tk.Entry(root)
entry_disease.pack(pady=5)

# Button to get recommendation
btn_recommend = tk.Button(root, text="Get Recommendation", command=get_recommendation)
btn_recommend.pack(pady=10)

# Output display
text_output = tk.Text(root, height=10, state=tk.DISABLED)
text_output.pack(pady=10)

# Run the application
root.mainloop()

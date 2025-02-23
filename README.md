# **Transcribe-It**

### **Automated Transcription for Audio Files**

## **📖 Overview**
**Transcribe-It** is a Python-based audio transcription tool designed for **automatically converting speech into text**. 
I initially wrote the script to transcribe **assignment audio files** for a **German course** in **NPTEL** (as a*3rd-year compulsory subject*). 

Understanding the spoken content in these recordings was challenging for me, so I created this tool to streamline the process. 

## **⚙️ How It Works**
- The script **converts MP3 audio files** into **WAV (Waveform Audio Format)** and stores them in a temporary directory: 

- It then processes these WAV files and **extracts text** using **Google Speech Recognition**.  
- The transcriptions are **saved as `.txt` files**, named according to the corresponding audio file.  
- Users can specify the **language of the audio file**, and the script automatically maps it to the correct language code.  

---

## **🌍 Supported Languages**
The following languages are currently supported for transcription:  

- **English**  
- **German**  
- **French**  
- **Spanish**  
- **Italian**  
- **Portuguese**  
- **Hindi**  
- **Japanese**  
- **Chinese**  
- **Russian**  
- **Korean**  
- **Dutch**  

*More languages can be added upon request.*  

---

## **🛠️ Installation & Usage**
### **Prerequisites**
Ensure you have the following installed:  
- **Python 3.x**  
- **pip (Python package manager)**  

### **Installation**
1. Clone the repository:  
```bash
 git clone https://github.com/Suvash-Sharma97/Transcribe-It.git
 cd Transcribe-It
 pip install -r requirements.txt
```
2. Bring your audio files (in mp3) format to the same folder as main.py file.
```bash
    python main.py
```
### **Contributions***
Suggestions and contributions are welcome! If you have suggestions, feature requests, or find any issues, feel free to:

    Open an issue
    Submit a pull request

Let’s make Transcribe-It better together!

Copyright © Suvash Sharma Subedi 2025


ent" id="48271"}
# OpenJarvis + Ollama + Python Tools Setup (Ubuntu Server)

## 1) Update system
bash sudo apt update && sudo apt upgrade -y 

---

## 2) Install required packages
bash sudo apt install -y \ git \ curl \ ffmpeg \ python3 \ python3-pip \ python3-venv \ build-essential 

จุดพังบ่อย:
- ffmpeg ไม่มี → voice/audio ใช้ไม่ได้
- build-essential ไม่มี → บาง package compile ไม่ผ่าน

---

## 3) Install uv
bash curl -LsSf https://astral.sh/uv/install.sh | sh 

โหลด path ใหม่
bash source ~/.bashrc 

เช็ค
bash uv --version 

ถ้า command not found:
bash export PATH="$HOME/.local/bin:$PATH" source ~/.bashrc 

---

## 4) Clone/Open project
bash cd ~/Desktop/Project_sasta 

ถ้ายังไม่มี:
bash git clone <https://github.com/open-jarvis/OpenJarvis.git> 

เข้าโปรเจกต์
bash cd OpenJarvis 

---

## 5) Install python environment
bash uv sync 

จุดพังบ่อย:
- internet timeout
- package compile fail
- python version ต่ำเกิน

เช็ค python:
bash python3 --version 

ควรเป็น 3.10+

---

## 6) Activate venv
bash source .venv/bin/activate 

เช็ค:
bash which python 

ต้องขึ้นประมาณ:
bash .../OpenJarvis/.venv/bin/python 

---

## 7) Test OpenJarvis import
bash python -c "import openjarvis; print('OPENJARVIS OK')" 

ถ้าพัง:
bash uv sync --reinstall 

---

## 8) Check CLI
bash python -m openjarvis.cli --help 

---

## 9) Initialize config
bash python -m openjarvis.cli init 

---

# OLLAMA

## 10) Install Ollama
bash curl -fsSL https://ollama.com/install.sh | sh 

เช็ค:
bash ollama --version 

---

## 11) Start ollama service
bash sudo systemctl enable ollama sudo systemctl start ollama 

เช็ค:
bash systemctl status ollama 

---

## 12) Pull model

Llama:
bash ollama pull llama3 

Gemma:
bash ollama pull gemma3:4b 

จุดพังบ่อย:
- disk เต็ม
- RAM ไม่พอ
- model ใหญ่เกินเครื่อง

เช็ค model:
bash ollama list 

---

# CONNECT OPENJARVIS

## 13) Test ask
bash python -m openjarvis.cli ask "hello" 

ถ้า timeout:
bash ollama serve 

แล้วลองใหม่

---

## 14) Config
bash python -m openjarvis.cli config 

ตั้ง model ให้ตรงกับ:
bash ollama list 

เช่น:
bash llama3 
หรือ
bash gemma3:4b 

---

# EXTRA PYTHON TOOLS

## 15) Ensure pip
bash ./.venv/bin/python -m ensurepip 

---

## 16) Install requests
bash python -m pip install requests 

---

## 17) Install extra server dependencies
bash uv sync --extra server 

---

# TEST EVERYTHING

## 18) Test ollama
bash ollama run llama3 

หรือ
bash ollama run gemma3:4b 

---

## 19) Final test
bash python -m openjarvis.cli ask "What time is it?" 

---

# USEFUL COMMANDS

## Activate venv
bash source .venv/bin/activate 

## Exit venv
bash deactivate 

## Update dependencies
bash uv sync 

## Rebuild venv
bash rm -rf .venv uv sync 

---

# COMMON ERRORS

## "uv: command not found"
bash export PATH="$HOME/.local/bin:$PATH" source ~/.bashrc 

---

## "No module named openjarvis"
bash source .venv/bin/activate uv sync 

---

## "Connection refused localhost:11434"
Ollama ยังไม่รัน:
bash ollama serve 

---

## Model not found
เช็ค:
bash ollama list 

แล้วใช้ชื่อ model ให้ตรง

---

## RAM ไม่พอ
ใช้:
bash gemma3:4b 

แทน model ใหญ่

---

## Disk เต็ม
เช็ค:
bash df -h 

ลบ model:
bash ollama rm <MODEL_NAME> 

---

# OPTIONAL

## Auto-start ollama
bash sudo systemctl enable ollama 

---

## Run O

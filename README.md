# OpenJarvis + Ollama + Python Tools Setup (Ubuntu Server)

Complete setup guide for running OpenJarvis with Ollama on Ubuntu/Linux.

---

# 1. Update System

bash sudo apt update && sudo apt upgrade -y 

---

# 2. Install Required Packages

bash sudo apt install -y \     git \     curl \     ffmpeg \     python3 \     python3-pip \     python3-venv \     build-essential 

## Common Issues

- ffmpeg missing → audio/voice features may fail
- build-essential missing → some Python packages cannot compile

---

# 3. Install uv

Install uv package manager:

bash curl -LsSf https://astral.sh/uv/install.sh | sh 

Reload shell:

bash source ~/.bashrc 

Check installation:

bash uv --version 

If uv: command not found:

bash export PATH="$HOME/.local/bin:$PATH" source ~/.bashrc 

---

# 4. Clone OpenJarvis

Go to your workspace:

bash cd ~/Desktop/Project_sasta 

Clone repository:

bash git clone https://github.com/open-jarvis/OpenJarvis.git 

Enter project directory:

bash cd OpenJarvis 

---

# 5. Install Python Environment

bash uv sync 

## Common Issues

- Internet timeout
- Package compile failure
- Python version too old

Check Python version:

bash python3 --version 

Recommended: Python 3.10+

---

# 6. Activate Virtual Environment

bash source .venv/bin/activate 

Verify Python path:

bash which python 

Expected output:

bash .../OpenJarvis/.venv/bin/python 

---

# 7. Test OpenJarvis Import

bash python -c "import openjarvis; print('OPENJARVIS OK')" 

If import fails:

bash uv sync --reinstall 

---

# 8. Check CLI

bash python -m openjarvis.cli --help 

---

# 9. Initialize Config

bash python -m openjarvis.cli init 

---

# OLLAMA SETUP

# 10. Install Ollama

bash curl -fsSL https://ollama.com/install.sh | sh 

Verify installation:

bash ollama --version 

---

# 11. Start Ollama Service

Enable auto-start:

bash sudo systemctl enable ollama 

Start service:

bash sudo systemctl start ollama 

Check status:

bash systemctl status ollama 

---

# 12. Download Models

## Llama 3

bash ollama pull llama3 

## Gemma 3 (4B)

bash ollama pull gemma3:4b 

## Common Issues

- Disk full
- Not enough RAM
- Model too large for hardware

List installed models:

bash ollama list 

---

# CONNECT OPENJARVIS

# 13. Test OpenJarvis

bash python -m openjarvis.cli ask "hello" 

If timeout occurs:

bash ollama serve 

Then retry.

---

# 14. Configure Model

bash python -m openjarvis.cli config 

Set model name to match:

bash ollama list 

Example:

bash llama3 

or

bash gemma3:4b 

---

# EXTRA PYTHON TOOLS

# 15. Ensure pip Exists

bash ./.venv/bin/python -m ensurepip 

---

# 16. Install requests

bash python -m pip install requests 

---

# 17. Install Extra Server Dependencies

bash uv sync --extra server 

---

# TEST EVERYTHING

# 18. Test Ollama Directly

bash ollama run llama3 

or

bash ollama run gemma3:4b 

---

# 19. Final Test

bash python -m openjarvis.cli ask "What time is it?" 

---

# USEFUL COMMANDS

## Activate venv

bash source .venv/bin/activate 

## Exit venv

bash deactivate 

## Update dependencies

bash uv sync 

## Rebuild virtual environment

bash rm -rf .venv uv sync 

---

# COMMON ERRORS

## uv: command not found

bash export PATH="$HOME/.local/bin:$PATH" source ~/.bashrc 

---

## No module named openjarvis

bash source .venv/bin/activate uv sync 

---

## Connection refused localhost:11434

Ollama is not running:

bash ollama serve 

---

## Model not found

Check installed models:

bash ollama list 

Use the exact model name shown.

---

## RAM Not Enough

Use a smaller model:

bash gemma3:4b 

instead of larger models.

---

## Disk Full

Check disk usage:

bash df -h 

Remove unused models:

bash ollama rm <MODEL_NAME> 

---

# OPTIONAL

## Auto-start Ollama on Boot

bash sudo systemctl enable ollama 

---

# Recommended Hardware

| Component | Recommended |
|---|---|
| RAM | 16GB+ |
| CPU | 4+ cores |
| Storage | SSD |
| GPU | Optional |

---

# Notes

- Running large models may require significant RAM.
- SSD storage greatly improves model loading speed.
- Use smaller models on low-power systems such as Raspberry Pi or

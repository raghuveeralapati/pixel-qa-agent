## 🚀 Agentic Visual Validation AI Agent

An intelligent AI agent for pixel-to-pixel image comparison, visual regression detection and OCR-aligned validation workflows.  
Designed for QA automation, AI evaluation pipelines and enterprise-grade visual testing systems.

## 👤 Author
Raghuveer Alapati  

## 🧠 Key Features
- Pixel-to-pixel image comparison (OpenCV)
- SSIM similarity scoring
- Intelligent agent decision logic (PASS/FAIL)
- Visual regression detection
- Automation pipeline ready
- OCR validation extensibility

## 🏗️ Architecture
User Input → Agent Layer → Image Comparison Engine → Decision Engine → Output

Core Modules:
- Agent Layer (Decision Intelligence)
- Comparison Engine (Pixel + SSIM)
- Utility Layer (Image Processing)

## 🌳 Branching Strategy

This repository follows a structured branching model to support scalable development and maintain code stability.

## Branch Structure
- `main` → Stable, production-ready code (default branch)
- `dev` → Active development and testing
- `feature/*` → New features and enhancements
- `hotfix/*` → Critical bug fixes

## Workflow
1. New features are created from `dev` branch  
2. Feature branches are merged into `dev` after testing  
3. Stable releases are merged from `dev` to `main`  
4. Hotfix branches are created from `main` for urgent fixes  

This strategy ensures clean version control, stable releases and professional repository management.

## 📂 Project Structure
```
pixel-qa-agent/
├── agent/
├── utils/
├── samples/
├── app.py
├── requirements.txt
└── README.md
```
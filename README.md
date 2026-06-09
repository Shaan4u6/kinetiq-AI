# Kinetiq AI

**Augmented Reality Integrated System and Method for Physiotherapy Monitoring and Training Using Machine Learning**

An AI-powered platform that uses real-time pose estimation and augmented reality overlays to guide patients through physiotherapy exercises while giving therapists data-driven insights into recovery progress.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 15, TailwindCSS, TypeScript |
| Backend | Python 3.11+, FastAPI |
| Pose Detection | MediaPipe (Google) |
| AR Overlay | OpenCV |
| Database | SQLite |
| Auth | JWT (via FastAPI) |

---

## Features

- Real-time pose detection via webcam using MediaPipe
- AR skeleton overlay with joint angle feedback using OpenCV
- Exercise correctness scoring and rep counting
- Patient and therapist dashboards
- Session history and recovery analytics
- AI insights on posture deviations
- Role-based access: Admin, Therapist, Patient

---

## Project Structure

```
kinetiq-AI/
├── frontend/          # Next.js app (UI, dashboards, AR view)
│   ├── public/
│   └── src/
├── backend/           # FastAPI server (ML, pose analysis, REST API)
│   ├── app/
│   ├── models/
│   └── database/
├── README.md
├── package.json
└── ...config files
```

---

## Getting Started

### Frontend
```bash
npm install
npm run dev
```

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Requirements

- Node.js 18+
- Python 3.11+
- Webcam (for live pose detection)

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
| Containerization | Docker, Docker Compose |

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
├── frontend/                  # Next.js app (UI, dashboards, AR view)
│   ├── public/
│   └── src/
│       ├── app/
│       │   ├── analysis/
│       │   ├── dashboard/
│       │   │   ├── admin/
│       │   │   ├── ai-insights/
│       │   │   ├── patient/
│       │   │   └── therapist/
│       │   ├── login/
│       │   ├── register/
│       │   └── training/
│       └── context/
├── backend/                   # FastAPI server (ML, pose analysis, REST API)
│   └── app/
│       ├── database/          # SQLite models & DB setup
│       ├── routes/            # API route handlers
│       ├── schemas/           # Pydantic schemas
│       ├── services/          # Pose detection, MediaPipe, exercise logic
│       └── utils/
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Getting Started

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker (optional)
```bash
docker-compose up --build
```

---

## Requirements

- Node.js 18+
- Python 3.11+
- Webcam (for live pose detection)
- Docker & Docker Compose (optional)

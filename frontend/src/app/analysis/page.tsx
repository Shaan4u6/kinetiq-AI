"use client";

import Webcam from "react-webcam";
import { useRef, useState } from "react";

type Exercise = "elbow_flexion" | "shoulder_raise";

export default function AnalysisPage() {
  const webcamRef = useRef<Webcam>(null);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [exercise, setExercise] = useState<Exercise>("elbow_flexion");

  const analyzeFrame = async () => {
    setError(null);
    const imageSrc = webcamRef.current?.getScreenshot();
    if (!imageSrc) return;

    try {
      const response = await fetch("http://127.0.0.1:8000/analysis/frame", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: imageSrc, exercise }),
      });

      if (!response.ok) {
        const err = await response.json();
        setError(err.detail ?? "Server error");
        return;
      }

      setResult(await response.json());
    } catch {
      setError("Cannot reach backend. Is it running on port 8000?");
    }
  };

  const resetReps = async () => {
    await fetch(`http://127.0.0.1:8000/analysis/reset/${exercise}`, { method: "POST" });
    setResult(null);
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Physiotherapy Analysis</h1>

      <div className="mb-4 flex gap-3 items-center">
        <label className="font-medium">Exercise:</label>
        <select
          value={exercise}
          onChange={(e) => setExercise(e.target.value as Exercise)}
          className="border rounded px-3 py-1"
        >
          <option value="elbow_flexion">Elbow Flexion</option>
          <option value="shoulder_raise">Shoulder Raise</option>
        </select>
        <button onClick={resetReps} className="bg-gray-400 text-white px-3 py-1 rounded">
          Reset Reps
        </button>
      </div>

      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" className="rounded-lg" />

      <button
        onClick={analyzeFrame}
        className="bg-blue-500 text-white px-4 py-2 rounded mt-4"
      >
        Analyze
      </button>

      {error && <p className="mt-4 text-red-500">{error}</p>}

      {result && (
        <div className="mt-4 p-4 bg-gray-100 rounded-lg space-y-1">
          <p><span className="font-medium">Angle:</span> {result.angle}°</p>
          <p><span className="font-medium">Reps:</span> {result.rep_count}</p>
          <p><span className="font-medium">Feedback:</span> {result.feedback}</p>
          <p>
            <span className="font-medium">Status:</span>{" "}
            <span className={result.status === "correct" ? "text-green-600" : "text-red-500"}>
              {result.status}
            </span>
          </p>
        </div>
      )}
    </div>
  );
}

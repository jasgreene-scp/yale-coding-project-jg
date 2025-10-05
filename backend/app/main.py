from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # this can be restricted later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include your route modules
from app.routes import counts, measurements, auth, diseases, dbhealth

app.include_router(counts.router, prefix="/counts")
app.include_router(measurements.router, prefix="/measurements")
app.include_router(auth.router, prefix="/auth")
app.include_router(diseases.router, prefix="/diseases")
app.include_router(dbhealth.router)
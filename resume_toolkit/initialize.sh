# Set the active Google Cloud project
gcloud config set project careercatalyst-492714

# Enable required Google Cloud APIs
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  aiplatform.googleapis.com \
  compute.googleapis.com

# Clone the repository
git clone https://github.com/uttara-sriya/CareerCatalyst.git

# Navigate to the project directory
cd CareerCatalyst/

# Initialize and activate a Python virtual environment
uv venv
source .venv/bin/activate

# Define environment variables for the project
PROJECT_ID=$(gcloud config get-value project)
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
SA_NAME=career-catalyst-sa

# Create an environment configuration file
cat <<EOF > .env
PROJECT_ID=$PROJECT_ID
PROJECT_NUMBER=$PROJECT_NUMBER
SA_NAME=$SA_NAME
SERVICE_ACCOUNT=${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
MODEL="gemini-2.5-flash"
EOF

# Load variables and create the Service Account
source .env
gcloud iam service-accounts create ${SA_NAME} \
    --display-name="Service Account for Career Catalyst "

# Grant the Service Account permissions to use Vertex AI
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT" \
  --role="roles/aiplatform.user"

# Deploy the application to Cloud Run using Google ADK
uvx --from google-adk==1.14.0 \
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=europe-west1 \
  --service_name=career-sa \
  --with_ui \
  . \
  -- \
  --labels=project=careercatalyst \
  --service-account=$SERVICE_ACCOUNT
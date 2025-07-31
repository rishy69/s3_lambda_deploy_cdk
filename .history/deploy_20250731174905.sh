set -e

source .venv/bin/activate

pip install -r requirements.

AWS_PROFILE=my-dev-account npx cdk deploy
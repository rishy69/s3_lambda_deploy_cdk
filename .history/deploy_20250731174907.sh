set -e

source .venv/bin/activate

pip install -r requirements.txt

AWS_PROFILE=my-dev-account npx cdk deploy
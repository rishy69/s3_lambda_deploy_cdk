set -e

source .venv/bin/activate

pip

AWS_PROFILE=my-dev-account npx cdk deploy
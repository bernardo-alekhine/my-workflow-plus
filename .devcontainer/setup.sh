set -e # Exit immediately if a command fails
echo "--- Starting Setup ---"
# Install Python requirements
pip install -r requirements/dev-requirements.txt
# Configure local git buffer/settings
git config --global http.postBuffer 524288000
git config --global --add safe.directory /workspaces/my-workflow-plus
pre-commit install
# Any other setup steps
echo "---- Setup complete! ---"

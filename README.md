# Technical-Writer

## Overview
Technical-Writer automates the updating of README files in response to code changes. Triggered by merged PRs, it leverages OpenAI's API for content generation and LangChain for orchestrating the automation process.

## Features
- Automates README updates upon PR merges using AI.
- Utilizes GitHub Actions for workflow automation.
- Integrates with LangChain to manage AI interactions and logic flow.
- Employs OpenAI's API for context-aware content generation.

## Current Status
This project is in the early stages of development. Further instructions will be provided as the implementation progresses.

## Getting Started
To get started with this project, follow these steps:
1. Copy the `.env.example` file and fill in your GitHub and OpenAI credentials.
2. Install the required Python dependencies by running `pip install -r requirements.txt`.
3. Set up the GitHub Action by following the instructions in `.github/workflows/update-readme.yaml`.

## Testing
You can run informal tests on the GitHub API functions by executing `python test_github_api.py`.

## Contributing
Contributions are welcome. Please submit any issues or pull requests through GitHub.

## License
This project is released under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements
- OpenAI for providing the API used for generating content.
- GitHub for hosting and automation capabilities.
- LangChain for the automation framework used to streamline AI operations.
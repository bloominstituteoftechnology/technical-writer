import os
from openai import OpenAI
from github import Github  # Changed from github_api to PyGithub
# from dotenv import load_dotenv  # Keeping load_dotenv for local testing purposes, if necessary
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

# Load environment variables
# load_dotenv()

def format_data_for_openai(diffs, file_content, commit_messages):
    # Combine the changes into a string with clear delineation.
    changes = '\n'.join([
        f'File: {file_path}\nDiff: \n{diff}\n'
        for file_path, diff in diffs.items()
    ])

    # Combine all commit messages
    commit_messages = '\n'.join(commit_messages) + '\n\n'

    # Construct the prompt with clear instructions for the LLM.
    prompt = (
        "Please review the following code changes and commit messages from a GitHub pull request:\n"
        "Code changes from Pull Request:\n"
        f"{changes}\n"
        "Commit messages:\n"
        f"{commit_messages}"
        "Here is the current README file content:\n"
        f"{file_content}\n"
        "Consider the code changes and commit messages, determine if the README needs to be updated. If so, edit the README, ensuring to maintain its existing style and clarity.\n"
        "Updated README:\n"
    )

    return prompt

def call_openai(prompt):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # Correctly using the OPENAI_API_KEY
    try:
        # Construct the chat messages for the conversation
        messages = [
            {"role": "system", "content": "You are an AI trained to help with updating README files based on code changes."},
            {"role": "user", "content": prompt},
        ]

        # Make the API call to OpenAI chat interface
        response = client.chat_completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        return response.choices[0].message.content  # Correct attribute access
    except Exception as e:
        print(f"Error making OpenAI API call: {e}")

def main():
    g = Github(os.getenv('GITHUB_TOKEN'))  # Authenticate with GitHub using the provided GITHUB_TOKEN
    owner = os.getenv('OWNER')
    repo = os.getenv('REPO')
    repository = g.get_repo(f"{owner}/{repo}")
    file_info = repository.get_contents("README.md", ref="main")
    readme_content = file_info.decoded_content.decode('utf-8')

    # Example owner, repo, and PR number - replace with dynamic values as necessary
    pull_request_number = 3  # Example placeholder for dynamic PR number

    # Placeholder for fetching diffs and commit messages
    pull_request_diffs = {}  # This should be populated with actual diff data
    commit_messages = ["Initial commit"]  # Populate with actual commit messages

    # Format data for OpenAI prompt
    prompt = format_data_for_openai(pull_request_diffs, readme_content, commit_messages)

    # Call OpenAI to generate the updated README content
    updated_readme = call_openai(prompt)

    # For testing purposes
    print(updated_readme)

    # commit_message = "Proposed README update based on recent code changes."
    # try:
    #     pr_response = put_readme_contents(owner, repo, updated_readme, commit_message, sha)
    #     print("README updated successfully.")
    # except Exception as e:
    #     print(f"Failed to update README: {e}")

    ####################################
    # Langchain implementation

    # Construct the chat prompt template
    # prompt_template = ChatPromptTemplate(readme_content, pull_request_diffs, commit_messages)

    # Wrap the functions with RunnableLambda
    # format_data_for_openai = RunnableLambda(format_data_for_openai)
    # call_openai = RunnableLambda(call_openai(prompt))

    # chain = call_openai

    # print(chain.run())

if __name__ == '__main__':
    main()

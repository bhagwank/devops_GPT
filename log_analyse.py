import openai
import os

# Initialize OpenAI API Key
#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = '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'
def analyze_log(log_content):
    """Analyzes the CI log using OpenAI GPT-4 to generate debugging suggestions."""
    
    if not log_content.strip():
        return "No logs to analyze."
    # Create a prompt with the CI log content
    prompt = f"""
    I am debugging a CI pipeline for an embedded software project. Here's the error log:

    {log_content}

    Can you provide detailed suggestions to fix this issue, along with explanations and any relevant links to documentation or resources?
    """

    # Make the API request to GPT-4
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=500,  
        temperature=0.5,  
    )
    
    return response.choices[0].text.strip()

def main():
    # For demonstration, we assume the log content is coming from a file or API
    log_file_path = 'result.log'
    
    with open(log_file_path, 'r') as file:
        log_content = file.read()
    
    # Get suggestions from GPT
    suggestions = analyze_log(log_content)
    
    # Print the suggestions
    print("AI-generated debugging suggestions:\n")
    print(suggestions)

if __name__ == "__main__":
    main()

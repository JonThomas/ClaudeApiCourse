Teaching myself to use the Claude API, by going through the couse "Claude with the Anthropic API": https://anthropic.skilljar.com/claude-with-the-anthropic-api

Keywords:
* Claude AI
* Anthropic API
  * Sending requests and receiving responses
  * Using System prompts to instruct Claude to behave in certain ways
  * Using Temperature to get more deterministic or creative responses
  * Response streaming
* Prompt evaluation - a method used to test prompts before production
  * [Structured output](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), instead of the unsupported Prefilling and Stop sequences that is still used in the course(!) to get Claude to return raw data like JSON
  * Using Claude to generate test data
  * Using Graders, both model grader and code graders, to evaluate a response.
* Prompt engineering techniques
  * Be clear and direct: Use simple language; Use instructions, not questions
  * Being spesific: Provide a guildeline/ steps to direct the model
  * Provide structure by using XML tags
  * Provide examples (Here: By taking a great response from Claude and using it as an example, wrapping it in XML comments)
* Jupyter notebooks
* Python
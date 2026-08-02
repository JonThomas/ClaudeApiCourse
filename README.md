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
* Tool use
  * JSON schemas used to tell Claude about local tools, and how to implement the tools
  * Fine grained tool calling
     * fine_grained = True <---- Claude will stream large json responses back to our server immediately, without waiting to check if Claude actually produces valid JSON
  * Text editor tool: Built into Claude
     * Gives Claude ability to do most any text editing operations 
     * **Updated code to use supported model claude-sonnet-4-5**
* Jupyter notebooks
* Python
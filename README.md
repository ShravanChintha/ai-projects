# AI Learning Projects

A personal repository dedicated to exploring and mastering the latest AI technologies through hands-on projects and experiments.

## 🎯 Purpose

This repository serves as a learning playground to:
- Stay current with cutting-edge AI technologies and trends
- Build practical projects using state-of-the-art AI tools and frameworks
- Develop skills in modern AI development practices
- Experiment with various AI models, APIs, and platforms
- Document learnings and best practices

## 🚀 Focus Areas

### Core AI Technologies
- **Large Language Models (LLMs)**: OpenAI, Anthropic Claude, Google Gemini, GitHub Models
- **AI Frameworks**: LangChain, Agent Framework, Azure AI Foundry
- **Model Fine-tuning**: Training and customization techniques
- **Embeddings & Vector Databases**: Semantic search and retrieval

### AI Application Development
- **Agentic Systems**: Building autonomous AI agents
- **RAG (Retrieval-Augmented Generation)**: Context-aware AI applications
- **Multi-Agent Workflows**: Orchestrating complex AI systems
- **Chat Applications**: Conversational AI interfaces
- **AI Evaluation**: Testing and measuring AI application performance

### Practical Skills
- Prompt engineering and optimization
- Model selection and deployment
- AI observability and tracing
- Cost optimization strategies
- Production-ready AI systems

## 📁 Project Structure

Each project in this repository will include:
- Clear objectives and learning goals
- Implementation code with comments
- Documentation of key concepts
- Challenges faced and solutions
- Performance metrics and insights

## 🛠️ Technologies & Tools

- **Languages**: Python, TypeScript/JavaScript, .NET
- **AI Platforms**: Azure AI Foundry, GitHub Models, OpenAI
- **Development Tools**: VS Code, AI Toolkit, Jupyter Notebooks
- **Version Control**: Git & GitHub

## 📚 Learning Approach

1. **Explore**: Research and understand new AI technologies
2. **Implement**: Build working projects and prototypes
3. **Experiment**: Test different approaches and configurations
4. **Document**: Record learnings, insights, and best practices
5. **Iterate**: Continuously improve and expand knowledge

## 🎓 Progress Tracking

Projects will be organized by complexity and topic area:
- 🟢 **Beginner**: Foundational AI concepts and basic implementations
- 🟡 **Intermediate**: More complex applications and integrations
- 🔴 **Advanced**: Sophisticated systems and cutting-edge techniques

## 💡 Getting Started

Each project folder contains:
- `README.md` - Project overview and setup instructions
- Source code and implementation files
- Requirements and dependencies
- Usage examples and demonstrations

## 🔄 Continuous Learning

This repository will evolve as new AI technologies emerge. Regular updates will include:
- New project implementations
- Updated frameworks and libraries
- Latest AI trends and techniques
- Performance improvements and optimizations

## 📝 Notes

This is a personal learning journey. Projects may be experimental and are intended for educational purposes rather than production deployment.

---

**Last Updated**: January 2026

## Day 1 — Ollama on macOS (2026-01-30)

**Summary**

Installed and tested Ollama locally on macOS. Tried starting the server and ran basic checks to verify what's running and reachable on port 11434.

**Commands run / useful checks**

- Install (Homebrew):

```bash
brew install ollama
```

- Alternative install (one-liner):

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

- Start server (foreground):

```bash
ollama serve
```

- Check running Ollama instances:

```bash
ollama ps
```

- Check port 11434 for listeners:

```bash
lsof -nP -iTCP:11434 -sTCP:LISTEN
```

- Quick HTTP health check:

```bash
curl -i http://localhost:11434/
```

**Observed results (notes)**

- `ollama serve` exited with code 1 in my terminal during initial attempt — check the terminal logs where you started it for error details.
- `ollama ps` returned successfully (shows active processes/containers managed by Ollama).
- If nothing is listening on 11434, use `lsof` to find conflicting processes and `ps -p <PID>` to inspect them.

**Troubleshooting steps taken / recommendations**

- Inspect the terminal output where `ollama serve` was run for stack traces or permission errors.
- Ensure Ollama has proper permissions (macOS may require approving network access in Security & Privacy).
- Restart the server in foreground to capture logs; use `Ctrl+C` to stop.
- Kill any conflicting process using the port with `kill <PID>` (or `kill -9 <PID>` if needed).
- Confirm model availability with `ollama list` and test with `ollama run <model>`.

**Next steps**

- Run the `lsof` and `curl` checks to confirm service state.
- Capture and paste any error logs from `ollama serve` if further help is needed.
- Try pulling a small model (`ollama pull <model>`) and run it to verify end-to-end functionality.

---

**Last Updated**: January 30, 2026


## Day 2 — Programmatic access to Ollama (2026-01-31)

**Summary**

Created `chat.py` to access Ollama programmatically via the `ollama` Python client. The script is a simple REPL that sends user input to a model and prints responses.

**File added**

- `chat.py` — basic example using the `ollama` Python package to call a model in a loop.

**How to run**

```bash
python3 chat.py
# type messages, then 'exit' to quit
```

**Notes**

- Replace the `model` string in `chat.py` with an available model from `ollama list` if needed.
- Ensure your Ollama server/daemon is reachable (run `ollama serve` locally or use the configured client settings).
- Consider adding error handling and streaming support next.

---

**Last Updated**: January 31, 2026



## Day 3 — Streamlit UI for Ollama (2026-02-01)

**Summary**

Built a small Streamlit UI (`app.py`) to interact with Ollama programmatically. The app demonstrates a simple chat interface, retains chat history in the session, and includes basic error handling.

**What changed**

- Added a Streamlit-based chat frontend in `app.py` that keeps a running history of messages.
- The app uses the `ollama` Python client to send user messages to a model and display responses.
- Added a simple form with a submit button to avoid accidental immediate requests on every keystroke.

**How to run (Day 3)**

Make sure dependencies are installed (see `requirements.txt`). Then run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

**Notes & next steps**

- Replace the `model` string in `app.py` with an available model from `ollama list` if needed.
- Consider adding streaming responses, richer error handling, and authentication for remote Ollama setups.

---

**Last Updated**: February 01, 2026


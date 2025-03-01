# Smart Documentation & Code Explanation

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
  - [Model Selection](#model-selection)
  - [Chat Levels](#chat-levels)
  - [Task Selection](#task-selection)
  - [Interactive Chatbot](#interactive-chatbot)
  - [Code Visualization](#code-visualization)
  - [Performance Analysis](#performance-analysis)
- [Configuration](#configuration)
- [Future Enhancements](#future-enhancements)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributors](#contributors)
- [Contact & Support](#contact--support)

## Overview
Smart Documentation & Code Explanation is an AI-powered application designed to help developers automatically generate clear and detailed documentation for codebases. The tool also provides insights into optimization, bug detection, security vulnerability analysis, and best practices, making technical details more accessible to developers at all levels.

## Features
- **Code Explanation:** AI-generated explanations tailored to different experience levels (Beginner, Intermediate, Expert).
- **Optimization Suggestions:** AI recommendations for improving performance, memory management, and readability.
- **Bug Detection and Fixes:** Automated analysis of potential issues with suggested corrections.
- **Security Vulnerability Analysis:** Detection of security risks and suggestions for safer coding practices.
- **Best Practices Recommendations:** Guidelines for maintainability and clean code principles.
- **Interactive Chatbot:** Users can interact with Nebby, the AI assistant, for real-time code analysis.
- **Code Visualization:**
  - Generates flowcharts based on Python Abstract Syntax Trees (ASTs).
  - Uses Cytoscape.js for interactive graph visualization.
  - Supports conditional structures, loops, and function calls.
  - Includes traversal animations to highlight execution paths dynamically.
  - Allows full-screen toggling for better clarity.
- **Performance Analysis:** Compares optimized and unoptimized code execution.
- **Multi-Model Support:** Choose between OpenAI's GPT-4o and Hugging Face’s DeepSeek-R1 for varied insights.
- **Customizable Output:** Users can export explanations and reports in Markdown or PDF format.
- **Integration-Friendly:** Future-ready integration with VS Code and Jupyter Notebooks.
- **Real-Time Code Performance Visualization:**
  - Runs optimized and unoptimized code in parallel.
  - Tracks CPU usage, memory consumption, and execution time.
  - Uses Streamlit and Plotly to display real-time graphs.
  - Helps developers understand the impact of optimizations.

## Technologies Used
- **Frontend:** Streamlit (for UI/UX)
- **AI Models:**
  - OpenAI's GPT-4o
  - Hugging Face's DeepSeek-R1
- **Libraries & APIs:**
  - `langchain_openai` for GPT-based responses
  - `langchain_huggingface` for Hugging Face model integration
  - `dotenv` for environment variable management
  - `matplotlib`, `graphviz` for visualization
  - `psutil`, `plotly`, `pandas`, `threading` for performance analysis and real-time visualization
- **Visualization:** Custom-built visual module for generating flowcharts and performance analysis

## Installation & Setup
### Prerequisites
- Python 3.8+
- A Hugging Face API token
- An OpenAI API key (if using GPT-4o)
- Required dependencies installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/smart-docs.git
   cd smart-docs
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your API keys:
   ```plaintext
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```
5. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage
### Model Selection
Users can select between **GPT-4o** and **DeepSeek-R1** in the sidebar to tailor responses to their needs.

### Chat Levels
Choose an experience level to get explanations that match your expertise:
- **Beginner** – Simple explanations with analogies.
- **Intermediate** – More technical breakdowns.
- **Expert** – In-depth, detailed analysis.

### Task Selection
Pick from various tasks like:
- Code explanation
- Performance optimization
- Bug detection
- Security analysis
- Best practices enforcement

### Interactive Chatbot
Nebby, the AI assistant, provides real-time code analysis and helps answer queries dynamically.

### Code Visualization
- **AST-Based Flowchart Generation**: Converts Python code into an Abstract Syntax Tree (AST) and visualizes the control flow.
- **Interactive Graphs**: Uses Cytoscape.js to render interactive, clickable nodes representing code structures.
- **Execution Path Highlighting**: Clicking on a node highlights its execution path for better understanding.
- **Loop and Condition Representation**: Different shapes and colors for function calls, loops, and conditional statements.
- **Full-Screen Mode**: Users can expand the visualization for better readability.

### Performance Analysis
Compare optimized and unoptimized code execution for efficiency insights.

## Configuration
- Modify the `.env` file to set up API tokens.
- Adjust logging and debugging levels in `config.py`.
- Customize UI settings in `main.py`.

## Future Enhancements
- Support for more AI models.
- Additional visualization methods.
- Exportable documentation in Markdown/PDF formats.
- Integration with VS Code and Jupyter Notebooks and other codebases.
- Collaboration features for team-based documentation.

## Troubleshooting
- **Issue:** Dependencies not installing.
  - **Solution:** Run `pip install --upgrade pip` and retry.
- **Issue:** API keys not working.
  - **Solution:** Check `.env` file and ensure keys are valid.
- **Issue:** Streamlit not launching.
  - **Solution:** Ensure you are in the correct virtual environment and try `streamlit run main.py` again.

## License
This project is licensed under the MIT License.

## Contributors
- [Harii2K4]
- [KairavDeepeshwa]
- [saadhvi-r28]
- [Sakthisudarsh1206]
- [SarathChander1]
- [Sjay06]




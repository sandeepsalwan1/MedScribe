<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">MEDSCRIBE</h1></p>
<p align="center">
	<em>Empowering Healthcare with Seamless Documentation Automation.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/sandeepsalwan1/AnimalCare?style=flat&logo=opensourceinitiative&logoColor=white&label=License&color=0080ff" alt="MIT License">
	<img src="https://img.shields.io/github/last-commit/sandeepsalwan1/MedScribe?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/sandeepsalwan1/MedScribe?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/sandeepsalwan1/MedScribe?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

MedScribe is an innovative open-source project designed to streamline healthcare documentation by automating medical form filling and coding. Utilizing advanced speech recognition and machine learning technologies, MedScribe accurately transcribes spoken medical notes and extracts critical data, enhancing efficiency for healthcare professionals. This solution is ideal for medical facilities looking to reduce administrative burdens and improve data accuracy in patient care documentation.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a microservices architecture with components like `MedicalCopilot/server/main.py` for backend API processing.</li><li>Integrates with external APIs such as AWS Comprehend Medical and Google Web Speech API.</li><li>Employs Docker for environment management, as seen in `MedicalCopilot/server/Dockerfile`.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Adheres to modern Python practices with configuration files like `pyproject.toml` for dependency management.</li><li>Uses `pytest` for testing, ensuring code reliability.</li><li>Structured and modular codebase facilitating maintenance and scalability.</li></ul> |
| 📄 | **Documentation** | <ul><li>Documentation includes installation and usage commands for `pip`, `poetry`, and `docker`.</li><li>Code comments and README files provide guidance on setup and operation.</li><li>Documentation is version-controlled within the repository, ensuring it evolves with the codebase.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with multiple external services like AWS, Google APIs, and Deepgram via `MedicalCopilot/multionapi.py` and `MedicalCopilot/server/voice.py`.</li><li>Supports HTTP communication through libraries like `aiohttp` and `requests`.</li><li>Capable of handling complex data processing and machine learning tasks with `scikit-learn` and `numpy`.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Highly modular design with separate components for API handling, data processing, and service integration.</li><li>Scripts like `voice_streaming.py` are designed for specific tasks, enhancing modularity.</li><li>Dependency management handled via `poetry`, isolating project environments effectively.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Uses `pytest` for comprehensive testing, as specified in test commands.</li><li>Test configurations are easily manageable through dependency files like `pyproject.toml`.</li><li>Continuous integration likely supported though not explicitly mentioned in the provided details.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized for performance with the use of efficient libraries like `numpy` and `scipy`.</li><li>Performance critical operations are handled through specialized APIs and services.</li><li>Asynchronous programming support with `aiohttp` for improved scalability and efficiency.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Utilizes `grpcio` for secure communication between services.</li><li>Dependencies like `google-auth` ensure secure authentication mechanisms.</li><li>Security practices likely include secure handling of API keys and sensitive data, though specifics are not detailed.</li></ul> |

---

## 📁 Project Structure

```sh
└── MedScribe/
    ├── MedicalCopilot
    │   ├── multionapi.py
    │   ├── scripts
    │   └── server
    ├── README.md
    └── requirements.txt
```


### 📂 Project Index
<details open>
	<summary><b><code>MEDSCRIBE/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Defines the specific versions of libraries and dependencies required for the project, ensuring compatibility and stability across different development environments<br>- It includes libraries for HTTP communication, data manipulation, machine learning, and visualization, crucial for the project's functionality and performance.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- MedicalCopilot Submodule -->
		<summary><b>MedicalCopilot</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/MedicalCopilot/multionapi.py'>multionapi.py</a></b></td>
				<td>- Integrates with the MultiOn client and agentops services to automate form filling on a healthcare platform<br>- It initializes a session without auto-start, sets specific tags, and processes a command to populate a mental health support plan form with predefined data, enhancing operational efficiency in medical documentation.</td>
			</tr>
			</table>
			<details>
				<summary><b>scripts</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/MedicalCopilot/scripts/pyproject.toml'>pyproject.toml</a></b></td>
						<td>- Manages dependencies and settings for the MedicalCopilot's "amina" script, ensuring compatibility and streamlined setup<br>- It specifies Python version, essential libraries like Click and Requests, and additional script-specific dependencies such as the Deepgram SDK and PyAudio, facilitating the script's integration and functionality within the broader project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/MedicalCopilot/scripts/voice_streaming.py'>voice_streaming.py</a></b></td>
						<td>- Enables real-time transcription of audio through the Deepgram API, collecting spoken sentences into manageable chunks<br>- It integrates signal handling for graceful shutdowns and communicates with a local server to process transcribed text<br>- The script is configurable via environment variables and command-line options, facilitating batch processing adjustments and API key management.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>server</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/MedicalCopilot/server/voice.py'>voice.py</a></b></td>
						<td>- Voice.py serves as the speech recognition module within the MedicalCopilot's server architecture, enabling the system to transcribe spoken commands from users<br>- It utilizes the Google Web Speech API to convert speech from the microphone input into text, enhancing user interaction by processing verbal inputs effectively.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/MedicalCopilot/server/main.py'>main.py</a></b></td>
						<td>- MedicalCopilot's server/main.py serves as the backend API for processing medical text<br>- It utilizes AWS Comprehend Medical to extract ICD-10 codes and symptoms from text inputs, facilitating automated medical coding and symptom identification<br>- Additionally, it integrates with the MultiOn client for specific automated actions based on the medical findings.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/MedicalCopilot/server/pyproject.toml'>pyproject.toml</a></b></td>
						<td>- Defines the configuration and dependencies for the server component of the MedicalCopilot project<br>- It specifies the server's version, dependencies on libraries like FastAPI for web framework, Boto3 for AWS integration, and Pydantic for data validation, ensuring the server can handle web requests and interact with other services efficiently.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/sandeepsalwan1/MedScribe/blob/master/MedicalCopilot/server/Dockerfile'>Dockerfile</a></b></td>
						<td>- Establishes the environment for the MedicalCopilot server by setting up a Docker container with Python and necessary dependencies managed via Poetry<br>- It configures the server to run a FastAPI application on port 8000, ensuring all project dependencies are correctly installed and the application is ready for deployment and execution.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with MedScribe, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip, Poetry
- **Container Runtime:** Docker


### ⚙️ Installation

Install MedScribe using one of the following methods:

**Build from source:**

1. Clone the MedScribe repository:
```sh
❯ git clone https://github.com/sandeepsalwan1/MedScribe
```

2. Navigate to the project directory:
```sh
❯ cd MedScribe
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry install
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t sandeepsalwan1/MedScribe .
```




### 🤖 Usage
Run MedScribe using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/sandeepsalwan1/MedScribe/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/sandeepsalwan1/MedScribe/issues)**: Submit bugs found or log feature requests for the `MedScribe` project.
- **💡 [Submit Pull Requests](https://github.com/sandeepsalwan1/MedScribe/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/sandeepsalwan1/MedScribe
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/sandeepsalwan1/MedScribe/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=sandeepsalwan1/MedScribe">
   </a>
</p>
</details>

---

## 🎗 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT/). For more details, please refer to the [LICENSE](./LICENSE) file.


---

# CSV Agent Project

Sample to be able to query a CSV file to find answers.

# How to setup

Install the required Python version.

```sh
pyenv install 3.11.5
```

Set the local python version

```sh
pyenv local 3.11.5
```

Create a virtual environment for the project

```sh
pyenv virtualenv 3.11.5 csv-agent-env
```

Active the virtual environment

```sh
pyenv activate csv-agent-env
```

Install the dependencies

```sh
pip install -r requirements.txt
```

Set the OpenAI API key

```sh
export OPENAI_API_KEY=sk-your-open-ai-key-here
```

Run the program

```sh
python csv-rag.py
```

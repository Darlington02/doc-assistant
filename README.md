
# LangChain Documentation Helper

A repository for learning LangChain by building a generative ai application.

This is a web application using Pinecone as a vectorstore to answer questions about LangChain 
(sources from LangChain official documentation). 



![Logo](https://github.com/emarco177/documentation-helper/blob/main/static/banner.gif)
[![udemy](https://img.shields.io/badge/LangChain%20Udemy%20Course-%2412.99-green)](https://www.udemy.com/course/langchain/?couponCode=LANGCHAINCD8C0B4060)

## Tech Stack
Client: Streamlit

Server Side: LangChain 🦜🔗

Vectorstore: Pinecone 🌲

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PINECONE_API_KEY`
`OPENAI_API_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/emarco177/documentation-helper.git
```

Go to the project directory

```bash
  cd documentation-helper
```

Download LangChain Documentation
```bash
  mkdir langchain-docs
  wget -r -A.html -P langchain-docs  https://api.python.langchain.com/en/latest
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  streamlit run main.py
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```


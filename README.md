
## Introduction

This repository contains a project for building a chatbot using Azure AI Foundry with the Phi-3 model and Streamlit. The chatbot leverages the Phi-3-mini-128k language model developed by Microsoft to provide advanced AI capabilities in a compact form.

## Features

* Utilizes the Phi-3-mini-128k language model from Microsoft.
* Built with Streamlit for an interactive and user-friendly interface.
* Deployed on Azure Web App for scalability and reliability.
* Customizable parameters such as temperature, top_p, and max_length for fine-tuning the chatbot's responses.
* Tracks token usage to monitor API consumption.

## Files

* `app.py`: Main application file that sets up the Streamlit interface, handles user input, and communicates with the Phi-3 model API.
* `requirements.txt`: Lists the dependencies required for the project, including Streamlit and python-dotenv.
* `.github/workflows/main_phi3.yml`: GitHub Actions workflow for building and deploying the application to Azure Web App.

## Setup

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your Azure Web App and obtain the necessary credentials.
4. Update the API key in `app.py` with your actual API key.
5. Run the application locally using `streamlit run app.py`.

## Deployment

The project includes a GitHub Actions workflow for automated deployment to Azure Web App. The workflow is defined in `.github/workflows/main_phi3.yml` and includes steps for building the application, creating a virtual environment, installing dependencies, and deploying to Azure.

## Usage

1. Access the deployed application through the Azure Web App URL.
2. Interact with the chatbot by entering your queries in the input field.
3. Adjust the parameters in the sidebar to customize the chatbot's responses.
4. Monitor the token usage to keep track of API consumption.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

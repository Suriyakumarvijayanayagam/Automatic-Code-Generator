# Code Comment Generator using Streamlit, OpenAI API, and SpeechRecognition

## Introduction

The Code Comment Generator is a web application built using Streamlit, OpenAI API, and SpeechRecognition. It allows users to input their code and receive AI-generated comments for the code snippets. The application offers both text input and voice recognition options for ease of use.

## Features

- **Code Input:** Users can manually enter their code snippets in the text area provided.
- **Voice Recognition:** Users can use voice commands to input their code using the microphone.
- **Code Highlighting:** The app detects the programming language and highlights the code accordingly.
- **AI-generated Comments:** The app utilizes OpenAI API to generate helpful comments for the provided code.
- **AI Model Selection:** Users can choose from different AI models for comment generation.
- **Comment Saving:** The app provides an option to save the generated comments to a file for future reference.
![] (ccg 1.png)

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain the necessary API key for OpenAI API and set it as `openai.api_key` in the code.
4. Run the application using `streamlit run app.py`.
5. Access the app in your browser at [http://localhost:8501](http://localhost:8501).

## Dependencies

- Streamlit
- OpenAI
- SpeechRecognition
- Pygments
- PyAudio
- Google Cloud Speech-to-Text

## Acknowledgments

The Code Comment Generator app is inspired by the OpenAI GPT-3.5 Playground.

## Contributions

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please contact me.

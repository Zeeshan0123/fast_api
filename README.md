# Story Generation API with FastAPI and LLaMA
 
This repository contains an API for generating personalized short stories based on user inputs such as mood, story type, theme, length, and more. The API leverages a LLaMA language model to create engaging, imaginative stories for kids, along with illustrations using FLUX AI.

## Features
- **Personalized Story Generation:** Generate short stories based on mood, theme, and user-provided details. <br />
- **Page-by-Page Format:** Stories are structured in a 7-page format, each with one paragraph. <br />
- **Image Generation:** Generate story-related images based on scene descriptions, using the FLUX AI model.<br />
- **Customizable Story Elements:** Users can input their mood, story type, theme, and specific details about characters or scenes.<br />

## Technologies Used
- **FastAPI:** The framework used to build the API.
- **LLaMA 3.1 Model:** Used for generating the story content.
- **FLUX AI:** Used for generating illustrations based on the story.
- **Pydantic:** Used for validating request models.
- **Langchain:** Used to manage prompts and chains for the LLaMA model.

## How It Works
1. **User Inputs:** The user provides details like mood, story type, theme, length, and number of scenes.
2. **Story Generation:** The model generates a 7-page story based on the inputs.
3. **Image Generation:** For each scene, an illustration is generated based on the story progression using FLUX AI.
4. **Response:** The API returns the complete story along with the generated images.

## Installation

Follow the steps below to set up and run the project:

### 1. Clone the Repository
 ```bash
git clone https://github.com/yourusername/story-generation-api.git
cd story-generation-api
```
### 2. Install Dependencies
 ```bash
pip install -r requirements.txt
```
### 3. Set Environment Variables
Ensure you have your FAL_KEY ready to use the FLUX AI API.
 ```bash
export FAL_KEY='your_fal_key'
```
### 4. Run the API
Run the FastAPI server locally:
 ```bash
uvicorn main:app --reload
```
By default, the API will run on http://127.0.0.1:8000.

## API Endpoints
### 1. /generate_story/ (POST)
Generates a story and accompanying illustrations based on user inputs.
```json
{
  "mood": "Happy",
  "story_type": "Adventure",
  "theme": "Friendship",
  "length": 500,
  "num_scenes": 3,
  "txt": "A young boy and his magical pet dragon go on an adventure."
}
```











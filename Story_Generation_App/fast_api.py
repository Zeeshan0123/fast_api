from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os
import fal_client

# FastAPI app
app = FastAPI()

# Set the environment variable
os.environ['FAL_KEY'] = ''

# Request body model
class StoryRequest(BaseModel):
    mood: str
    story_type: str
    theme: str
    length: int
    num_scenes: int
    txt: str

# Initialize the LLM
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path="natsumura-storytelling-rp-1.0-llama-3.1-8B.Q3_K_M.gguf",
    temperature=0.3,
    max_tokens=2000,
    top_p=1,
    n_ctx=1024,
    callback_manager=callback_manager,
    verbose=True,
)

# Create a prompt template
# system = """You are a helpful and creative assistant that specializes in generating engaging and imaginative stories for kids.
# Based on the user's provided mood, preferred story type, theme, age, and desired story length of 500-600 words, create a unique and captivating story.
# Always start with Story Title then generate a single story and dont ask for any feedback at the end just sign off with a cute closing inviting the reader 
# to create another adventure soon! 
# """

system = """You are a helpful and creative assistant that specializes in generating engaging and imaginative short storie for kids.
Based on the user's provided mood, preferred story type, theme, age, and desired story length of 500-600 words, create a unique and captivating story.
Always start with Story Title then generate a single story.Storie begin on Page 1(also mention the all pages headings in bold) and end on Page 7.
Total pages in storie are seven each page have one short paragraph and dont ask for any feedback at the end just sign off with a cute closing inviting the reader 
to create another adventure soon! 
"""

prompt_template = ChatPromptTemplate.from_messages([("system", system), ("human", "{text}")])

# FastAPI endpoint to generate the story
@app.post("/generate_story/")
async def generate_story(story_request: StoryRequest):
    story = f"""here are the inputs from user:
    - **Mood:** {story_request.mood}
    - **Story Type:** {story_request.story_type}
    - **Theme:** {story_request.theme}
    - **Details Provided:** {story_request.txt}
    """
    
    final_prompt = prompt_template.format(text=story)

    # Create the LLMChain
    # chain = LLMChain(llm=llm, prompt=prompt_template)
    chain = llm | prompt_template
    
    # try:
    #     response = chain.invoke(final_prompt)
    #     return {"story": response}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    response = chain.invoke(final_prompt)
    
    if not response:
        raise HTTPException(status_code=500, detail="Failed to generate the story")
    
    images = []
    for i in range(story_request.num_scenes):
        # image_prompt = f"Generate an image for Scene {i+1} based on this story: Mood: {story_request.mood}, Story Type: {story_request.story_type}, Theme: {story_request.theme}. Story: {response}"
        image_prompt = (
        f"Generate an image for Scene {i+1}. "
        f"This image should represent the details described in paragraph {i+1} of the story. "
        f"Mood: {story_request.mood}, Story Type: {', '.join(story_request.story_type)}, Theme: {story_request.theme}. "
        f"Story: {response} "
        f"Focus on the key elements in paragraph {i+1}."
        )
        handler = fal_client.submit(
            "fal-ai/flux/schnell",
            arguments={
                "prompt": image_prompt,
                "num_images": 1,
                "enable_safety_checker": True
            },
        )
        result = handler.get()
        image_url = result['images'][0]['url']
        images.append(image_url)
    
    return {
        "story": response,
        "images": images
    }
    


# image_prompt = (
#         f"Generate an image for Scene {i+1}. "
#         f"This image should represent the details described in paragraph {i+1} of the story. "
#         f"Mood: {mood}, Story Type: {', '.join(story_type)}, Theme: {theme}. "
#         f"Story: {response} "
#         f"Focus on the key elements in paragraph {i+1}."
#     )

import os
import streamlit as st
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import openai

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
persist_directory = "./chroma_db"

# Initialize OpenAI client
openai.api_key = api_key

# Streamlit app setup
st.title("Personalized Search Assistant for Wellness and Relaxation Media")
st.write("Enter your query to get personalized recommendations based on YouTube metadata.")

# Load the vector database
@st.cache_resource
def load_database():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    return Chroma(embedding_function=embeddings, persist_directory=persist_directory)

db = load_database()

# Define helper functions
def retrieve_chunks(query, vector_db, k=5):
    """Retrieve top k chunks from vector database based on query."""
    return vector_db.similarity_search(query, k=k)

def _get_document_prompt(docs):
    """Format documents for the OpenAI GPT model."""
    prompt = "\n"
    for i, doc in enumerate(docs):
        prompt += f"Content {i + 1}:\n"
        prompt += doc.page_content[:1000] + "\n\n"  # Truncate long documents for clarity
    return prompt

def generate_response(query, retrieved_docs):
    """Generate a response using OpenAI GPT."""
    formatted_context = _get_document_prompt(retrieved_docs)

    prompt = f"""
    ## SYSTEM ROLE
    You are an expert chatbot designed to provide actionable, insightful, and personalized advice on **Mindfulness**, **Relaxation**, and **Self-Help Techniques**. 
    Your answers must be based exclusively on the content provided in the `CONTEXT` section, which is derived from YouTube video metadata.

    ## USER QUESTION
    The user has asked: 
    "{query}"

    ## CONTEXT
    Here is the relevant content from YouTube video metadata:  
    '''
    {formatted_context}
    '''

    ## GUIDELINES
    1. **Accuracy**:  
       - Only use the content in the `CONTEXT` section to answer.  
       - Prioritize videos from the most relevant categories based on the user's query.
       - If the answer cannot be found, explicitly state: "The provided context does not contain this information."
       - Use actionable language to recommend techniques or videos for relaxation and mindfulness.

    2. **Transparency**:  
       - Reference the video title and include the link when recommending specific videos.  
       - Avoid generic statements like "mentioned in the context"; provide specific details.

    3.   **Actionable Advice**:  
       - Use practical steps, examples, or benefits to explain the techniques being recommended.  
       - Highlight **how** the technique can help the user based on their query.

    4. **Clarity**:  
       - Use simple, professional, and user-friendly language.  
       - Ensure the response is well-structured and formatted in Markdown for readability.  


    ## RESPONSE FORMAT
    Your response should follow this structure: 
    
    '''
    # [Custom Title Based on the Query]
    Provide a meaningful title based on the user’s query (e.g., "How to Relax and Sleep Better").

    ## Recommendations
    1. **[Technique Name]**: [Actionable and insightful advice—expand on the metadata to include how it can help the user, how to do it, and why it works].
    2. **[Another Technique Name]**: [Actionable advice—explain why it's useful and how it can be applied].

    ## Recommended Videos
    - **[Video Title 1]**: [Description from the context]. [Link]
    - **[Video Title 2]**: [Description from the context]. [Link]

    **Note**: If no relevant content exists, respond with: "The provided context does not contain this information."
    '''

    
    ## EXAMPLE RESPONSE
    If the query was: "How can I relax and sleep better?"  
    And the context included:  
    - Title: "Guided Sleep Meditation" - "A 10-minute guided meditation to help you sleep better."  
    - Title: "Breathing Exercises for Relaxation" - "Simple techniques for reducing stress."  
    
    The response should be:  
    '''
    # How to Relax and Sleep Better
    
    ## Recommendations
    1. **Guided Meditation**: Spend 10 minutes focusing on your breath and letting go of intrusive thoughts before bedtime. This practice can help calm your mind and prepare your body for restful sleep.  
    2. **Breathing Exercises**: Use simple techniques like the 4-7-8 breathing method to lower your heart rate, reduce anxiety, and transition into a relaxed state before sleeping.  
    
    ## Recommended Videos
    - **Guided Sleep Meditation**: A 10-minute guided meditation to help you sleep better. [Link](https://youtube.com/example1)  
    - **Breathing Exercises for Relaxation**: Simple techniques for reducing stress. [Link](https://youtube.com/example2)  
    
    **Note**: If no relevant content exists, respond with: "The provided context does not contain this information."
    '''
    """

    try:
        # Initialize the OpenAI client and use the old API
        client = openai.OpenAI()  # Old-style OpenAI client
        model_params = {
            'model': 'gpt-4',  # Specify your model
            'temperature': 0.7,
            'max_tokens': 4000,
            'top_p': 0.9,
            'frequency_penalty': 0.5,
            'presence_penalty': 0.6,
        }
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            **model_params
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {e}"


# User Input
query = st.text_input("Enter your query:")
if query:
    with st.spinner("Retrieving recommendations..."):
        retrieved_docs = retrieve_chunks(query, db, k=5)
        response = generate_response(query, retrieved_docs)  # No asyncio here for older API
    st.markdown(response)

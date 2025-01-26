# 🧘💆‍♂️ SerenityStreams ✨🎥
Relaxation and mindfulness video recommendations tailored to user's needs.

**Welcome to your Mindful Video Recommendation System!**
This project combines *YouTube metadata retrieval*, *natural language processing (NLP)*, and *semantic search* to provide personalized video recommendations. 

Designed to help users quickly discover **meaningful** and **actionable** content based on their queries.

---

## 📑 Table of Contents

1. [Project Overview](#/project-overview)
2. [Key Features](#/key-features)
3. [How It Works](#/how-it-works)
4. [Project Files](#-project-files)
5. [Requirements](#-requirements)
6. [Usage](#-usage)
7. [Why This System](#-why-this-system)
8. [Next Steps](#-next-steps)

---

## 📖 Project Overview

The system consists of **three main stages**:

1. **📊 Fetching YouTube Data**:
   - Queries YouTube API for videos across **6 curated categories**:  
     - 🧘 Mindfulness and Relaxation  
     - 📝 CBT and Self-Help  
     - 🤸‍♂️ Physical and Somatic Practices  
     - 📈 Productivity and Focus  
     - 🌙 Sleep and Rest  
     - 💖 General Well-Being  
   - Extracts metadata like video titles, descriptions, and links.  
   - Organizes the fetched data into a structured **PDF report** for reference.

2. **🛠️ Cleaning and Processing**:
   - **Data Cleaning**: Removes invalid content, ensures each chunk includes a valid title, description, and link.  
   - **Sanitizing and Filtering**: Only meaningful chunks with both descriptions and links are retained.  
   - **Embedding with LangChain and Chroma**:  
     - Text embeddings are created using OpenAI’s `text-embedding-3-large` model.  
     - A **vector database** is built for semantic search.

3. **💻 Building the Streamlit App**:
   - Allows users to input queries and retrieves relevant content from the **vector database**.  
   - Leverages OpenAI’s GPT-4 for generating actionable and insightful recommendations.  
   - Displays the most relevant videos with descriptions and links.

---

## ✨ Key Features

1. **🎯 Personalized Recommendations**:
   - Goes beyond traditional keyword searches by understanding the meaning behind queries.  
   - Example: A query like "I want to feel less stressed" may recommend:  
     - **10-Minute Guided Meditation** (Mindfulness and Relaxation)  
     - **Yoga for Stress Relief** (Physical and Somatic Practices).  

2. **🔍 Semantic Search**:
   - Uses vector embeddings to find videos based on meaning, even if they don’t match exact keywords.  

3. **📂 Curated Categories**:
   - Videos are grouped into predefined categories for a more organized experience.

---

## 🤔 How It Works

### Query Processing Pipeline:

1. **💬 User Input**:
   - The app collects a query like "How can I sleep better?"

2. **🔗 Semantic Search**:
   - The query is compared against the **vector database** using cosine similarity.  
   - Videos with relevant semantic meanings are prioritized.

3. **🧠 Response Generation**:
   - GPT-4 constructs a response, combining video metadata and actionable advice.

4. **📜 Results Display**:
   - Recommendations include video titles, descriptions, and direct links.

---

## 📂 Project Files

1. **`creating_youtube_data.ipynb`**:
   - Fetches metadata from the YouTube API based on predefined keywords and categories.  
   - Converts the data into a structured **PDF report**.

2. **`clean.ipynb`**:
   - Cleans and processes the data.  
   - Creates vector embeddings using LangChain and Chroma for semantic search.

3. **`app.py`**:
   - A **Streamlit application** for user interaction.  
   - Integrates the vector database and GPT-4 for personalized recommendations.

4. **`youtube_data.pdf`**:
   - A sample output showing organized video metadata.

5. **`presentation.pdf`**:
   - A presentation summarizing the project.
     
6. **`requirements.txt`**:
   - A list of Python dependencies required for the project.

---

## ⚙️ Requirements

1. **API Keys**:
   - YouTube API Key (add `OPENAI_API_KEY=your_openai_api_key` to `.env` file).  
   - OpenAI API Key (add `YOUTUBE_API_KEY=your_youtube_api_key`to `.env` file).  

2. **Dependencies**:
   - Python libraries: `streamlit`, `langchain`, `openai`, `fpdf`, `requests`.

3. **Environment Setup**:
   - Install dependencies:  
     ```bash
     pip install -r requirements.txt
     ```
---

## 🚀 Usage

1. **Run the App**:
   - Start the Streamlit app:
     ```bash
     streamlit run app.py
     ```

2. **Input Queries**:
   - Enter a question or topic, like "I want to improve my focus."

3. **View Recommendations**:
   - The app will display the most relevant videos, along with actionable advice and links.

---

## ⁉ Why This System?

Traditional YouTube searches may lack personalization, often showing generic or unrelated results, and capturing user's attention.  
This system ensures:
- **✅ Actionable Advice**: Recommendations come with context and clear guidance.
- **🎯 Personalization**: Videos tailored to the user's current needs.
- **⏳ Efficiency**: Saves time by providing focused, meaningful results.

---

## 🚧 Next Steps

- **🔄 Dynamic Video Fetching**:
  - Expanding the system to fetch new videos dynamically using the YouTube API.

- **🧠 NLP Enhancements**:
  - Processing and enhancing video descriptions to extract actionable insights and present user-focused recommendations.

- **📊 Improved Relevance Scoring**:
  - Integrating advanced NLP techniques to score the relevance of video content dynamically.

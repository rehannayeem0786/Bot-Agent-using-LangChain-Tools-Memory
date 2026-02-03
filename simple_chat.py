"""
SIMPLE CONVERSATIONAL CHATBOT
A beginner-friendly chatbot with search and memory
"""

from langchain_openai import ChatOpenAI
from langchain.tools import tool
import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# ============================================================================
# STEP 1: CREATE A SIMPLE SEARCH TOOL (Optional - can be used manually)
# ============================================================================

@tool(description="Search the web for information")
def websearch(query: str) -> str:
    """
    Search the web using DuckDuckGo
    Input: query (what to search for)
    Output: search results
    """
    try:
        url = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json"}
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        
        if data.get("Abstract"):
            return f"Found: {data['Abstract'][:300]}"
        else:
            return f"No detailed results for '{query}'"
    except:
        return f"Search error for '{query}'"

# ============================================================================
# STEP 2: CREATE THE LLM (Language Model)
# ============================================================================

def create_chatbot():
    """
    Create a simple chatbot with Open Router API using pure LLM (no agents)
    This is simpler and more reliable than agent-based approach
    """
    # Initialize the LLM (AI model)
    llm = ChatOpenAI(
        model="openai/gpt-3.5-turbo",
        temperature=0.7,  # More natural responses
        api_key=API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )
    
    return llm

# ============================================================================
# STEP 3: SIMPLE CHAT FUNCTION WITH MEMORY
# ============================================================================

def chat():
    """
    Main chat function - conversation loop with conversation history
    """
    print("\n" + "="*60)
    print("🤖 SIMPLE CHATBOT WITH MEMORY")
    print("="*60)
    print("\nType your questions and chat! Type 'exit' to quit.\n")
    
    # Create the chatbot
    llm = create_chatbot()
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit command
        if user_input.lower() == "exit":
            print("\nGoodbye! 👋\n")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Add to conversation history
        conversation_history.append(("user", user_input))
        
        # Build context - combine conversation history into a single message
        # This way the LLM understands the full conversation
        context_text = ""
        if len(conversation_history) > 1:
            for role, message in conversation_history[:-1]:
                if role == "user":
                    context_text += f"User: {message}\n"
                else:
                    context_text += f"Assistant: {message}\n"
        
        # Create the full message with context
        if context_text:
            full_message = context_text + f"User: {user_input}\nAssistant:"
        else:
            full_message = user_input
        
        try:
            # Get response from LLM
            response = llm.invoke(full_message)
            response_text = response.content.strip()
            
            # Add to history
            conversation_history.append(("assistant", response_text))
            
            print(f"Bot: {response_text}\n")
            
        except Exception as e:
            print(f"Error: {str(e)[:100]}\n")

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    chat()

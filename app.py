# app.py
import streamlit as st
from openai import OpenAI

# Streamlit App UI and Main Function
def main():
    """Main function to run the Streamlit app."""
    st.title("Meeting Preparation App")
    st.write("Generate detailed meeting briefs using OpenAI's GPT model.")

    # User input for OpenAI API key
    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")
    
    # Check if the API key is provided
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key.")
        st.stop()

    # Define a system prompt for meeting preparation
    SYSTEM_PROMPT = """
    You are an AI assistant helping sales professionals prepare for client meetings. 
    Your company specializes in cloud-based AI solutions that enhance efficiency, security, and scalability. 
    You solve problems like inefficient workflows, data security concerns, and scalability challenges for businesses in various industries.

    Based on the provided client information, generate a meeting preparation brief that includes:
    1. A brief company overview.
    2. Key industry trends relevant to our solutions.
    3. Potential pain points we could address.
    4. Specific talking points for the meeting.
    5. How our solutions align with their needs.
    """

    # User input for client information
    client_info = st.text_area("Client Information", placeholder="Enter details about the client company, industry, known challenges, etc.")

    # Check if client information is provided
    if st.button("Generate Meeting Brief"):
        if not client_info.strip():
            st.warning("Please enter client information.")
        else:
            with st.spinner("Analyzing client information..."):
                try:
                    # Initialize the OpenAI client
                    client = OpenAI(api_key=openai_api_key)

                    # Create the chat completion request
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": client_info}
                        ]
                    )

                    # Extract the generated content
                    meeting_brief = response.choices[0].message.content

                    # Display the generated meeting brief
                    st.subheader("Generated Meeting Brief")
                    st.write(meeting_brief)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
    

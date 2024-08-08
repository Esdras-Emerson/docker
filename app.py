import streamlit as st

def hello_word():
    return "Olá, familia! Eu amo vocês"

def main():
    st.write(hello_word())

if __name__ == "__main__":
    main()
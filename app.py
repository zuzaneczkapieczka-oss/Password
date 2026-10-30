import streamlit as st

# Password Test babes :3
st.set_page_config(
    page_title="Password test babes :3",
    page_icon="🍫",
    layout="centered",
)

# Kolory oryginalnego programu
BG = "#E9EEC9"
FG = "#000232"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {BG};
        color: {FG};
    }}
    h1, h2, h3, p, label, .stMarkdown {{
        color: {FG} !important;
    }}
    div.stButton > button {{
        background-color: {FG};
        color: {BG};
        border: 0;
        border-radius: 8px;
    }}
    div.stButton > button:hover {{
        background-color: #25275a;
        color: white;
        border: 0;
    }}
    div[data-testid="stTextInput"] input {{
        background-color: white;
        color: {FG};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Haslo Python Test")
st.write("Podaj haslo prosze.")

show_password = st.checkbox("Show Password :3")

with st.form("password_form"):
    password = st.text_input(
        "Hasło",
        type="default" if show_password else "password",
        label_visibility="collapsed",
        placeholder="Wpisz hasło tutaj...",
    )
    submitted = st.form_submit_button("Sprawdź hasło")

if submitted:
    if password == "czekolada":
        st.success("Gratulacje! Wkoncu ci sie kurwa udalo skurwysynie ^_^")
    elif password == "69":
        st.info("Czemu ta liczba? Sprobuj jeszcze raz! :(")
    elif password in ("Muehehe", "muehehe"):
        st.info("Co cie tak smieszy stara ruro?")
    elif password == "hehe":
        st.info("No slodkie ale to nie smieszne!")
    elif password == "help":
        st.info("Nie. ja nie twoja mamusia.")
    elif password == "/help":
        st.info("Haslo to: czekolada")
    elif password == "jakie jest haslo?":
        st.info("czekolada. Z malej litery.")
    elif password == "Oops! Zle haslo, sprobuj ponownie!":
        st.info("Haslo to: czekolada, DEBILU-")
    elif password == "czekolada, DEBILU-":
        st.info("NIE DOSLOWNIE!!!!")
    elif password == "TO CO MAM NAPISAC?":
        st.info("czekolada. TO NAPISZ, BEZ KROPKI, Z malej LITERY!!!!")
    else:
        st.error("Oops! Zle haslo, sprobuj ponownie!")

st.caption("Mały projekt do zabawy. Nie używaj prawdziwych haseł ani prywatnych danych.")

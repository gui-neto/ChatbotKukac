import json
import random
import streamlit as st

def read_json(file):
    content = file.getvalue()
    data = json.loads(content)
    return data

def get_answer(question, key):
    if question['tipo'] == 'multipla_escolha':
        text = question['texto']
        options = question['opcoes']
        random.shuffle(options)
        return st.radio(text, options, key=key)
    elif question['tipo'] == 'verdadeiro_falso':
        text = question['texto']
        options = ['Verdadeiro', 'Falso']
        random.shuffle(options)
        return st.radio(text, options, key=key)
    else:
        return st.text_input(question['texto'], key=key)
    
def check_answers(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def submit(user_answer, question):
    st.session_state.answers['resultados'].append({'pergunta': question['texto'], 'resposta': st.session_state[user_answer]})
    st.session_state.score += 1 if check_answers(st.session_state[user_answer], question['resposta_correta']) else 0
    st.session_state.index += 1

def build_file(answers):
    file = json.dumps(answers, indent=2, ensure_ascii=False)
    return file


if 'index' not in st.session_state:
    st.session_state.index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {'resultados': []}

st.title("CHATBOT KUKAC 🧠")

uploaded_file = st.file_uploader("Escolha um arquivo JSON", type=["json"])

if uploaded_file is not None:
    questions = read_json(uploaded_file)

    if st.session_state.index < len(questions['perguntas']):
        question = questions['perguntas'][st.session_state.index]

        with st.form('test'):
            answer = get_answer(question, question["id"])
            if st.session_state.index < len(questions['perguntas']) - 1:
                submitted = st.form_submit_button("Próxima pergunta", on_click=submit, kwargs=dict(user_answer=str(question["id"]), question=question))
            else:
                submitted = st.form_submit_button("Finalizar questionário", on_click=submit, kwargs=dict(user_answer=str(question["id"]), question=question))

    else:
        st.write("Fim do questionário.")
        st.session_state.index = 0
        st.session_state.answers['pontuacao'] = st.session_state.score

        json_string = build_file(st.session_state.answers)

        st.download_button(
            label='Baixar respostas',
            data=json_string,
            file_name='respostas.json',
            mime='application/json'
        )
else:
    st.session_state.index = 0
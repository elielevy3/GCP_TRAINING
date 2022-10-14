import streamlit as st
import pandas as pd
from random import sample


@st.cache()
def get_sample_question(data, nb_of_questions):
    return sample(range(1, len(data)), nb_of_questions)


st.title("WELCOME TO WEWYSE GCP ACE TRAINING !")

# get raw data
data = pd.read_csv("Evaluation_test.csv", sep=";")

# ask the user how many questions he wants
n = st.number_input('How many questions do you want ?', step=1, min_value=1, max_value=len(data))
st.write('You asked for ', n, ' questions.')

# get n questions
questions = get_sample_question(data, n)

submitted_answers = []
explanations = []

for i, question in enumerate(questions):

    # question number
    st.write("Question ", i + 1, " / ", n)

    # writing the question
    st.write(data["Question"][question], key=i)

    # writing options
    dico = {str(x) + " : " + str(data[x][question]): x for x in ['A', 'B', 'C', 'D', 'E'] if str(data[x][question]) != "nan"}
    options = [str(x) + " : " + str(data[x][question]) for x in ['A', 'B', 'C', 'D', 'E'] if str(data[x][question]) != "nan"]
    answer = st.radio('What is your answer ? ', options)
    submitted_answers.append(dico[answer])
    explanation = st.empty()
    explanations.append(explanation)
    st.write("-----------------------------------")

submitted = st.button(label="Submit answers")


if submitted:
    score = 0
    for i, answer in enumerate(submitted_answers):
        if data["result"][questions[i]] == answer:
            score += 1
            with explanations[i].container():
                st.write("Correct !")
                st.write(data["explanation"][questions[i]])
        else:
            with explanations[i].container():
                st.write("Wrong !")
                st.write("The correct answer was ", data["result"][questions[i]])
                st.write(data["explanation"][questions[i]])
    st.write("Final score : ", score, " / ", n)
    st.write("Accuracy percentage : ", round((score / n)*100, 3), " %")

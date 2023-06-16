from chapter_11.survey import AnonymousSurvey

# Define a question, and make survey.
question = "Which language did you first learn to code with: "
my_survey = AnonymousSurvey(question)
print("Enter 'q' at any time to quit")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show all survey responses
my_survey.show_responses()
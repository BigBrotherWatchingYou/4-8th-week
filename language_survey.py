#aaa
from survey import AnonymousSurvey

#create a question  
question = "What languague did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#show the answer and put it into storage
my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break   
    my_survey.store_response(response)  
#show the results of the survey
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

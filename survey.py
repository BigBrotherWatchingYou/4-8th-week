class AnonymousSurvey():
    def __init__(self, question):
        #store a question
        self.question = question
        self.responses = []
    
    def show_question(self):
        #show the survey
        print(self.question)
    
    def store_response(self, new_response):
        #show a single survey answer
        self.responses.append(new_response)
    
    def show_results(self):
        #show all the survey answers
        print("Survey results:")
        for response in self.responses:
            print('-' + response) 

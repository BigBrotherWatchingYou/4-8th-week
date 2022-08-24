import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    #Test aim at TestAnoymousSurvey

    def setUp(self):
        #Create a test object to use for test
        question =  "What languague did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        #test whether a single answer will be put into storage
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_sotre_three_responses(self):
        #test whether 3 answers will be storaged
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

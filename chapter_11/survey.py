

class AnonymousSurvey:
    """Collect anonymous answer to a survey question"""

    def __init__(self, question):
        """Store a question and prepare to store a response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show survey question"""
        print(self.question)

    def store_response(self,new_response):
        """Store a single response in survey responses"""
        self.responses.append(new_response)

    def show_responses(self):
        """Show all survey responses"""
        print("Survey responses: ")
        for response in self.responses:
            print(" - " + response.title())

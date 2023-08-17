from difflib import get_close_matches
import json

    
def get_best_match(user_question,questions):
    questions=[q for q in questions]
    matches=get_close_matches(user_question,questions,n=1,cutoff=0.6)

    if matches:
        return matches[0]


f=open("Chat/support_files/Brain.json")
brain=json.load(f)
f.close()


def chat_bot(user_input, knowledge=brain ):

    best_match=get_best_match(user_input,knowledge)

    if answer:=knowledge.get(best_match):
        return (answer)

    else:
        return ("I don't know the response. Can you teach me?")
                                


def new_ans(user_input, new_answer, knowledge=brain ):

    if new_answer.lower()!="skip":
        knowledge.update({user_input:new_answer})
                    
        with open("Chat/support_files/Brain.json","w") as file:
            json.dump(knowledge, file)
                
        return ('Thank you. I learnt something new.')




if __name__=='__main__':
    user_input=input("You: ")
    chat_bot(user_input)
   
    

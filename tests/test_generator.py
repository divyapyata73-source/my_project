from generator import generate_answer


question = "What places can I visit in Switzerland?"

context = """
Switzerland has several popular destinations including
Zurich, Lucerne, Interlaken, Montreux and Zermatt.

A suggested route is:
Zurich → Lucerne → Interlaken → Montreux → Zermatt.

Transportation includes trains, buses, boats,
mountain railways and cable cars.

Popular foods include cheese fondue, raclette,
rösti and Swiss chocolate.
"""


answer = generate_answer(question, context)


print("ANSWER GENERATION SUCCESSFUL")
print("-----------------------------")
print("Question:")
print(question)

print("\nGenerated Answer:")
print("=================")
print(answer)
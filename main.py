import pandas
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabets = {j["letter"]: j["code"] for (i, j) in student_data_frame.iterrows()}

user_input = input("Enter a word: ").upper()
nato_alphabet = [alphabets[a] for a in user_input]
print(nato_alphabet)

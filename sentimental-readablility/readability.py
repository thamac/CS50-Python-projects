from cs50 import get_string
from re import search


def calcGrade(text):
    totalLetters = 0
    totalWords = 1
    totalSentences = 0

    for i in text:
        if i.isalpha():
            totalLetters += 1
        if i.isspace():
            totalWords += 1
        if search("[.!?]", i):
            totalSentences += 1

    calcWords = 100 / totalWords
    l = calcWords * totalLetters
    s = calcWords * totalSentences

    grade = round(0.0588 * l - 0.296 * s - 15.8)

    return grade


def main():
    text = get_string("Text: ")

    grade = calcGrade(text)

    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


main()

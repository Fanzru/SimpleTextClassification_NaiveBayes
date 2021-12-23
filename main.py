import pandas as pd

columns = ['sent', 'class']

rows = [['This is my book', 'stmt'],
        ['They are novels', 'stmt'],
        ['have you read this book', 'question'],
        ['who is the author', 'question'],
        ['what are the characters', 'question'],
        ['This is how I bought the book', 'stmt'],
        ['I like fictions', 'stmt'],
        ['what is your favorite book', 'question']]

training_data = pd.DataFrame(rows, columns=columns)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(training_data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

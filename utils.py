import pandas

def load_data(file_path):
    return pandas.read_csv(file_path)

def rank_labels():
    file = "Base Risk Lexicon 2021 - Triggers.csv"
    df = load_data(file)

if __name__ == '__main__':
    rank_labels()
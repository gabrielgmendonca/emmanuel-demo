import pandas as pd

BOOK_DATASET = 'data/books_paragraphs.json'


def write_chapter(row):
    title = row['book_title']
    chapter = row['chapter_number']
    filename = f'chapter_{chapter}.txt'
    with open(f'data/{title}/{filename}', 'a') as f:
        f.write(row['paragraph_text'] + '\n')


if __name__ == '__main__':
    book_df = pd.read_json(BOOK_DATASET, orient='records')
    book_df = book_df[book_df['book_title'] == 'A caminho da Luz']
    book_df = book_df.drop_duplicates(
        ['book_title', 'book_author', 'chapter_number', 'chapter_name', 'paragraph_index']
    )
    book_df = book_df.reset_index(drop=True)
    book_df.apply(write_chapter, axis=1);

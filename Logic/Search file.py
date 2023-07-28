import os
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
from whoosh import index

def create_index(dir_path, index_dir):
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    schema = Schema(content=TEXT(stored=True))
    ix = create_in(index_dir, schema)
    writer = ix.writer()
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.txt'):  # Process text files
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                writer.add_document(content=content)
    writer.commit()

def search_files(index_dir, search_query, file_type=None):
    ix = open_dir(index_dir)
    searcher = ix.searcher()
    query_parser = QueryParser("content", ix.schema)
    query = query_parser.parse(search_query)

    # Apply the file type filter if provided
    if file_type:
        query = query_parser.parse(f"{search_query} AND {file_type}")

    results = searcher.search(query)
    return results

if __name__ == "__main__":
    directory_path = "/path/to/your/search_directory"
    index_directory = "index"
    create_index(directory_path, index_directory)

    while True:
        search_query = input("Enter your search query (or 'q' to quit): ").strip()
        if search_query.lower() == 'q':
            break

        file_type = input("Enter the file type (e.g., txt, c, py), or leave empty for all types: ").strip()
        file_type = file_type.lower() if file_type else None

        results = search_files(index_directory, search_query, file_type)

        print("Search results:")
        for result in results:
            print(result['content'])
            print('-' * 50)

import client

if __name__ == '__main__':
    # file_path = '../input_files/football.pdf'
    # file_name = input("Enter file name:")
    # print(file_path)
    # with open(file_path, 'rb') as f:
    #     file_content = f.read()
    # document_id = client.upload_document(file_content, file_name)
    # print(document_id)
    query = input()
    print(query)
    results = client.search_documents(query)
    print(results)
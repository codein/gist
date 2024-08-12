import os
from collections import defaultdict
from lunr import lunr

from api.utils import logger

WIKI_HOST = 'http://192.168.13.31:8080'

class LunrIndexer:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.documents = {}
        self.permalink_map = {}
        self.idx = None

    def set_documents(self, path):
        """Given a path return a list of documents."""
        for filename in os.listdir(path):
            if filename.endswith('.md'):

                file_path = os.path.join(path, filename)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    count_lines = len(lines)
                    chunk_size = 20
                    for chunk in range(0, count_lines, chunk_size):
                        chunk_lines = lines[chunk:chunk + chunk_size]
                        chunk_lines = [line.strip() for line in chunk_lines]
                        chunk_lines = [line for line in chunk_lines if line]
                        doc_chunk = ' '.join(chunk_lines)
                        perma_filename = filename.replace('.md', '')
                        chunk_id = f'{chunk}-{chunk + chunk_size}'
                        document_id = f'{perma_filename}:{chunk_id}'
                        document = {
                            'id': document_id,
                            'title': filename,
                            'body': doc_chunk,
                            'chunk_id': chunk_id,
                            'permalink': f'{WIKI_HOST}/#{perma_filename}'
                        }
                        self.documents[document_id] = document

        logger.info(f'Found {len(self.documents)} documents.')

    def set_lunr_index(self, dir_path):
        self.set_documents(dir_path)
        document_list = list(self.documents.values())

        self.idx = lunr(ref='id', fields=('title', 'body'), documents=document_list)
        logger.info('Created lunr index.')

    def search(self, query):
        """Given a query return a list of results."""
        results = self.idx.search(query)
        for result in results:
            result['match_data'] = result['match_data'].metadata
        return results


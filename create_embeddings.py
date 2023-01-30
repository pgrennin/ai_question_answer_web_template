import sys

from app.models.embeddings_service import EmbeddingsService

# if filename is present as commandline argument, use it as the filename to embed, else use the string 'ALL'
if len(sys.argv) > 1:
    filename_to_embed = sys.argv[1]
else:
    filename_to_embed = 'ALL'

EmbeddingsService.create_embeddings(filename_to_embed)

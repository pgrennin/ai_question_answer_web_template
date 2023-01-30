# Place a txt file in assets/raw directory, then add the filename here:
#FILE_NAME_TO_CREATE_EMBEDDING="tsla_earnings_transcript_q3_2022.txt"

docker exec -it omniscient-web conda run --no-capture-output -n myenv python /app/create_embeddings.py #$FILE_NAME_TO_CREATE_EMBEDDING

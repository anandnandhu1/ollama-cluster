FROM ollama/ollama
RUN ollama pull gemma:3b
ENV OLLAMA_NUM_PARALLEL=4

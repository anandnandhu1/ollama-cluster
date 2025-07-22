FROM ollama/ollama
RUN ollama pull tinyllama
ENV OLLAMA_NUM_PARALLEL=2

REQUEST_QUEUE_TIMEOUT_S = 1
NUM_WORKERS = 10
GRACEFUL_WORKER_EXIT_WAIT_S = 10

# This must be larger than GRACEFUL_WORKER_EXIT_WAIT_S, since this one subsumes 
# the other.
GRACEFUL_AGENT_EXIT_WAIT_S = 15

HTTP_POOL_SIZE = 10
REQUEST_WAIT_PERIOD_S = 1
DOWNLOAD_PATH = '/tmp/gdrive/downloads'
CHUNK_SIZE = 1024*1024

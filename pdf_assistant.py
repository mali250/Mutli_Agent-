from phi.storage.agent.postgres import PgAgentStorage
from phi.agent import Agent
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Create a storage backend using the Postgres database
storage = PgAgentStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # db_url: Postgres database URL
    db_url=db_url,
)

# Add storage to the Agent
agent = Agent(storage=storage)
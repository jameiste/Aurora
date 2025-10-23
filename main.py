import asyncio
# Local imports
from functions.notification import aurora_alert
from environment.variables import TIME_THRESHOLD

# Function: Run every now and then
async def run_once():
    await asyncio.to_thread(aurora_alert)  

# Function: Schedule
async def scheduler(interval_seconds: int = TIME_THRESHOLD):
    while True:
        await run_once()
        await asyncio.sleep(interval_seconds)

# Start app
if __name__ == "__main__":
    asyncio.run(scheduler())

import asyncio
import datetime
# Local imports
from functions.notification import aurora_alert
from environment.variables import TIME_THRESHOLD, REQUEST_TIMEOUT

# Function: Run every now and then
async def run_once():
    print(f"Run at {datetime.datetime.now().isoformat()}", flush=True)
    # Error handling
    try:
        await asyncio.wait_for(asyncio.to_thread(aurora_alert(notification="bark")), timeout=REQUEST_TIMEOUT + 5)
        print("Run finished", flush=True)
    except Exception as e:
        print(f"Run error: {e}", flush=True)
        
# Function: Schedule
async def scheduler():
    while True:
        await run_once()
        print(f"Sleeping {TIME_THRESHOLD} seconds...\n", flush=True)
        await asyncio.sleep(TIME_THRESHOLD)

# Start app
if __name__ == "__main__":
    asyncio.run(scheduler())

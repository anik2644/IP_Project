from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Provide the correct path to the JSON file
json_file_path = 'C:/Users/anik1/Documents/WebPractise/events.json'


# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extract events from the JSON data
events = data['events']

@app.get("/events")
async def get_all_events():
    return events

@app.get("/events/{event_id}")
async def get_event_by_id(event_id: int):
    for event in events:
        if event['id'] == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

@app.post("/events")
async def create_event():
    # Here you can implement the logic to create a new event
    # For demonstration purposes, let's add a dummy event
    new_event = {
        "id": len(events) + 1,
        "title": "New Event",
        "date": "YYYY-MM-DD",
        "location": "Location",
        "description": "Description",
        "organizer": "Organizer"
    }
    events.append(new_event)
    return new_event

@app.put("/events/{event_id}")
async def update_event(event_id: int):
    for event in events:
        if event['id'] == event_id:
            # Here you can implement the logic to update properties of an event
            # For demonstration purposes, let's update the title of the event
            event['title'] = "Updated Event Title"
            return event
    raise HTTPException(status_code=404, detail="Event not found")

@app.delete("/events/{event_id}")
async def delete_event(event_id: int):
    for i, event in enumerate(events):
        if event['id'] == event_id:
            del events[i]
            return {"message": "Event deleted successfully"}
    raise HTTPException(status_code=404, detail="Event not found")

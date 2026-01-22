import datetime

class SoundEngineer:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

class StudioRoom:
    def __init__(self, room_name, base_price):
        self.room_name = room_name
        self.base_price = base_price

class RecordingSession:
    def __init__(self, client_name, studio_room, engineer, duration_hours):
        self.client_name = client_name
        self.studio_room = studio_room
        self.engineer = engineer
        self.duration_hours = duration_hours
        self.timestamp = datetime.datetime.now()

    def calculate_total_cost(self):
        # Total = (Room Base Price + Engineer Rate) * Hours
        total = (self.studio_room.base_price + self.engineer.hourly_rate) * self.duration_hours
        return total

    def generate_report(self):
        print(f"--- Session Report: {self.client_name} ---")
        print(f"Room: {self.studio_room.room_name}")
        print(f"Engineer: {self.engineer.name}")
        print(f"Duration: {self.duration_hours} hours")
        print(f"Total Cost: ${self.calculate_total_cost():.2f}")
        print("-" * 30)

# Implementation execution
if __name__ == "__main__":
    # Create Resources
    vocal_booth = StudioRoom("Vocal Booth A", 50.0)
    lead_engineer = SoundEngineer("Alex Sterling", 75.0)

    # Create a Booking
    new_session = RecordingSession("The Midnight Band", vocal_booth, lead_engineer, 4)
    
    # Output result
    new_session.generate_report()

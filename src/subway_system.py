
# subway_system.py

# Define the SubwaySystem class
class SubwaySystem:
    def __init__(self):
        # Dictionary to store check-ins: card_id maps to (station, time)
        self.check_ins = {}  # card_id -> (station, time)
        # Dictionary to store trips: (start_station, end_station) maps to list of durations
        self.trips = {}      # (start_station, end_station) -> list of durations

    def check_in(self, card_id, station, time):
        # Check if the card is already checked in
        if card_id in self.check_ins:
            print(f"Error: Card {card_id} already checked in.")  # Print error if already checked in
        else:
            # Store the check-in information for the card
            self.check_ins[card_id] = (station, time)
            print(f"✅ Checked in card {card_id} at {station} at time {time}.")  # Confirm check-in

    def check_out(self, card_id, station, time):
        # Check if the card was checked in
        if card_id not in self.check_ins:
            print(f"Error: Card {card_id} did not check in.")  # Print error if not checked in
            return  # Exit the function

        # Retrieve the start station and time from check-ins
        start_station, start_time = self.check_ins[card_id]
        # Calculate the duration of the trip
        duration = time - start_time

        # If this route hasn't been recorded yet, create a new list for it
        if (start_station, station) not in self.trips:
            self.trips[(start_station, station)] = []

        # Add the duration to the list of trips for this route
        self.trips[(start_station, station)].append(duration)
        # Remove the card from check-ins since the trip is complete
        del self.check_ins[card_id]

        # Print confirmation of check-out and trip duration
        print(f"✅ Checked out card {card_id} at {station}. Trip took {duration} minutes.")

    def get_average_distance(self, start, end):
        # Create a route tuple from start and end stations
        route = (start, end)
        # Check if there are any trips recorded for this route
        if route not in self.trips or len(self.trips[route]) == 0:
            print(f"❌ No trip data from {start} to {end}.")  # Print error if no data
            return  # Exit the function

        # Get the list of durations for this route
        durations = self.trips[route]
        # Calculate the average duration
        average = sum(durations) / len(durations)
        # Print the average trip duration
        print(f"🧠 Average trip from {start} to {end}: {average:.2f} minutes.")


# Main function to run the subway system interface
def main():
    # Create an instance of SubwaySystem
    system = SubwaySystem()

    # Print welcome message
    print("\n🚇 Welcome to MhanStevo Subway Payment System 🚇")

    # Loop to continuously accept user commands
    while True:
        # Prompt user for a command
        command = input("\nEnter command (checkin, checkout, avg, exit): ").strip().lower()

        # If user wants to check in
        if command == "checkin":
            card_id = input("Card ID: ")  # Get card ID
            station = input("Station: ")  # Get station name
            try:
                time = int(input("Time (in minutes): "))  # Get time and convert to integer
            except ValueError:
                print("Invalid time format. Please enter an integer.")  # Handle invalid input
                continue  # Skip to next loop iteration
            system.check_in(card_id, station, time)  # Call check_in method

        # If user wants to check out
        elif command == "checkout":
            card_id = input("Card ID: ")  # Get card ID
            station = input("Station: ")  # Get station name
            try:
                time = int(input("Time (in minutes): "))  # Get time and convert to integer
            except ValueError:
                print("Invalid time format. Please enter an integer.")  # Handle invalid input
                continue  # Skip to next loop iteration
            system.check_out(card_id, station, time)  # Call check_out method

        # If user wants to get average trip duration
        elif command == "avg":
            start = input("Start station: ")  # Get start station
            end = input("End station: ")      # Get end station
            system.get_average_distance(start, end)  # Call get_average_distance method

        # If user wants to exit the program
        elif command == "exit":
            print("👋 Exiting system. Goodbye!")  # Print exit message
            break  # Exit the loop and program

        # If user enters an invalid command
        else:
            print("❌ Invalid command. Try again.")  # Print error message


# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
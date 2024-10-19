This project implements a Smart Parking System using a Segment Tree data structure in C++. The goal is to efficiently manage and query the availability of parking spots based on real-time reservations and dynamically updated time intervals. Each parking spot can be reserved for a specified time, and the system automatically tracks when each spot will become available again.

Key Features:
Real-time Parking Management:

The system manages the status of parking spots (whether they are available or reserved) and tracks when a spot is going to become free.
The system can provide real-time updates on the number of available spots and the minimum time until the next parking spot becomes free.
Efficient Querying with Segment Tree:

A segment tree is used to store the status of parking spots and their corresponding free times, allowing for fast querying of the number of available spots and the minimum free time in any given range of spots.
The segment tree helps to efficiently update the status and free time when a reservation is made or a spot becomes available.
Periodic Time Updates:

The system periodically decreases the time remaining for reserved spots. Once the reserved time expires, the spot automatically becomes available again.
This time update happens in real-time (simulated in the code), with the system dynamically adjusting the availability of spots.
Code Overview:
Data Structure:

Each parking spot is represented by a ParkingSpot struct, which stores the status (0 for available, 1 for reserved) and freeTime (the time in minutes when the spot will become available).
The segment tree is built from an array of ParkingSpot structs, allowing for efficient range queries and updates.
Functions:

build(): Initializes the segment tree from the list of parking spots.
update(): Updates the status and free time of a specific parking spot.
query(): Returns the number of available spots and the minimum time until the next spot becomes available within a specified range.
decreaseFreeTime(): Periodically decreases the free time for all reserved spots and updates their availability status when the time reaches zero.
Usage:
Reserve a Spot: When a user reserves a spot, the system updates the status to "reserved" and sets the free time according to the user's reservation.
Check Availability: Users can check if parking spots are available, and if none are available, the system informs them of when the next spot will become free.
Real-time Updates: The system continuously updates the free times of reserved spots, making it easy for users to see when a spot will become available.
Example:
The system initializes with 5 parking spots. Some spots are available, and others are reserved for specific durations (e.g., 5 or 10 minutes).
The system can query the number of available spots and the minimum time for a spot to become available.
It simulates time passing, updating the free time for reserved spots every second (each second represents one minute in real-time).
Future Enhancements:
Add a user interface for customers to easily reserve spots and check availability.
Extend the system to support multiple parking lots and manage reservations across different locations.
Integrate the system with hardware sensors for real-time monitoring of parking spot occupancy.
This smart parking solution is ideal for modern parking lots that need efficient management of limited parking spots and real-time information for customers.

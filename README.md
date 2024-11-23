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

Integrate the system with hardware sensors for real-time monitoring of parking spot occupancy.
This smart parking solution is ideal for modern parking lots that need efficient management of limited parking spots and real-time information for customers.

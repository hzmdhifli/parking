#include <bits/stdc++.h>
/*#include <iostream>
#include <vector>
#include <climits>  // For INT_MAX
#include <chrono>
#include <thread>*/

using namespace std;

struct ParkingSpot {
    int status;  // 0 for available, 1 for reserved
    int freeTime; // Time (in minutes) when this spot becomes available
};

class SegmentTree {
public:
    SegmentTree(int n) {
        this->n = n;
        spots.resize(n);
        tree.resize(2 * n, {0, INT_MAX});  // {status, freeTime} default: available and max time
    }

    // Build the segment tree from the initial parking spots
    void build(const vector<ParkingSpot>& parkingSpots) {
        for (int i = 0; i < n; i++) {
            spots[i] = parkingSpots[i];  // Store the original parking spots
            tree[n + i] = parkingSpots[i];  // Leaf nodes
        }

        // Build the tree by calculating availability and minimum free time
        for (int i = n - 1; i > 0; --i) {
            tree[i].status = tree[2 * i].status + tree[2 * i + 1].status;
            tree[i].freeTime = min(tree[2 * i].freeTime, tree[2 * i + 1].freeTime);
        }
    }

    // Update a parking spot when reserved/freeTime changes
    void update(int index, int newStatus, int freeTime) {
        index += n;
        tree[index] = {newStatus, freeTime};

        // Update the parent nodes
        for (int i = index / 2; i > 0; i /= 2) {
            tree[i].status = tree[2 * i].status + tree[2 * i + 1].status;
            tree[i].freeTime = min(tree[2 * i].freeTime, tree[2 * i + 1].freeTime);
        }
    }

    // Query how many available spots and the minimum time until the next spot becomes available
    pair<int, int> query(int l, int r) {
        l += n;
        r += n;
        int available = 0;
        int minFreeTime = INT_MAX;

        while (l < r) {
            if (l % 2 == 1) {
                available += tree[l].status == 0 ? 1 : 0;
                minFreeTime = min(minFreeTime, tree[l].freeTime);
                l++;
            }
            if (r % 2 == 1) {
                --r;
                available += tree[r].status == 0 ? 1 : 0;
                minFreeTime = min(minFreeTime, tree[r].freeTime);
            }
            l /= 2;
            r /= 2;
        }
        return {available, minFreeTime};
    }

    // Function to periodically update freeTime
    void decreaseFreeTime() {
        for (int i = 0; i < n; i++) {
            if (tree[n + i].freeTime > 0) {
                tree[n + i].freeTime--;
                if (tree[n + i].freeTime == 0) {
                    tree[n + i].status = 0;  // Mark the spot as available when time is up
                }
            }
        }

        // Update parent nodes in the segment tree
        for (int i = n - 1; i > 0; --i) {
            tree[i].status = tree[2 * i].status + tree[2 * i + 1].status;
            tree[i].freeTime = min(tree[2 * i].freeTime, tree[2 * i + 1].freeTime);
        }
    }

private:
    vector<ParkingSpot> spots;  // Original parking spots
    vector<ParkingSpot> tree;   // Segment tree to store {status, freeTime}
    int n;
};

int main() {
    int n = 5;  // Number of parking spots
    vector<ParkingSpot> parkingSpots = {
        {0, 0}, {1, 5}, {0, 0}, {1, 10}, {0, 0}
    };

    // Initialize the segment tree
    SegmentTree segTree(n);
    segTree.build(parkingSpots);

    // Query the availability and minimum free time for the range [0, 5)
    pair<int, int> result = segTree.query(0, 5);
    cout << "Available spots: " << result.first << endl;
    cout << "Minimum free time: " << result.second << " minutes" << endl;

    // Simulate periodic updates (decreasing free time by 1 minute every second)
    cout << "Starting countdown for reserved spots..." << endl;
    for (int i = 0; i < 10; ++i) {
        segTree.decreaseFreeTime();
        result = segTree.query(0, 5);
        cout << "Available spots: " << result.first << ", Minimum free time: " << result.second << " minutes" << endl;
        this_thread::sleep_for(chrono::seconds(1));  // Simulate time passing (1 minute = 1 second)
    }

    return 0;
}

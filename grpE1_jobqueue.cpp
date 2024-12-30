/*Queues are frequently used in computer programming, and a typical example is the
creation of a job queue by an operating system. If the operating system does not use
priorities, then the jobs are processed in the order they enter the system. Write C++
program for simulating job queue. Write functions to add job and delete job from queue.*/
#include <iostream>
using namespace std;

const int MAX_SIZE = 10;

class JobQueue {
private:
    int front, rear;
    int queue[MAX_SIZE];

public:
    JobQueue() {
        front = -1;
        rear = -1;
    }

    bool isFull() {
        return rear == MAX_SIZE - 1;
    }

    bool isEmpty() {
        return front == -1;
    }

    void enqueue(int job) {
        if (isFull()) {
            cout << "Overflow!!! [Queue is Full]" << endl;
        } else {
            if (isEmpty()) {
                front = 0;
            }
            rear++;
            queue[rear] = job;
            cout << "Job " << job << " added to the queue." << endl;
        }
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Underflow!!! [Queue is Empty]" << endl;
        } else {
            cout << "Deleted Job: " << queue[front] << endl;
            if (front == rear) {
                front = rear = -1;
            } else {
                front++;
            }
        }
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is Empty!" << endl;
        } else {
            cout << "Queue Contains: ";
            for (int i = front; i <= rear; i++) {
                cout << queue[i] << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    JobQueue jobQueue;
    jobQueue.enqueue(1);
    jobQueue.enqueue(2);
    jobQueue.enqueue(3);
    jobQueue.display();
    jobQueue.dequeue();
    jobQueue.display();

    return 0;
}


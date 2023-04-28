#include<iostream>
#include<stdlib.h>
using namespace std;
#define max 10
struct queue
{
	int data[max];
	int front,rear;
};
class Queue
{
	struct queue q;
    public:
	Queue()
	{
		q.front=q.rear=1;
	}
	
	int isempty();
	int isfull();
	void enqueue(int x);
	int delqueue();
	void display();
};
int Queue::isempty()
{
	return (q.front==q.rear)?1:0;
}
int Queue::isfull()
{
	return (q.rear==max-1)?1:0;
}
void Queue::enqueue(int x)
{
	q.data[++q.rear]=x;
}
int Queue::delqueue()
{
	return q.data[++q.front];
}
void Queue::display()
{
	int i;
	cout<<"\n";
	for(i=q.front+1;i<=q.rear;i++)
	{
		cout<<q.data[i]<<" ";
	}
}
int main()
{
	Queue obj;
	int ch,x;
	do
	{
		cout<<"\n1.Insert a job.  \n2.Delete a job;  \n3.Display jobs.  \n4.Exit from the program.\n";
		cout<<"Enter your choice :   ";
		cin>>ch;
		

		switch(ch)
		{
			case 1:
				if(!obj.isfull())
				{
					cout<<"\nEnter data : ";
					cin>>x;
					obj.enqueue(x);
				}
				else
				{
					cout<<"Queue is overflow.";
				}
				break;
			case 2:
				if(!obj.isempty())
				{
					cout<<"\nDeleted Element =  "<<obj.delqueue();
				}
				else
				{
					
					cout<<"\nQueue is underflow.";
				}
				cout<<"\nRemaining Jobs : ";
				obj.display();
				break;
			case 3:
				if(!obj.isempty())
				{
					cout<<"\nQueue contains : ";
					obj.display();
					cout<<"\n\n";
				}
				else
				{
					cout<<"Queue is empty ";
				}
				break;
			case 4:
				exit(0);
				break;
			default:
				cout<<"Invalid choice!";
				break;
		}
	}while(ch!=5);
}



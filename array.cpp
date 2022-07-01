#include <iostream>

using namespace std;

int que[50];
int y= 50;
int front = - 1;
int rear = - 1;
void insert() {
int x;
if (rear == y - 1)
cout<<" Overflow"<<endl;
else {
front = 0;
cout<<" insert value  : "<<endl;
cin>>x;
rear++;
que[rear] = x;
}
}
void delete1() {
if (front == - 1) {
cout<<"Underflow";
} else {
cout<<"Element deleted  : "<< que[front] <<endl;
front++;;
}
}
void display () {
if (front == - 1 )
cout<<" empty"<<endl;
else {
cout<<" elements are : ";
for (int i = front; i <= rear; i++)
cout<<que[i]<<" ";
cout<<endl;
}
}
int main() {
int option;
cout<<"1) insert "<<endl;
cout<<"2) delete"<<endl;
cout<<"3) display "<<endl;
cout<<"4) Exit"<<endl;
do {
cout<<" choice : "<<endl;
cin>>option;
switch (option) {
case 1: insert();
break;
case 2: delete1();
break;
case 3: display ();
break;
case 4: cout<<"Exit"<<endl;
break;
default: cout<<"not found"<<endl;
break;
}
} while(option!=0);
return 0;
}

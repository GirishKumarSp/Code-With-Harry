package com.company;
import java.util.Scanner;

//1 Write a program to sum three numbers in Java.
//2 Write a program to calculate CGPA using marks of three subjects (out of 100)
//3 Write a Java program that asks the user to enter his/her name and greets them with “Hello <name>, have a good day” text.
//4 Write a Java program to convert Kilometers to miles.
//5 Write a Java program to detect whether a number entered by the user is an integer or not.

public class Practice_Set_Questions {
    public static void main(String[] args) {
//        Question 1
        Scanner sc = new Scanner(System.in);
        System.out.print("enter first number :");
        int a=sc.nextInt();
        System.out.print("enter second number :");
        int b=sc.nextInt();
        System.out.print("enter third number :");
        int c=sc.nextInt();
        System.out.print("The sum of the three numbers are :");
        System.out.println(a+b+c);

//        Question 2
        System.out.print("enter first Subject marks :");
        float subject1=sc.nextInt();
        System.out.print("enter second Subject marks :");
        float subject2=sc.nextInt();
        System.out.print("enter third Subject marks :");
        float subject3=sc.nextInt();
        float cgpa=(subject1+subject2+subject3)/30;
        System.out.println("Your CGPA is:"+cgpa);

//        Question 3
        System.out.print("Enter Your Name :");
        String name=sc.next();
        System.out.println("Hello "+name+" have a good day");

//        Question 4
        System.out.print("Enter Kilometers :");
        float Kilometers=sc.nextInt();
        double miles = Kilometers / 1.6;
        System.out.println("converted value of Kilometers to miles :"+miles);

//        Question 5
        System.out.print("enter number to check:");
        System.out.println(sc.hasNextInt());
    }

}

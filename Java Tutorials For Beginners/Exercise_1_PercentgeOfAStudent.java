//Question
//Write a program to calculate the percentage of a given student in the CBSE board exam.
//His marks from 5 subjects must be taken as input from the keyboard. (Marks are out of 100)
package com.company;
import java.util.Scanner;

public class Exercise_1_PercentgeOfAStudent {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //System.in is a standard input stream.
        System.out.println("Enter All 5 subject marks: "); //reads marks.
        System.out.print("Enter 1st subject marks: "); //reads marks.
        int a=sc.nextInt();
        System.out.print("Enter 2nd subject marks: "); //reads marks.
        int b=sc.nextInt();
        System.out.print("Enter 3rd subject marks: "); //reads marks.
        int c=sc.nextInt();
        System.out.print("Enter 4th subject marks: "); //reads marks.
        int d=sc.nextInt();
        System.out.print("Enter 5th subject marks: "); //reads marks.
        int e=sc.nextInt();
        float Sum=a+b+c+d+e; //adds all 6 subject marks
        System.out.print("Enter Total marks: "); //reads Total marks.
        int Total= sc.nextInt();
        float Percentage=(Sum/Total)*100; //converting into percentage
        System.out.println("Your Percentage Is :"+Percentage);
    }
}
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
class Solution
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        int [] wynik = new int[N];
        List<int[]> input = new List<int[]>();
        List<int> E = new List<int>();
        for (int i = 0; i < N; i++)
        {
            string[] a = Console.ReadLine().Split(' ');
            int[] element = new int[4];
            element[0] = int.Parse(a[0]);
            element[1] = int.Parse(a[1]);
            element[2] = a[2] == "E" ? -1 : int.Parse(a[2]);
            element[3] = a[3] == "E" ? -1 : int.Parse(a[3]);
            input.Add(element);
        }
        wynik[0] = input[0][1];
        for(int i = 0; i < N; i++)
        {
            int w = input[i][2];
            int z = input[i][3];
            if(w != -1){wynik[w] = Math.Max(wynik[w],wynik[i]+input[w][1]);}
            if(z != -1){wynik[z] = Math.Max(wynik[z],wynik[i]+input[z][1]);}
            if(z==-1 || w ==-1){E.Add(wynik[i]);}
        }
        Console.WriteLine(E.Max());
    }
}
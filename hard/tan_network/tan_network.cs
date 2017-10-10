using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;


class Przystanek
{
    public string id {get; set;}
    public string name {get; set;}
    public double lat {get; set;}
    public double lon {get; set;}
    public List<int> dojazd = new List<int>();
    public List<double> dystans = new List<double>();
    
    public void Wczytaj()
    {
        string[] a = Console.ReadLine().Split(',');
        this.id = a[0].Substring(9);
        this.name = a[1].Substring(1, a[1].Length - 2);
        this.lat = Double.Parse(a[3]);
        this.lon = Double.Parse(a[4]);
    }
    public void Przydziel(int stdo, double latn, double lonn)
    {
        this.dojazd.Add(stdo);
        double a = toRadians(lonn-this.lon);
        double b = toRadians(latn+this.lat);
        double y = toRadians(latn-this.lat);
        double x = a*Math.Cos(b/2);
        double d = Math.Sqrt(x*x +y*y)*6371;
        this.dystans.Add(d);
    }
    static double toRadians(double deg)
    {
        return deg*Math.PI/180;
    }
}
public class intComparer: IComparer<int[]>
{
    public int Compare(int[] x, int[] y)
    {
        return x[1].CompareTo(y[1]);
    }
}
class Solution
{
    static DateTime start = DateTime.Now;
    private static void dumpTime()
    {
        var totalSeconds = (new TimeSpan(DateTime.Now.Ticks - start.Ticks)).TotalSeconds;
        Console.Error.WriteLine(totalSeconds);
    }
    static bool LContains(List<int[]> lista, int[] array, int wiersz)
    {
        int dllisty = lista.Count;
        bool wynik = false;
        for(int i = 0; i < dllisty; i++)
        {
            wynik = areequal(lista[i], array, wiersz);
            if(wynik == true){break;}
        }
        return wynik;
    }
    static bool areequal(int[] first, int[] second, int wiersz)
    {
        int dl1 = first.Length;
        int dl2 = second.Length;
        if(dl1 != dl2 || wiersz > dl1 || wiersz > dl2)
        {
            return false;
        }
        else
        {
            bool test = false;
            test = (first[wiersz] == second[wiersz]) ? true : false;
            return test;
        }
    }
    static void Main(string[] args)
    {
        string startPoint = Console.ReadLine().Substring(9);
        string endPoint = Console.ReadLine().Substring(9);
        int N = int.Parse(Console.ReadLine());
        List<Przystanek> Przystanki = new List<Przystanek>();
        for (int i = 0; i < N; i++)
        {
            Przystanki.Add(new Przystanek());
            Przystanki[Przystanki.Count-1].Wczytaj();
        }
        int startid = Przystanki.FindIndex(x => x.id == startPoint);
        int endid = Przystanki.FindIndex(x => x.id == endPoint);
        int M = int.Parse(Console.ReadLine());
        for (int i = 0; i < M; i++)
        {
            string[] route = Console.ReadLine().Split(' ');
            string Pz = route[0].Substring(9);
            string Pdo = route[1].Substring(9);
            int indz = Przystanki.FindIndex(x => x.id == Pz);
            int inddo = Przystanki.FindIndex(x => x.id == Pdo);
            double latn = Przystanki[inddo].lat;
            double lonn = Przystanki[inddo].lon;
            Przystanki[indz].Przydziel(inddo, latn, lonn);
        }
        if(startid == endid)
        {
            Console.WriteLine(Przystanki[startid].name);
        }
        else
        {
            int curid;
            int licznik = 0;
            List<int[]> odstartu = new List<int[]>(); // 0 - poprzedni przystanek id, 1 - poziom
            odstartu.Add(new int[]{startid, 0, -1, 0});
            intComparer dc = new intComparer();
            do
            {
                curid = odstartu[licznik][0];
                int ldojazd = Przystanki[curid].dojazd.Count;
                for(int i = 0; i < ldojazd; i++)
                {
                    double oo = Przystanki[curid].dystans[i] * 1000 + odstartu[licznik][1];
                    int[] test = new int[]{Przystanki[curid].dojazd[i], (int)oo, curid, licznik};
                    if(LContains(odstartu, test, 0) == false)
                    {
                        odstartu.Add(test);
                    }
                    else if(LContains(odstartu, test, 0) == true && odstartu[odstartu.FindIndex(x => x[0] == test[0])][1] > oo)
                    {
                        int indeksdupy = odstartu.FindIndex(x => x[0] == test[0]);
                        odstartu.Add(test);
                        odstartu.RemoveRange(indeksdupy,1);
                    }
                }
                odstartu.Sort(licznik + 1, odstartu.Count - licznik - 1, dc);
                licznik++;
            }
            while(licznik < odstartu.Count);
            List<int> wyswietl = new List<int>();
            wyswietl.Add(endid);
            if(odstartu.Exists(x => x[0] == endid) == true)
            {
                int nextid;
                do
                {
                    int previd = wyswietl[wyswietl.Count-1];
                    nextid = odstartu.Find(x => x[0] == previd)[2];
                    int[] u = odstartu.Find(x => x[0] == previd);
                    wyswietl.Add(nextid);
                }
                while(nextid != startid);
                wyswietl.Reverse();
                foreach(int a in wyswietl)
                {
                    Console.WriteLine(Przystanki[a].name);
                }
            }
            else {Console.WriteLine("IMPOSSIBLE");}
        }
        dumpTime();
    }
}
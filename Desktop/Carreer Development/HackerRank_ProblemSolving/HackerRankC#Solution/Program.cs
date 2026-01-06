namespace HackerRankC_Solution;

using System.Collections;
using System.Runtime.InteropServices;

class Program
{
    static void Main(string[] args)
    {
        NeetCode150.ValidAnagram();
    }


}
class NeetCode150
{
    public static void ValidAnagram()
    {
        Hashtable countT = new Hashtable();
        Hashtable countS = new Hashtable();

        string s = "racecar", t = " carrace";
        if (s.Length != t.Length)
        {
            Console.Write(false);
        }

        foreach (char charac in s)
        {
            countS.Add(charac, 1);
        }
        Console.WriteLine(countS);
    }

}

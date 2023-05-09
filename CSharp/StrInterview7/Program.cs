using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrInterview7
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string: ");
            string word = Console.ReadLine().ToLower();

            int vowels = 0;
            int cons = 0;

            for (int lcv = 0; lcv < word.Length; lcv++) {
                char let = word[lcv];
                if (let == 'a' || let == 'e' || let == 'i' ||
                    let == 'o' || let == 'u')
                    vowels++;
                else if (let >= 'a' && let <= 'z') cons++;  // Check ASCII range
            }

            Console.WriteLine(word + " contains " + vowels +
                   " vowels, and " + cons + " consonants");
            Console.ReadLine();
        }
    }
}

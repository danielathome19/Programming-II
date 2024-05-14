namespace StrInterview7 {
    internal class Program {
        static void Main(string[] args) {
            Console.Write("Enter a string: ");
            string word = Console.ReadLine().ToLower();

            int vowels = 0;
            int cons = 0;

            for (int lcv = 0; lcv < word.Length; lcv++) {
                char ltr = word[lcv];
                if (ltr == 'a' || ltr == 'e' || ltr == 'i' ||
                    ltr == 'o' || ltr == 'u')
                    vowels++;
                else if (ltr >= 'a' && ltr <= 'z') cons++;  // Check ASCII range
            }

            Console.WriteLine($"{word} contains {vowels} vowels, and {cons} consonants");
            Console.ReadLine();
        }
    }
}

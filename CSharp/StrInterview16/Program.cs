static bool searchText(string text, string search) {
    int tLen = text.Length;
    int sLen = search.Length;

    if (sLen > tLen) return false;

    for (int i = 0; i <= tLen - sLen; i++)
        // if (text[i..(i + sLen)] == search) return true;  // text[i:i+sLen]
        if (text.Substring(i, sLen) == search) return true;
    // Substring uses startIndex, length (not endIndex)
    return false;
}

Console.Write("Enter a string: ");
string text = Console.ReadLine();
Console.Write("Enter a substring to search for: ");
string word =  Console.ReadLine();
bool result = searchText(text, word);
Console.WriteLine("Does \"{0}\" contain \"{1}\"?: {2}", text, word, result);
// Console.WriteLine($"Does \"{text}\" contain \"{word}\"?: {result}");
Console.ReadLine();
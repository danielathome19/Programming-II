/* using System.Collections.Generic; */  // You may need to import

Console.WriteLine("Hello, World!");

// Lists are equivalent to Python lists
// List<TYPE> name = new List<TYPE>();
List<string> text = [];  // C# 12 onward
List<string> lines = new List<string>();  //  { "hi", "hey" }

List<int> numbers = [1, 2, 3];  // C# 12 onward
List<int> nums = new List<int>() { 1, 2, 3 };

nums.Add(4);
nums.Add(5);
nums.Add(6);
nums.Add(7);
nums.RemoveAt(5);  // Removes '6'
nums.Remove(7);  // Removes '7'
Console.WriteLine("Length: " + nums.Count);
Console.WriteLine(string.Join(", ", nums));  // "1, 2, 3, 4, 5"

foreach (int n in nums)
    Console.WriteLine(n);

// Look at C# documentation on MSDN for all List methods
nums[0] = 100;
Console.WriteLine(nums[0]);
Console.ReadLine();
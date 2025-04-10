Console.Write("Enter length: ");
int len = int.Parse(Console.ReadLine());
Console.Write("Enter width: ");
int wid = int.Parse(Console.ReadLine());
int area = len * wid;
int perim = 2 * len + 2 * wid;
Console.WriteLine("Area: " + area);
Console.WriteLine("Perimeter: " + perim);
Console.ReadLine();
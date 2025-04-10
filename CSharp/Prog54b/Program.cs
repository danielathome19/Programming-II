using static System.Console;
Write("Enter num1: ");
int num1 = int.Parse(ReadLine());
Write("Enter num2: ");
int num2 = int.Parse(ReadLine());
Write("Enter num3: ");
int num3 = int.Parse(ReadLine());
Write("Enter num4: ");
int num4 = int.Parse(ReadLine());

int sum = num1 + num2 + num3 + num4;
double average = (double)sum / 4;
WriteLine("Sum: " + sum);
WriteLine("Average: " + Math.Round(average, 2));
ReadKey();

Console.Write("Enter num1: ");
int num1 = int.Parse(Console.ReadLine());
Console.Write("Enter num2: ");
int num2 = int.Parse(Console.ReadLine());

int sum = num1 + num2;
int dif = num1 - num2;
int prd = num1 * num2;
double avg = (double)sum / 2.0;
int abs = Math.Abs(dif);
// Math.Max and Math.Min
int max, min;

if (num1 > num2) {
    max = num1;
} else {
    max = num2;
}

if (num1 <= num2)
    min = num1;
else min = num2;
// else if

Console.WriteLine("Sum: " + sum);
// TODO: print the rest
Console.WriteLine("Max: " + max);
Console.WriteLine("Min: " + min);
Console.ReadLine();
Console.Write("Enter # of copies to print: ");
int copies = int.Parse(Console.ReadLine());
double price = 0;
double cost = 0;
// && AND, || OR, ! NOT
if (copies > 0 && copies <= 99)         price = 0.30;
else if (copies > 99 && copies <= 499)  price = 0.28;
else if (copies > 499 && copies <= 749) price = 0.27;
// TODO: the rest
else Console.WriteLine("Invalid number of copies!");

// TODO
namespace CalcWithFunctions {
    internal class Program {
        static void Main(string[] args) {
            Console.Write("Enter num1: ");
            int n1 = int.Parse(Console.ReadLine());
            Console.Write("Enter num2: ");
            int n2 = int.Parse(Console.ReadLine());
            Console.Write("Choose an option: add, sub, mul, or div: ");
            string op = Console.ReadLine().ToLower();
            int result = 0;
            if (op == "add") result = add(n1, n2);
            else if (op == "sub") result = sub(n1, n2);
            else if (op == "mul") result = mul(n1, n2);
            else if (op == "div") result = div(n1, n2);
            Console.WriteLine("Result: " + result);
            wait();
        }

        // <access level> <static or not> <return type> name(<args) {}
        // In console apps, we'll make all functions "static"
        // Not static in Forms apps; always "public" though

        static void wait() {  // void means "returns nothing"
            Console.ReadLine();
            // return;
        }

        static int add(int x, int y) {
            return x + y;
        }

        static int sub(int x, int y) {
            return x - y;
        }

        static int mul(int x, int y) {
            return x * y;
        }

        static int div(int x, int y) {
            return x / y;
        }

    }
}

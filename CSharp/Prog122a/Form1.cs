namespace Prog122a {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            listBox1.Items.Clear();
            listBox1.Items.Add("Number\t\tSquare\t\tSquare Root");
            int lcv = 1;
            while (lcv <= 50) {
                int sqr = (int)Math.Pow(lcv, 2);
                double sqrt = Math.Sqrt(lcv);
                // listBox1.Items.Add(lcv + "\t\t" +
                //                    sqr + "\t\t" + Math.Round(sqrt, 4));
                listBox1.Items.Add($"{lcv}\t\t{sqr}\t\t{Math.Round(sqrt,4)}");
                // listBox1.Items.Add(string.Format("{0}\t\t{1}\t\t{2}", 
                //                                  lcv, sqr, Math.Round(sqrt, 4)));
                lcv++;  // lcv += 1
            }
        }
    }
}

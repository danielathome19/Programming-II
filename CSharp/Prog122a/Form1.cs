namespace Prog122a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("Number\t\tSquare\t\tSquare Root");
            int lcv = 1;
            while (lcv <= 50) {
                int sqr = (int)Math.Pow(lcv, 2);
                double sqrt = Math.Sqrt(lcv);
                listBox1.Items.Add(lcv + "\t\t" + sqr +
                                   "\t\t" + Math.Round(sqrt, 4));
                lcv++;
            }
        }
    }
}

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang366b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("The following numbers generated " +
                               "by the formula x^2 - x + 41 are:");
            int x = 1;
            while (true) {
                int number = (int)Math.Pow(x, 2) - x + 41;
                if (IsPrime(number, 2))
                    listBox1.Items.Add(number + "   prime");
                else {
                    int factor = FindSmallestFactor(number);
                    listBox1.Items.Add(number + 
                        "   test fails/factor=" + factor);
                    return;
                }
                x++;
            }
        }

        public bool IsPrime(int n, int f) {
            // Trial Division Algorithm
            if (n <= 1) return false;
            if (n == 2 || f * f > n) return true;
            if (n % f == 0) return false;
            return IsPrime(n, f + 1);
        }

        public int FindSmallestFactor(int n) {
            for (int lcv = 2; lcv <= Math.Sqrt(n); lcv++)
                if (n % lcv == 0) return lcv;
            return n;
        }
    }
}

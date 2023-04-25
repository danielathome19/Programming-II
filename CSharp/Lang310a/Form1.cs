using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang310a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Random rand = new Random();

            for (int lcv = 0; lcv < rand.Next(5, 11); lcv++) {
                double hist = rand.Next(0, 21) + rand.NextDouble();
                string msg = "";
                int max = (int)Math.Round(hist);
                for (int lcv2 = 0; lcv2 < max; lcv2++)
                    msg += "*";
                msg += " " + Math.Round(hist, 2);
                listBox1.Items.Add(msg);
            }
        }
    }
}

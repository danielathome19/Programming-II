using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSalesCS
{
    public partial class GeneralForm : Form
    {
        private Form myParent;
        public GeneralForm(Form prt)
        {
            InitializeComponent();
            this.myParent = prt;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        decimal decTAXRATE = 0.06m;  // Sales Tax Rate
        private decimal CalcTax(decimal cost)
        {
            // Returns the sales tax on ticket sales
            return cost * decTAXRATE;
        }

        private void GeneralForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }
    }
}

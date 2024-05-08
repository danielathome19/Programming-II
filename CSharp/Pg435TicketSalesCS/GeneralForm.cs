using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSalesCS {
    public partial class GeneralForm : Form {
        private Form myParent;

        public GeneralForm(Form myParent) {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e) {
            this.myParent.Show();
            this.Close();
        }

        private void GeneralForm_FormClosing(object sender, FormClosingEventArgs e) {
            this.myParent.Show();
        }

        // TODO: copy into student form
        decimal decTAXRATE = 0.06m;  // Sales tax
        private decimal CalcTax(decimal cost) {
            // Returns the sales tax on ticket sales
            return cost * decTAXRATE;
        }
    }
}

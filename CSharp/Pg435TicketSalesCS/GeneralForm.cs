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

        public GeneralForm(Form myParent) {  // Constructor (__init__)
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

        // TODO: decimal taxrate/calctax
    }
}

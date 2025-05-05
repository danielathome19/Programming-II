namespace Pg435TicketSalesCS {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            GeneralForm frm = new GeneralForm(this);
            // Python: frm = GeneralForm()
            frm.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e) {
            Form frm = new StudentForm(this);
            frm.Show();
            this.Hide();
        }
    }
}

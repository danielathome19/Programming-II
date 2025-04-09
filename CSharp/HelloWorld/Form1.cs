namespace HelloWorld {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            label1.Text = "Hello, world!";
        }

        private void button2_Click(object sender, EventArgs e) {
            label1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e) {
            Application.Exit();
        }
    }
}

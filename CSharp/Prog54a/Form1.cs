namespace Prog54a {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            int miles = 0;
            int gallons = 0;
            double mpg = 0;
            string car = comboBox1.Text;

            if (car == "1970 VW Bug") {
                miles = 286;
                gallons = 9;
            } else if (car == "1979 Firebird") {
                miles = 412;
                gallons = 40;
            }  // TODO: last 2 cars
            else {
                MessageBox.Show("Invalid selection!");
                return;  // Immediately exit the function, no 0/0
            }

            mpg = (double)miles / gallons;
            mpg = Math.Round(mpg, 1);
            lblMiles.Text = miles.ToString();
            lblGallons.Text = gallons.ToString();
            lblMpg.Text = mpg.ToString();
        }
    }
}
